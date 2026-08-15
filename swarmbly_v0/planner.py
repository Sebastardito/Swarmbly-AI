"""Prompt -> global contract + micro-task DAG.

Two artefacts come out of this module:

``global_contract(prompt, backend) -> Contract``
    The contract ``Gamma``: the small block of shared state that must travel
    with *every* packet for the fragments to be mutually consistent. Its size
    is one of the two things that drives ``rho`` (the other is the predecessor
    summaries), and every token in it is paid ``N`` times.

``plan(prompt, backend) -> Plan``
    A DAG whose nodes are micro-tasks and whose edges are *real* data
    dependencies. The edge set matters twice over: it decides which packets
    need a predecessor summary at all, and its level decomposition is the
    critical path that bounds any achievable speedup.

Both functions accept a backend so a real model can be used for extraction.
By default they run a deterministic heuristic path, because V0 must be
reproducible and runnable with no API keys; pass ``refine=True`` to let the
backend rewrite the objective.
"""

from __future__ import annotations

import hashlib
import re
from typing import Any, Sequence

from .schema import Contract, Plan, Task
from .textutil import (
    count_tokens,
    extract_entities,
    keywords,
    split_into_token_chunks,
    split_sentences,
    truncate_tokens,
)

__all__ = ["global_contract", "plan", "summarize_fragment", "suggest_n_tasks"]

_AUDIENCE_RE = re.compile(
    r"\bfor (?:an?|the)?\s*([a-z][a-z \-]{3,40}?)(?:\s+audience)?\s*(?:[.,;]|$)", re.I
)
_LENGTH_RE = re.compile(r"\b(\d{2,5})\s*(word|token)s?\b", re.I)
_FORBID_RE = re.compile(
    r"(?:do not use|don't use|avoid(?: using)?|never mention|without using)\s+([^.;\n]{3,80})", re.I
)
_ENUM_SPLIT_RE = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+", re.M)

_FORMAT_CUES: tuple[tuple[str, str], ...] = (
    ("json", r"\bjson\b|\bschema\b"),
    ("code", r"\bcode\b|\bfunction\b|\bclass\b|\bmodule\b|\bpython\b|\bimplement\b"),
    ("table", r"\btable\b|\bcsv\b|\bcolumns?\b|\bspreadsheet\b"),
    ("list", r"\bbullet\b|\blist\b|\benumerate\b|\bitemi[sz]e\b"),
    ("report", r"\breport\b|\bsections?\b|\bwhitepaper\b|\bmemo\b|\bbrief\b"),
    ("narrative", r"\bstory\b|\bnarrative\b|\bpoem\b|\bscene\b"),
)

_REGISTER_CUES: tuple[tuple[str, str], ...] = (
    ("casual", r"\bcasual\b|\binformal\b|\bconversational\b|\bfriendly\b|\bplain english\b"),
    ("formal", r"\bformal\b|\bacademic\b|\bprofessional\b|\btechnical\b|\bexecutive\b|\brigorous\b"),
)

_DEFAULT_FORBIDDEN = ("obviously", "as an AI language model", "in conclusion")


def _session_id(prompt: str) -> str:
    """Stable 12-hex-char id for a prompt (used to tie packets to a session)."""
    return hashlib.blake2b(prompt.encode("utf-8"), digest_size=6).hexdigest()


def _detect(cues: Sequence[tuple[str, str]], prompt: str, default: str) -> str:
    for label, pattern in cues:
        if re.search(pattern, prompt, re.I):
            return label
    return default


def global_contract(
    prompt: str,
    backend: Any | None = None,
    *,
    refine: bool = False,
    target_length_tokens: int | None = None,
) -> Contract:
    """Derive the global contract ``Gamma`` from ``prompt``.

    Args:
        prompt: The raw user prompt.
        backend: Optional backend, used only when ``refine`` is set.
        refine: Ask the backend to rewrite the objective. Off by default
            because it makes the contract non-deterministic across backends.
        target_length_tokens: Override the inferred answer length.

    Returns:
        A frozen :class:`~swarmbly_v0.schema.Contract`.
    """
    sentences = split_sentences(prompt)
    # Kept short on purpose: the objective is replicated into every packet, so
    # each of its tokens is paid N times and directly raises rho.
    objective = truncate_tokens(sentences[0] if sentences else prompt, 24).strip()

    if refine and backend is not None:
        try:
            refined = backend.generate(
                "Restate the following request as a single imperative objective "
                f"sentence.\n\n{prompt}\n",
                max_tokens=60,
            ).strip()
            if refined:
                objective = truncate_tokens(refined, 40)
        except Exception:
            pass  # A backend hiccup must never break planning.

    audience_match = _AUDIENCE_RE.search(prompt)
    audience = (audience_match.group(1).strip() if audience_match else "a technical reader")

    register = _detect(_REGISTER_CUES, prompt, "formal")
    output_format = _detect(_FORMAT_CUES, prompt, "report")

    if target_length_tokens is not None:
        target = int(target_length_tokens)
    else:
        length_match = _LENGTH_RE.search(prompt)
        if length_match:
            value = int(length_match.group(1))
            # Words -> tokens with the conventional ~1.3 factor.
            target = int(value * 1.3) if length_match.group(2).lower() == "word" else value
        else:
            target = 320
    target = max(120, min(target, 2000))

    forbidden = [m.group(1).strip().strip("\"'") for m in _FORBID_RE.finditer(prompt)]
    forbidden.extend(_DEFAULT_FORBIDDEN)
    seen: set[str] = set()
    unique_forbidden: list[str] = []
    for term in forbidden:
        key = term.lower()
        if key not in seen:
            seen.add(key)
            unique_forbidden.append(term)

    entities = extract_entities(prompt, min_mentions=1)[:6]
    if not entities:
        # Fall back to salient common nouns, left in their natural case: forcing
        # title case here would invent proper nouns the prompt never contained.
        entities = keywords(prompt, limit=3)

    return Contract(
        objective=objective,
        audience=audience,
        register=register,
        output_format=output_format,
        target_length_tokens=target,
        forbidden_terms=tuple(unique_forbidden[:6]),
        canonical_entities=tuple(entities),
        session_id=_session_id(prompt),
        prompt_tokens=count_tokens(prompt),
    )


def suggest_n_tasks(prompt: str, minimum: int = 2, maximum: int = 16) -> int:
    """Heuristic micro-task count when the caller does not specify ``N``.

    Explicit enumeration in the prompt wins; otherwise the count scales with
    prompt length at roughly one micro-task per 60 tokens.
    """
    enum_units = len([u for u in _ENUM_SPLIT_RE.split(prompt) if u.strip()]) - 1
    if enum_units >= minimum:
        return max(minimum, min(enum_units, maximum))
    return max(minimum, min(round(count_tokens(prompt) / 60) or minimum, maximum))


def _segment(prompt: str, n_tasks: int) -> list[str]:
    """Split ``prompt`` into exactly ``n_tasks`` non-empty units of work.

    Enumerated prompts split on their own bullets; otherwise sentences are
    packed into ``n_tasks`` roughly equal-token groups. When there is less
    material than requested tasks, the prompt is sliced by *tokens* instead of
    duplicating sentences: duplicating would inflate ``sum(|task_i|)`` above
    ``|P|`` and make ``rho = 1.0`` unreachable, destroying the floor of the
    sweep. ``N`` is always honoured exactly -- the sweep needs ``N`` to be the
    independent variable, not a suggestion.
    """
    units = [u.strip() for u in _ENUM_SPLIT_RE.split(prompt) if u.strip()]
    if len(units) < n_tasks:
        units = [s for s in split_sentences(prompt) if s.strip()]
    if not units:
        units = [prompt.strip() or "Answer the request."]

    if len(units) >= n_tasks:
        # Contiguous balanced partition. Every group gets at least one unit and
        # no unit is ever emitted twice -- duplicating a unit would inflate
        # sum(|task_i|) and silently raise the reachable rho floor.
        total = sum(count_tokens(u) for u in units)
        quota = total / n_tasks
        groups: list[list[str]] = []
        cursor = 0
        for group_index in range(n_tasks):
            groups_left = n_tasks - group_index - 1
            take = 1
            acc = count_tokens(units[cursor])
            while (
                cursor + take < len(units)
                and (len(units) - (cursor + take)) > groups_left
                and acc < quota
            ):
                acc += count_tokens(units[cursor + take])
                take += 1
            groups.append(units[cursor : cursor + take])
            cursor += take
        if cursor < len(units):  # sweep up any remainder
            groups[-1].extend(units[cursor:])
        return [" ".join(group) for group in groups]

    # Fewer natural units than requested tasks: slice the prompt by tokens.
    chunks = split_into_token_chunks(prompt.strip(), n_tasks)
    return [
        chunk.strip() or f"Part {i + 1} of {n_tasks} of the request."
        for i, chunk in enumerate(chunks)
    ]


def plan(
    prompt: str,
    backend: Any | None = None,
    *,
    n_tasks: int | None = None,
    contract: Contract | None = None,
    force_sequential: bool | None = None,
) -> Plan:
    """Build the micro-task DAG for ``prompt``.

    Two dependency topologies are produced, chosen by whether the prompt
    contains sequential-dependency markers:

    * **Chain** (sequential prompts): ``t0 -> t1 -> ... -> t{N-1}``. One task
      per level, so the DAG admits no parallelism at all -- which is exactly
      the honest answer for a prompt whose step ``i`` needs step ``i-1``.
    * **Fan-in** (parallel prompts): ``t0 .. t{N-2}`` are mutually independent
      and sit on level 0; the final task integrates them and sits on level 1.

    Args:
        prompt: The raw user prompt.
        backend: Optional backend (forwarded to :func:`global_contract`).
        n_tasks: Number of micro-tasks. Defaults to :func:`suggest_n_tasks`.
        contract: Reuse an already-computed contract.
        force_sequential: Override the sequential/parallel detection.

    Returns:
        A validated :class:`~swarmbly_v0.schema.Plan`.
    """
    from .router import extract_features  # local import avoids a cycle

    count = n_tasks if n_tasks is not None else suggest_n_tasks(prompt)
    count = max(1, int(count))
    gamma = contract or global_contract(prompt, backend)

    if force_sequential is None:
        features = extract_features(prompt)
        sequential = features["sequential_cues"] >= 0.45 or features["continuity_cues"] >= 0.55
    else:
        sequential = bool(force_sequential)

    segments = _segment(prompt, count)
    canonical = list(gamma.canonical_entities)

    tasks: list[Task] = []
    for i, segment in enumerate(segments):
        task_id = f"t{i}"
        local_entities = extract_entities(segment, min_mentions=1)[:3]
        expected = [e for e in canonical if e.lower() in segment.lower()] or local_entities
        if not expected and canonical:
            expected = [canonical[i % len(canonical)]]

        if sequential:
            deps = (f"t{i - 1}",) if i > 0 else ()
            kind = "step"
        elif count > 1 and i == count - 1:
            deps = tuple(f"t{j}" for j in range(count - 1))
            kind = "integration"
        else:
            deps = ()
            kind = "section"

        # The integration node's extra directive is kept deliberately short:
        # it is mandatory (untrimmable) packet content, so every token of it is
        # paid N-independently and pushes up the reachable rho floor.
        instruction = f"{segment} Close the answer; do not repeat earlier parts." \
            if kind == "integration" else segment

        tasks.append(
            Task(
                task_id=task_id,
                instruction=instruction,
                depends_on=deps,
                expected_entities=tuple(expected[:3]),
                kind=kind,
            )
        )

    return Plan(prompt=prompt, tasks=tasks, sequential=sequential)


def summarize_fragment(text: str, max_tokens: int = 40) -> str:
    """Compress a produced fragment into a predecessor summary.

    This is the *other* knob on ``rho``: the summary length is what a
    successor packet pays to know what its predecessors already said. The
    implementation is extractive (lead sentence plus the entity list), which
    keeps the harness deterministic and backend-independent.
    """
    sentences = split_sentences(text)
    if not sentences:
        return ""
    lead = sentences[0]
    entities = extract_entities(text, min_mentions=1)[:4]
    tail = f" Entities covered: {', '.join(entities)}." if entities else ""
    return truncate_tokens(f"{lead}{tail}", max_tokens).strip()
