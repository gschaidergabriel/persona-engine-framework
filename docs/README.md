# Persona Engine Framework — Live Demo

This repository contains a **transparent, architecture-level demo** of the *Persona Engine Framework*.

It does **not** simulate AI behavior, fake responses, or proxy APIs.  
Instead, it demonstrates a different claim:

> **Persona is not a prompt.  
> Persona is a constraint system that lives outside the interaction loop.**

---

## What this demo is (and is not)

### What it shows
- How a **stable synthetic writing identity** can be defined as:
  - tonal constraints
  - semantic anchors
  - structural rules
  - drift-correction mechanisms
- How the same user input produces **qualitatively different behavior**
  when the governing constraints change.
- Why long-horizon consistency cannot be achieved with prompts alone.

### What it does *not* do
- No live API calls
- No simulated chat responses
- No automation claims

This is intentional.  
The demo is designed to be **honest, reproducible, and inspectable**.

---

## How the demo works

1. Select a persona (e.g. Philosopher, Scientist, Artist).
2. The system generates a **persona-anchored system prompt**.
3. Copy the prompt.
4. Open ChatGPT and paste it as the system instruction.
5. Continue the conversation there.

This makes the control boundary explicit:
- The framework governs *behavior*.
- The model supplies *capability*.

---

## The Writing Matrix

All personas are derived from the same underlying architecture: the **Writing Matrix**.

It defines:
- an **Identity Core**
- **Tonal Architecture**
- **Semantic Anchors**
- **Rhythm & Structure**
- a **Constraint System**
- a built-in **Saboteur** for drift correction
- explicit **Drift Control**

Creativity is allowed — but **constraints override creativity**.

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
- and failure-aware

The goal is not better replies.
The goal is **stable behavior over time**.

---

## Who this is for

- Researchers exploring **synthetic identity**
- Developers building **agent-like systems**
- Writers and thinkers who care about **voice consistency**
- Anyone interested in where prompting stops working

---

## Running the demo

This is a static HTML demo.

Open `index.html` in any modern browser.

No build step. No dependencies.


---

## Author

**Gabriel Gschaider**

Interdisciplinary work on AI, philosophy, and ethics.  
Thinking before writing. Clarity over output.

---

## Notes

This demo is intentionally minimal.

If you want:
- automation
- agents
- memory
- orchestration

Those belong *after* identity is solved — not before.


