# Identity Drift Diagnostics

This folder contains **diagnostic tooling** for observing **identity drift, erosion, and collapse** in large language models over extended iteration chains.

The tools here are designed to evaluate **synthetic writing identities** defined by external constraints (e.g. a Writing Matrix), not to optimize prompts or model performance.

---

## Scope

- Long-horizon identity stability testing
- Structural and tonal drift detection
- Failure-mode visibility over time

**Not a benchmark.  
Not an alignment claim.  
Not a performance comparison.**

---

## What is measured

- Gradual erosion of identity constraints
- Sudden collapse into generic or unstable output
- Recurrent drift causes (e.g. tone escalation, verbosity drift, generic cadence)

The signal lies in the **trajectory**, not in absolute scores.

---

## Contents

- `drift_evaluator.py`  
  Iterative self-regeneration diagnostic with:
  - soft vs. hard collapse detection  
  - drift-cause attribution  
  - ASCII compliance timeline (screenshot-friendly)

---

## Execution Notes

- Designed for **GPU-backed systems** or short diagnostic runs
- CPU-only systems may experience severe slowdowns or timeouts
- No automatic model pulling is performed
- Results are heuristic and context-dependent

---

## Status

Experimental diagnostic tooling.  
Intended for research, ev
