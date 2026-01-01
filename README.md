# persona-engine-framework v1.5.0

*A framework for building stable, long-horizon synthetic writing identities using large language models.*

---

## Target Audience

This repository is for:

- **System thinkers, researchers, and advanced practitioners** working with LLMs  
- **Developers and architects** building long-running AI agents or assistants  
- **Writers, strategists, and creators** who require persistent tone, reasoning, and stance across hundreds of outputs  
- **Users encountering drift, collapse, or instability** in extended AI collaboration  

It is **not** intended for prompt collections, casual chatbot customization, or short-lived, one-off generations.

If you care about **identity stability, long-horizon coherence, and system-level correctness**, this framework is for you.

---

## Overview

**persona-engine-framework** is a modular architecture for building **stable synthetic writing identities** on top of large language models.

Version **1.5.0** extends the original framework beyond stylistic control into **long-run behavioral and cognitive stability**, introducing:
   
- A Reflection Loop  
- Cognitive risk detection for safe long-term collaboration  

The result is a system that remains coherent, bounded, and predictable over **hundreds of turns**, even under pressure and token limits.

---

## 🧠 What is this?

This is **not a prompt**.

This is a **system architecture** for creating a synthetic writing identity that behaves like a consistent persona across long interaction horizons — even in cloud-based LLMs such as **ChatGPT, Claude, or Grok**.

It enables:

- Tonal consistency  
- Semantic stability  
- Drift detection and correction  
- Persistent situational awareness  
- Behavioral continuity under pressure  
- Periodic self-reflection for consolidation  
- Long-run robustness under token pressure  
- Ethical and stylistic boundary enforcement  
- Presence without loss of voice  

---

## 🔍 Why does it exist?

Most AI-generated text **drifts over time**:

- Tone shifts  
- Reasoning weakens  
- Outputs become generic  
- Context collapses  
- Long sessions destabilize both model and user  

This framework solves that by **externalizing identity and cognition as architecture**, rather than compressing everything into a single system prompt.

---

## ✨ What’s new in v1.5.0

Version 1.5.0 introduces **structural modules** that allow identity to persist under real-world constraints:

### Reflection Loop
A periodic self-reflection module for behavioral consolidation.

Enables:
- Forced reflection every N turns  
- Detection of slow erosion  
- Reinforcement of stable patterns  
- Tightening of weak boundaries  

Transforms time into signal and prevents silent drift.

---

### Cognitive Risk Detection (within v1.5.0 architecture)
A non-diagnostic cognitive ergonomics layer for long-running interaction.

Monitors:
- Sustained cognitive overload  
- Recursive acceleration without consolidation  
- Loss of natural stopping signals  
- Control anxiety and agency misattribution  

Enables:
- State-based intervention (not alarmism)  
- Automatic de-escalation of system behavior  
- Protection against destabilizing feedback loops  

---

## ⚙️ How does it work?

### Core Components

**Writing Matrix**  
Defines tone, structure, rhythm, reasoning patterns, and the identity core.

**Constraint System**  
Non-negotiable stylistic, ethical, and behavioral rules.  
Constraints override creativity.

**Semantic Anchors**  
Conceptual pillars that stabilize meaning and interpretation.

**Saboteur Mechanism**  
Built-in stress tests to prevent over-optimization and generic AI collapse.

**Drift Control**  
Detection and correction mechanisms for long-term identity stability.

**Reflection Loop**  
Periodic consolidation and correction.

**Invariant Stability & Cognitive Risk Detection**  
Ensure long-run robustness under token pressure and human cognitive limits.

---

## 🚀 Quick Start — Primary Use: Cloud LLMs

The framework is designed to be used **directly inside web-based LLMs**  
by uploading the PSF files (`.md` documents).

### Steps

1. Download or clone the repository  
2. Upload the key framework files to your LLM chat:
   - `/framework/writing-matrix.md`  
   - `/framework/constraints.md`  
   - `/framework/semantic-anchors.md`  
   - `/framework/drift-control.md`   
   - `/framework/reflection-loop.md`
   - `/framework/style-rules.md`
   - `/framework/cognitive-risk-detection-module.md` 
3. Upload `/agent/agent-setup.md`  
4. Activate the identity using `agent-setup.md`  
5. Provide inputs (tweets, threads, prompts, questions)  
6. Generate outputs  
7. Check for drift, curate, and publish  

This workflow has been used to generate **hundreds of consistent outputs** inside ChatGPT projects with minimal editing.

For the full step-by-step guide, see:  
`/agent/usage.md`

---

## 🛠️ Alternative: Local Development & Testing

```bash
git clone https://github.com/gschaidergabriel/persona-engine-framework.git
cd persona-engine-framework
