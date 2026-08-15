"""A five-hour sweep must not die on one dropped socket.

The first attempt to exercise the full v0 grid aborted because the endpoint
blinked once. On a laptop swapping three models in and out of memory that is an
ordinary event, and the cost of not handling it is the whole run.

Retries are bounded and counted. An unlimited retry would hide a genuinely dead
endpoint; an uncounted one would let a run held together by retries look
identical to a clean one in the metadata.
"""

from __future__ import annotations

import pytest

from swarmbly_v0.backends import BackendUnavailable, OpenAICompatBackend


class _Flaky(OpenAICompatBackend):
    """Fails `fail_times` times, then succeeds."""

    def __init__(self, fail_times: int, **kw):
        super().__init__(retry_backoff_s=0.0, **kw)
        object.__setattr__(self, "_left", fail_times)
        object.__setattr__(self, "calls", 0)

    def _post_once(self, path, payload):
        self.calls += 1
        if self._left > 0:
            self._left -= 1
            raise BackendUnavailable("connection refused")
        return {"choices": [{"message": {"content": "ok"}}]}


def test_a_single_blip_is_survived_and_counted():
    b = _Flaky(1)
    assert b._post("/chat/completions", {})["choices"][0]["message"]["content"] == "ok"
    assert b.calls == 2
    assert b.retries == 1
    assert b.retry_events and "connection refused" in b.retry_events[0]


def test_a_clean_call_costs_no_retries():
    b = _Flaky(0)
    b._post("/chat/completions", {})
    assert b.calls == 1 and b.retries == 0 and b.retry_events == []


def test_a_dead_endpoint_still_fails_rather_than_looping():
    b = _Flaky(99)
    with pytest.raises(BackendUnavailable, match="gave up after 3 attempts"):
        b._post("/chat/completions", {})
    assert b.calls == 3, "bounded: first attempt plus max_retries"


def test_retry_can_be_switched_off():
    b = _Flaky(1, max_retries=0)
    with pytest.raises(BackendUnavailable):
        b._post("/chat/completions", {})
    assert b.calls == 1


def test_the_run_metadata_reports_the_retries():
    from swarmbly_v0.experiment import SweepConfig, load_prompts, run_sweep
    from swarmbly_v0.backends import HashEmbedder

    class _OneBlip(OpenAICompatBackend):
        def __init__(self, **kw):
            super().__init__(retry_backoff_s=0.0, **kw)
            object.__setattr__(self, "_blipped", False)

        def _post_once(self, path, payload):
            if not self._blipped:
                object.__setattr__(self, "_blipped", True)
                raise BackendUnavailable("connection refused")
            if path == "/embeddings":
                n = len(payload["input"])
                return {"data": [{"embedding": [1.0, 0.0, 0.0]} for _ in range(n)]}
            return {"choices": [{"message": {"content": "Alpha beta. Gamma delta."}}]}

    engine = _OneBlip()
    _, meta = run_sweep(
        load_prompts()[:2],
        SweepConfig(rhos=(1.0,), ns=(2,), ks=(1,), backend_name="openai"),
        engine,
        HashEmbedder(),
    )
    assert meta["transport_retries"] >= 1
