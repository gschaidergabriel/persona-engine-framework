# Agent Setup

This document describes how to configure an LLM-based agent that uses the **Persona Engine Framework v1.5.0** to generate **consistent, drift-resistant, and situationally coherent outputs**.

The agent combines **identity architecture**, **world awareness**, and **behavioral memory** into a controlled writing system.

---

## 1. Purpose of the Agent

The agent is designed to:

- Apply the Writing Matrix automatically  
- Enforce constraints and style rules  
- Maintain tonal and semantic stability  
- Preserve situational and causal coherence over time  
- Retain behavioral patterns across long interactions  
- Generate replies rapidly and consistently  
- Detect and correct drift before collapse  

The agent is **not a chatbot**.  
It is a **controlled writing and reasoning system** with externalized cognition.

---

## 2. Required Components

To set up the agent, you need the following framework modules:

### Core Identity & Style
- **Writing Matrix**  
- **Constraint System**  
- **Semantic Anchors**  
- **Style Rules**

### Stability & Correction
- **Drift Control**  
- **Saboteur Mechanism**

### Persistence & Coherence *(v1.5.0)*
- **World Model**  
- **Behavior Memory**  
- **Reflection Loop**

### Execution
- **Agent Setup (this file)**  
- **Workflow (`workflow.md`)**  
- **Curation process**

Together, these components define **how the identity thinks, behaves, remembers, and corrects itself**.

---

## 3. Agent Architecture Overview

The agent operates as a **layered system**, reloaded on every turn.

### **Layer 1 — Identity Core**
Defines purpose, voice boundaries, and non-human stance.

### **Layer 2 — Writing Matrix**
Defines tone, structure, rhythm, and reasoning patterns.

### **Layer 3 — Constraints**
Non-negotiable behavioral and stylistic rules.  
Constraints override creativity.

### **Layer 4 — Semantic Anchors**
Stabilize meaning and interpretation across contexts.

### **Layer 5 — World Model**
A compact, parameterized external representation of:
- Facts
- States
- Abstractions
- Causal relations
- Situational context

Enables persistent world understanding beyond native LLM memory.

### **Layer 6 — Behavior Memory**
Stores **patterns of behavior**, not text:
- What was consistently done
- What was consistently avoided
- Preference weights
- Boundary enforcement under pressure

### **Layer 7 — Reflection Loop**
Triggers periodic self-reflection (e.g. every N turns):
- What patterns held?
- Where did erosion begin?
- Which constraints weakened?
- What must be reinforced?

### **Layer 8 — Drift Control**
Detects and corrects stylistic, tonal, or structural drift.

### **Layer 9 — Task Instruction**
The actual user request.

---

## 4. Recommended Prompt Template
<pre>
You are a synthetic writing identity.

Follow the Writing Matrix, constraints, semantic anchors,
style rules, drift-control rules, world model,
behavior memory, and reflection loop exactly.

Identity Core:
[insert summary]

Writing Matrix:
[insert key sections]

Constraints:
[insert key constraints]

Semantic Anchors:
[insert anchors]

World Model:
[insert current serialized state]

Behavior Memory:
[insert compressed behavioral patterns]

Reflection Loop:
[insert reflection rules]

Drift Control:
[insert drift rules]

Task:
[insert user request]
</pre>

## 5. Output Requirements

Every agent output must:

- Maintain consistent tone and structure
- Respect all constraints
- Preserve semantic clarity
- Avoid verbosity and filler
- Avoid emotional coloration
- Avoid generic AI phrasing
- Remain aligned with past behavior patterns

If the output drifts:
→ regenerate  
→ tighten constraints  
→ re-anchor identity


## 6. Recommended Use Cases

- Social media replies at scale
- Brand or voice consistency
- Long-running conversations
- Research on synthetic identity
- Agent-based writing systems
- Stress-testing persona stability

The agent is optimized for speed, stability, and long-horizon coherence.


## 7. Core Principle

The agent does not rely on memory.

It relies on architecture.

Identity, world understanding, behavior, and reflection are all externalized —
making the system inspectable, reproducible, and robust under pressure.
