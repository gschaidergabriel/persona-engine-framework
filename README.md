# persona-engine-framework

**A framework for building stable, synthetic writing identities using LLMs.**

Includes a Writing Matrix, constraint system, drift-control mechanisms, saboteur mode, and an agent workflow for generating consistent, high-quality replies at scale.

---

## 🧠 What is this?

This is **not a prompt**.

This is a modular architecture for creating a synthetic writing identity that behaves like a consistent persona across hundreds of AI-generated replies — even in cloud-based LLMs like ChatGPT, Claude, or Grok.

It enables:

- Tonal consistency
- Semantic stability
- Drift prevention & detection
- Rapid, scalable reply generation
- Ethical and stylistic boundaries
- Presence without loss of voice

---

## 🔍 Why does it exist?

Most AI-generated text drifts over time: tone shifts, reasoning weakens, outputs become generic.

This framework solves that by **externalizing identity as architecture** (constraints, anchors, matrix) instead of cramming everything into prompts.

Result: Stable, predictable, high-quality synthetic voice — at scale.

---

## ⚙️ How does it work?

Core components:

- **Writing Matrix**: Defines tone, structure, rhythm, and reasoning patterns
- **Constraint System**: Non-negotiable rules (stylistic, ethical, behavioral)
- **Semantic Anchors**: Core concepts that stabilize meaning
- **Saboteur Mechanism**: Stress-tests to prevent over-optimization
- **Drift Control**: Mechanisms + tools to detect and prevent identity collapse
- **Agent Workflow**: Structured process for consistent generation
- **Diagnostics**: Optional local tool (`drift_evaluator.py`) for automated testing

---

## 🚀 Quick Start – Primary Use: Cloud LLMs (ChatGPT, Claude, etc.)

The framework is designed to be used directly in web-based LLMs by **uploading the PSF files** (.md documents).

1. Download or clone the repo
2. Upload the key PSF files to your LLM chat (e.g., ChatGPT):
   - `/framework/writing-matrix.md`
   - `/framework/constraints.md`
   - `/framework/semantic-anchors.md`
   - `/framework/drift-control.md`
   - `/agent/agent-setup.md`
   - And others as needed
3. Activate the identity using the instructions in `agent-setup.md`
4. Provide inputs (tweets, questions, threads) and generate replies
5. Check for drift, curate best outputs (e.g., via screenshot), and publish

**Real example**: This exact workflow has been used in ChatGPT projects to generate hundreds of consistent replies with minimal editing.

For the full step-by-step guide (including the complete ChatGPT workflow), see **[agent/usage.md](agent/usage.md)**.

---

## 🛠️ Alternative: Local Development & Testing

1. Clone the repo: `git clone https://github.com/gschaidergabriel/persona-engine-framework.git`
2. Read and customize `/framework/writing-matrix.md` and constraints
3. Set up your agent: Follow `/agent/agent-setup.md`
4. Generate replies manually or test drift locally with `/diagnostics/identity_drift/drift_evaluator.py` (requires Ollama + Mistral)
5. Curate via screenshot and post

---

## 📁 Key Files & Folders

- `/framework/` – Core architecture (matrix, constraints, anchors, etc.)
- `/agent/` – Setup, workflow, and **[usage.md](agent/usage.md)** (detailed guide)
- `/diagnostics/` – Local drift evaluation tool
- `/philosophy/` – Underlying principles
- `/examples/` – Sample outputs and curation

---

## 🔧 Related Repository

For advanced drift/collapse detection:  
[Identity-Collapse-Detection-Engine](https://github.com/gschaidergabriel/Identity-Collapse-Detection-Engine)

---

**The voice speaks for itself.**  
No commentary needed.

