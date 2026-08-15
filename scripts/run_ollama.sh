#!/usr/bin/env bash
#
# Swarmbly V0 + V3c against a local Ollama, with three model families.
#
#   ./scripts/run_ollama.sh smoke     ~5 min    does the wiring hold?
#   ./scripts/run_ollama.sh v0        ~2-4 h    the coherence-tax curve (H1)
#   ./scripts/run_ollama.sh v3c       ~2-3 h    agreement vs judged quality (V3c)
#   ./scripts/run_ollama.sh all       ~5-7 h    both, sequentially
#
# Everything is written under results/<tier>-<timestamp>/. Nothing is deleted.
#
# Why three *families* and not three sizes: agreement between replicas is only
# evidence to the extent the replicas could have disagreed. Models sharing
# training data share errors and will agree confidently on the same mistake, so
# a k=3 run drawn from one family produces a high agreement score that means
# nothing at all. The script refuses to proceed if fewer than three distinct
# families are present.

set -euo pipefail

TIER="${1:-smoke}"
HOST="${OLLAMA_HOST:-http://localhost:11434}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

# --- the three families -----------------------------------------------------
# Override with SWARMBLY_MODELS="fam:model,fam:model,fam:model" if you prefer
# different ones. Keep them small: three models resident at once on a laptop.
MODELS_DEFAULT="llama:llama3.2:3b,qwen:qwen2.5:3b,gemma:gemma2:2b"
MODELS="${SWARMBLY_MODELS:-$MODELS_DEFAULT}"
EMBED_MODEL="${SWARMBLY_EMBED_MODEL:-nomic-embed-text}"
PRIMARY="$(echo "$MODELS" | cut -d, -f1 | cut -d: -f2-)"

bold() { printf '\033[1m%s\033[0m\n' "$*"; }
warn() { printf '\033[33m%s\033[0m\n' "$*"; }
die()  { printf '\033[31mERROR: %s\033[0m\n' "$*" >&2; exit 1; }

# --------------------------------------------------------------------------
# Preflight. Every check here is one that would otherwise fail three hours in.
# --------------------------------------------------------------------------
bold "== Preflight =="

command -v ollama >/dev/null 2>&1 || die "ollama is not on PATH. https://ollama.com/download"

if ! curl -sS -m 5 "$HOST/api/tags" >/dev/null 2>&1; then
  warn "Ollama is not answering on $HOST — starting it in the background."
  (ollama serve >/tmp/ollama-serve.log 2>&1 &)
  for _ in $(seq 1 30); do
    sleep 1
    curl -sS -m 2 "$HOST/api/tags" >/dev/null 2>&1 && break
  done
  curl -sS -m 5 "$HOST/api/tags" >/dev/null 2>&1 \
    || die "could not reach $HOST after 30s. See /tmp/ollama-serve.log"
fi
echo "  ollama:       reachable at $HOST"

# distinct families
NFAM=$(echo "$MODELS" | tr ',' '\n' | cut -d: -f1 | sort -u | wc -l | tr -d ' ')
[ "$NFAM" -ge 3 ] || die "only $NFAM distinct families in SWARMBLY_MODELS. \
k>1 across one family measures that family's sampling variance, not the \
disagreement between independent estimators — which is the whole point of V3c."
echo "  families:     $NFAM distinct"

# pull what is missing
HAVE="$(ollama list 2>/dev/null | tail -n +2 | awk '{print $1}')"
for entry in $(echo "$MODELS" | tr ',' ' '); do
  model="${entry#*:}"
  if ! echo "$HAVE" | grep -qx "$model"; then
    bold "  pulling $model (first run only)"
    ollama pull "$model" || die "failed to pull $model"
  else
    echo "  present:      $model"
  fi
done
if ! echo "$HAVE" | grep -q "^${EMBED_MODEL}"; then
  bold "  pulling $EMBED_MODEL (embeddings)"
  ollama pull "$EMBED_MODEL" || warn "could not pull $EMBED_MODEL — tau will be calibrated on hashed vectors and will mean nothing"
else
  echo "  present:      $EMBED_MODEL"
fi

# python side
python3 -c "import swarmbly_v0" 2>/dev/null || {
  bold "  installing swarmbly_v0 in editable mode"
  python3 -m pip install -e . --quiet || die "pip install -e . failed"
}
python3 -c "import swarmbly_v0; print('  swarmbly_v0:  ', swarmbly_v0.__version__)"

export OPENAI_BASE_URL="$HOST/v1"
export OPENAI_API_KEY="ollama"
export SWARMBLY_MODEL="$PRIMARY"
export SWARMBLY_EMBED_MODEL="$EMBED_MODEL"
export SWARMBLY_REPLICA_MODELS="$MODELS"

# end-to-end smoke of the actual transport, before committing hours to it
bold "  round-trip test"
python3 - <<'PY' || die "the endpoint is reachable but the round trip failed"
from swarmbly_v0 import get_backend, get_embedder
b = get_backend("openai")
out = b.generate("Reply with exactly the word: ready", max_tokens=8)
print(f"  generate:     {out[:60]!r}  (transport: {b.transport})")
e = get_embedder("api")
v = e.embed(["alpha", "beta"])
print(f"  embeddings:   shape {v.shape}  available={e.available}")
if not e.available:
    print("  WARNING: embeddings degraded to hashing; tau_sem will be meaningless.")
PY

STAMP="$(date +%Y%m%d-%H%M%S)"

run_v0() {
  local out="results/v0-$STAMP"
  bold ""
  bold "== V0 — the coherence tax as a function of rho (hypothesis H1) =="
  echo "  This is the make-or-break measurement: how much quality is lost to"
  echo "  fragmentation and reassembly, and whether any rho gets it under 5%."
  echo "  Output: $out"
  mkdir -p "$out"
  python3 -m swarmbly_v0 run \
    --backend openai --embedder api \
    --rho 1.0,1.25,1.5,2.0 --n 2,4,8 --k 1 \
    --candidates 2 --seed 0 \
    --out "$out" 2>&1 | tee "$out/run.log" || true
  echo "  -> $out/report.html"
}

run_v3c() {
  local out="results/v3c-$STAMP"
  bold ""
  bold "== V3c — does agreement predict quality? =="
  echo "  k complete replicas per micro-task, one per family, aligned and scored."
  echo "  The number that matters is the correlation between the per-unit"
  echo "  agreement score and judged acceptability. If it is flat, the confidence"
  echo "  map is decoration and the paper must say so."
  echo "  Output: $out"
  mkdir -p "$out"
  python3 -m swarmbly_v0 run \
    --backend openai --embedder api \
    --rho 1.5 --n 4 --k 1,3,5 \
    --candidates 2 --seed 0 \
    --out "$out" 2>&1 | tee "$out/run.log" || true
  echo "  -> $out/report.html"
}

case "$TIER" in
  smoke)
    out="results/smoke-$STAMP"
    bold ""
    bold "== Smoke — two prompts, minimal grid. Proves the wiring, measures nothing. =="
    mkdir -p "$out"
    python3 -m swarmbly_v0 run \
      --backend openai --embedder api \
      --rho 1.0,1.5 --n 2 --k 1,3 --max-prompts 2 \
      --out "$out" 2>&1 | tee "$out/run.log"
    bold ""
    bold "Smoke run finished. If the numbers above look sane, run:"
    echo "  ./scripts/run_ollama.sh all"
    ;;
  v0)  run_v0 ;;
  v3c) run_v3c ;;
  all) run_v0; run_v3c ;;
  *)   die "unknown tier '$TIER'. Use: smoke | v0 | v3c | all" ;;
esac

bold ""
bold "== Done =="
echo "Before quoting any number from these runs, check run_metadata.json for:"
echo "  harness_validation_only : must be false (it is true only for the mock backend)"
echo "  embeddings_degraded     : must be false, or tau_sem carries no meaning"
echo "  n_families_mean         : must be 3 in the k>1 rows, or agreement is not evidence"
