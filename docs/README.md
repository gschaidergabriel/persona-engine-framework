## Persona Engine Framework — Live Demo (v1.5.0)

This repository contains a transparent, architecture-level demo of the **Persona Engine Framework**.

It does **not** simulate AI behavior, fake responses, or proxy APIs.  
Instead, it demonstrates a precise claim:

**Persona is not a prompt.**  
**Persona is a constraint system — and a world model — that live outside the interaction loop.**

---

## What this demo is (and is not)

### What it shows

- How a stable synthetic writing identity can be defined as:
  - tonal constraints  
  - semantic anchors  
  - structural rules  
  - drift-correction mechanisms  
  - **a persistent external World Model**
- How the same user input produces qualitatively different behavior when the governing constraints change.
- Why long-horizon consistency cannot be achieved with prompts or short-term memory alone.
- How an explicit World Model enables:
  - situational continuity  
  - causal coherence  
  - resistance to contradiction  
  - similarity-based recall  
  - controlled evolution of understanding across turns  

### What it does not do

- No live API calls  
- No simulated chat responses  
- No automation claims  

This is intentional.

The demo is designed to be **honest**, **reproducible**, and **inspectable**.

---

## How the demo works

1. Select a persona (e.g. Philosopher, Scientist, Artist).
2. The system generates a **persona-anchored system prompt**.
3. The prompt includes:
   - the Writing Matrix  
   - constraints and drift control  
   - **a fully embedded World Model Module**
4. Copy the prompt.
5. Open ChatGPT and paste it as the system instruction.
6. Continue the conversation there.

This makes the control boundary explicit:

- **The framework governs behavior and memory structure.**
- **The model supplies capability.**

---

## The Writing Matrix

All personas are derived from the same underlying architecture: the **Writing Matrix**.

It defines:

- an Identity Core  
- Tonal Architecture  
- Semantic Anchors  
- Rhythm & Structure  
- a Constraint System  
- a built-in Saboteur for drift correction  
- explicit Drift Control  

Creativity is allowed —  
**but constraints override creativity.**

---

## The World Model (new in v1.5.0)

Since version **1.5.0**, the framework includes a **World Model Module**.

The World Model is:

- a compact, JSON-based external state
- maintained explicitly inside the chat
- reinjected on every turn
- authoritative over facts, relations, and abstract states

It enables:

- persistent situational awareness  
- coherent temporal reasoning  
- automatic conflict resolution  
- similarity-based recall via vector embeddings  
- stable reference frames across long conversations  

The World Model governs **cognition and recall**,  
while the Writing Matrix governs **style and behavior**.

Together, they form a complete identity architecture.

---

## Why this matters

Most “persona” systems collapse into:

- structured prompting  
- tone presets  
- or memory hacks  

Those approaches drift under pressure.

This framework treats identity as:

- externalized  
- inspectable  
- reusable  
- failure-aware  

The goal is not better replies.  
The goal is **stable behavior over time**.

---

## Who this is for

- Researchers exploring synthetic identity  
- Developers building agent-like systems  
- Writers and thinkers who care about voice consistency  
- Anyone interested in where prompting stops working  

---

## Running the demo

This is a **static HTML demo**.

- Open `index.html` in any modern browser  
- No build step  
- No dependencies  

---

## Author

**Gabriel Gschaider**

Interdisciplinary work on AI, philosophy, and ethics.  
Thinking before writing.  
Clarity over output.

---

## Notes

This demo is intentionally minimal.

If you want:

- automation  
- agents  
- orchestration  
- external memory backends  

Those belong **after identity and world modeling are solved — not before**.
