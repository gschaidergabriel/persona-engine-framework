# persona-engine-framework v1.5.0

A framework for building **stable, synthetic writing identities** using large language models.

This release extends the original architecture with a **World Model module**, enabling persistent situational awareness and long-horizon coherence in addition to stylistic stability.

---

## 🧠 What is this?

This is **not a prompt**.

This is a **modular architecture** for creating a synthetic writing identity that behaves like a consistent persona across hundreds of AI-generated replies — even in cloud-based LLMs such as **ChatGPT, Claude, or Grok**.

It enables:

- Tonal consistency  
- Semantic stability  
- Drift prevention and detection  
- Persistent situational awareness  
- Rapid, scalable reply generation  
- Ethical and stylistic boundaries  
- Presence without loss of voice  

---

## 🔍 Why does it exist?

Most AI-generated text **drifts over time**:
tone shifts, reasoning weakens, outputs become generic, and context collapses.

This framework solves that by **externalizing identity and cognition as architecture**  
instead of compressing everything into a single system prompt.

**v1.5.0 adds a World Model layer**, allowing the identity to maintain a compact,
parameterized representation of the world it experiences through text, images, and interaction history.

Result:  
A **stable, predictable, high-quality synthetic voice** with situational continuity — at scale.

---

## ⚙️ How does it work?

### Core Components

- **Writing Matrix**  
  Defines tone, structure, rhythm, reasoning patterns, and identity core.

- **Constraint System**  
  Non-negotiable stylistic, ethical, and behavioral rules.  
  Constraints override creativity.

- **Semantic Anchors**  
  Core concepts that stabilize meaning and interpretation across replies.

- **Saboteur Mechanism**  
  Built-in stress tests to prevent over-optimization and generic AI collapse.

- **Drift Control**  
  Detection and correction mechanisms for long-term identity stability.

- **World Model (new in v1.5.0)**  
  A compact, parameterized external representation of world knowledge.  
  Enables:
  - Persistent situational awareness  
  - Causal inference  
  - Emergent understanding  
  - Conflict detection and resolution  
  - Reference to past interactions without relying on LLM memory

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

```bash
git clone https://github.com/gschaidergabriel/persona-engine-framework.git
