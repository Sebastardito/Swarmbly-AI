# First measurements against real models — V0 and V3c

**Runs:** `results/v0-20260814-140941/` and `results/v3c-20260814-140941/` ·
**Backend:** local Ollama, three families (`llama3.2:3b`, `qwen2.5:3b`,
`gemma2:2b`), embeddings `nomic-embed-text` · **Corpus:** the 8-prompt smoke set,
one seed, temperature 0

> **Provenance, checked before anything below was read.** `harness_validation_only:
> false` and `embeddings_degraded: false` in both runs — real models, real
> embeddings, not the mock. `transport_retries: 0` — no connection was dropped
> and re-tried, so nothing here is a partial result stitched together.
> τ_sem = 0.51, calibrated on **72 labelled pairs** (F₀·₅ = 0.988, precision 1.00,
> recall 0.944).
>
> **Reproducibility.** These runs reproduce an earlier pair, cell for cell, at the
> same seed. The pipeline is deterministic at temperature 0, which is what makes
> a disagreement between two runs meaningful rather than expected.
>
> **Scale.** Eight prompts, one seed, 2–3B models. A signal to act on, not a
> benchmark to publish as a headline.

---

## 1. V0 — the coherence tax falls monotonically in ρ

BooookScore-like tax against the monolithic baseline, *k* = 1, 21 valid cells per ρ:

| ρ (target) | ρ (achieved) | Coherence tax | Absolute difference | Cells |
|---|---|---|---|---|
| 1.00 | 1.17 | **+24.1 %** | +0.1235 | 21 |
| 1.25 | 1.27 | **+20.4 %** | +0.0761 | 21 |
| 1.50 | 1.53 | **+16.1 %** | +0.0678 | 21 |
| 2.00 | 2.08 | **+13.7 %** | +0.0517 | 21 |

Both the ratio and the denominator-free absolute difference decrease with ρ.
This is what hypothesis H1 predicts: more shared context per fragment, less
quality lost to reassembly. It is the first evidence that the context budget is
the variable the design says it is.

### The go/no-go criterion is met

Six of 28 category × ρ cells fall below the 5 % threshold fixed before any data
existed:

| Category | ρ | Tax |
|---|---|---|
| creative_writing | 2.00 | **−9.0 %** |
| synthetic_data | 1.50 | **−6.2 %** |
| synthetic_data | 1.25 | **−5.1 %** |
| synthetic_data | 2.00 | **−0.3 %** |
| synthetic_data | 1.00 | **+1.3 %** |
| code_shared_state | 1.50 | **+3.2 %** |

Negative means fragmentation *improved* the answer on that instrument.
`synthetic_data` clears the threshold at every ρ tested. The criterion was
written as "at least one task category" because nobody expected all of them to
pass — and they do not.

### Two measurement failures, reported because they bound the table above

**The entity grid is unusable on this corpus.** Its monolithic baseline ranges
from 0.000 to 0.114 across all eight prompts, median 0.024 — every one below the
0.15 floor at which a ratio stops being a statistic. All **96 of 96** cells are
excluded and the harness reports the relative entity-grid tax as *not measured*
rather than as zero. An earlier version of this run, before the denominator was
checked, reported figures as extreme as **−180 %**.

**One prompt broke its baseline.** `rag_summarization_filings` produced a
monolithic answer of one sentence and six tokens — a generation failure, not a
coherence result. Its BooookScore baseline is 0.000 and its 12 cells are
excluded. This needs investigating before the next run: a prompt that cannot
produce a baseline cannot contribute a tax.

## 2. V3c — agreement does not predict quality here

Sweeping *k* ∈ {1, 3, 5} at ρ = 1.5, one replica per family:

| *k* | Coherence tax | Mean agreement | HIGH | LOW |
|---|---|---|---|---|
| 1 | +13.2 % | — | — | — |
| 3 | **+30.8 %** | 0.577 | 29.1 % | 42.3 % |
| 5 | **+33.3 %** | 0.728 | 58.3 % | 28.7 % |

Consensus costs roughly **17 to 20 points of quality** relative to *k* = 1. What
it buys was supposed to be the confidence map:

> **Pearson r = −0.030 over 597 semantic units.**

The bins are flat and non-monotone, and agreement does not order them: the
highest-scoring bin is 0.6–0.8, the *lowest*-agreement bin is second, and the
bin where the models agreed most scores below both.

| Agreement | Units | Judged acceptable |
|---|---|---|
| 0.0 – 0.2 | 40 | 97.5 % |
| 0.2 – 0.4 | 91 | 91.2 % |
| 0.4 – 0.6 | 80 | 91.3 % |
| 0.6 – 0.8 | 122 | 99.2 % |
| 0.8 – 1.0 | 264 | 91.3 % |

Section 11.4 of the whitepaper committed in advance: *"a flat or negative
correlation would invalidate the confidence map as a reliability signal, and that
outcome must be publishable."* It is published.

### The run is not the experiment the whitepaper specifies

**The judge accepted 93.3 % of units.** With that little variance in the
dependent variable a correlation cannot appear even if the underlying signal is
real. This measurement therefore **cannot distinguish**:

1. agreement between independent model families does not predict correctness; or
2. a peer-class judge does not discriminate quality finely enough to detect it.

Section 11.4 specifies V3c against **ground-truth datasets**. This run used the
judge — the weaker instrument the whitepaper already warns about. **The honest
statement is that the confidence map is unsupported, not refuted.**

That does not rescue the claim. An unsupported property cannot be advertised as
the architecture's most valuable one, and it no longer is: Section 1.3 was
rewritten, Section 8.4b carries the measured result, E16 is now disclosed
explicitly as a mechanism with no claimed reliability benefit, and L13 records
the whole thing as a limitation.

## 3. What changed in the paper

| Change | Where |
|---|---|
| Results reported in full, including the unfavourable one | new Section 11.3 |
| Abstract states both outcomes | Abstract |
| The confidence map demoted from "most valuable property" to "mechanism, benefit unmeasured" | Section 1.3, point 2 |
| The measured correlation and its weakness stated at the mechanism | Section 8.4b, point 2 |
| E16 disclosed as a mechanism with no reliability claim | Section 13 |
| **L13** — the confidence map has no demonstrated value | Section 12 |
| **L14** — the entity grid does not function on short answers | Section 12 |
| Metrics table gains a *measured* column | Section 11.5 |
| Conclusion revised: first measurement in, one contribution weakened | Section 14 |

## 4. What to run next, in priority order

1. **V3c against ground truth.** The single experiment that would settle whether
   the confidence map is worth its 17–20 point cost. Everything else about E16 is
   speculation until this exists.
2. **Fix `rag_summarization_filings`.** A prompt that yields a six-token baseline
   is a bug in the corpus or in generation, not a finding.
3. **Replace or repair the second coherence instrument.** One working mechanical
   proxy is thinner evidence than this design deserves.
4. **Longer outputs, more prompts, more seeds.** Eight prompts and one seed
   bound how much any of the above can mean.

## 5. Reproduce

```bash
./scripts/run_ollama.sh v0     # results/v0-<stamp>/
./scripts/run_ollama.sh v3c    # results/v3c-<stamp>/
```

Runs from commit `846aeea` onwards record the denominator alongside every ratio,
exclude and count unstable cells, take the headline from *k* = 1, report an
unmeasured point as absent rather than as zero, and survive a dropped connection.
