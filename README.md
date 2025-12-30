# persona-engine-framework v1.5.0

A framework for building **stable, synthetic writing identities** using large language models.

Version **1.5.0** extends the original architecture with a **World Model module**, **Behavior Memory**, and a **Reflection Loop**, enabling persistent situational awareness and long-horizon coherence in addition to stylistic stability.

---

## 🧠 What is this?

This is **not a prompt**.

This is a **modular architecture** for creating a synthetic writing identity that behaves like a consistent persona across hundreds of AI-generated replies — even in cloud-based LLMs such as **ChatGPT, Claude, or Grok**.

It enables:

- Tonal consistency  
- Semantic stability  
- Drift prevention and detection  
- Persistent situational awareness  
- Behavioral continuity under pressure  
- Periodic self-reflection for consolidation  
- Rapid, scalable reply generation  
- Ethical and stylistic boundaries  
- Presence without loss of voice  

---

## 🔍 Why does it exist?

Most AI-generated text **drifts over time**:
tone shifts, reasoning weakens, outputs become generic, and context collapses.

This framework solves that by **externalizing identity and cognition as architecture**,  
instead of compressing everything into a single system prompt.

**What’s new in v1.5.0:**

- A **World Model layer** that maintains a compact, parameterized representation of the world as experienced through interaction.
- A **Behavior Memory layer** that tracks *how* the identity behaves over time, not just *what* it says.
- A **Reflection Loop** that forces periodic self-reflection to detect slow erosion and reinforce boundaries.

Result:  
A **stable, predictable, high-quality synthetic voice** with situational and behavioral continuity — at scale.

---

## ⚙️ How does it work?

### Core Components

- **Writing Matrix**  
  Defines tone, structure, rhythm, reasoning patterns, and the identity core.

- **Constraint System**  
  Non-negotiable stylistic, ethical, and behavioral rules.  
  Constraints override creativity.

- **Semantic Anchors**  
  Core concepts that stabilize meaning and interpretation across replies.

- **Saboteur Mechanism**  
  Built-in stress tests to prevent over-optimization and generic AI collapse.

- **Drift Control**  
  Detection and correction mechanisms for long-term identity stability.

- **World Model (added in v1.5.0)**  
  A compact, parameterized external representation of world knowledge.  
  Enables:
  - Persistent situational awareness  
  - Temporal and causal consistency  
  - Emergent understanding  
  - Conflict detection and resolution  
  - Reference to past interactions without relying on LLM memory

- **Behavior Memory (added in v1.5.0)**  
  A lightweight memory of behavioral patterns rather than facts.  
  Tracks:
  - Boundary adherence under pressure  
  - Repeated response patterns  
  - Preference weights instead of fixed claims  
  - Behavioral trajectories across turns

- **Reflection Loop (added in v1.5.0)**  
  A periodic self-reflection module for behavioral consolidation.  
  Enables:
  - Forced reflection every N turns  
  - Detection of slow erosion  
  - Reinforcement of stable patterns  
  - Tightening of weak boundaries  
  Transforms time into signal and prevents silent drift.

- **Agent Workflow**  
  A structured process for activating the identity and generating outputs.

- **Diagnostics**  
  Optional local tooling for automated drift and collapse testing.

---

## 🚀 Quick Start – Primary Use: Cloud LLMs (ChatGPT, Claude, etc.)

The framework is designed to be used **directly inside web-based LLMs**  
by uploading the PSF files (`.md` documents).

### Steps

1. Download or clone the repository.
2. Upload the key PSF files to your LLM chat (e.g., ChatGPT):
   - `/framework/writing-matrix.md`
   - `/framework/constraints.md`
   - `/framework/semantic-anchors.md`
   - `/framework/drift-control.md`
   - `/framework/world-model.md`
   - `/framework/behavior-memory.md`
   - `/framework/reflection-loop.md`
   - `/agent/agent-setup.md`
3. Activate the identity using the instructions in `agent-setup.md`.
4. Provide inputs (tweets, questions, threads, prompts).
5. Generate replies.
6. Check for drift, curate the best outputs (e.g., via screenshot), and publish.

**Real example:**  
This exact workflow has been used in ChatGPT projects to generate **hundreds of consistent replies** with minimal editing.

For the full step-by-step guide (including the complete ChatGPT workflow), see:  
`/agent/usage.md`

---

## 🛠️ Alternative: Local Development & Testing

For experimentation and diagnostics:

bash
>git clone https://github.com/gschaidergabriel/persona-engine-framework.git
>cd persona-engine-framework

Customize /framework/writing-matrix.md, constraints, and anchors.

Activate the agent via /agent/agent-setup.md.

Generate replies manually or evaluate drift with:
/diagnostics/identity_drift/drift_evaluator.py
(requires Ollama + a local model such as Mistral).

---

## 📌 Core Insight

Identity is not a static description.

It is a **pattern of behavior under constraint**,  
maintained through **external architecture**, not internal memory.

The framework defines:

- how the identity is built  
- how it reasons  
- how it understands the world  
- how it remembers its own behavior  
- how it reflects to prevent slow erosion  
- how it detects and corrects failure modes  

The agent defines how the identity acts.

Together, they form a **complete synthetic writing and reasoning engine**.
