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

**First-time setup:** In the project chat, explicitly instruct ChatGPT to read and analyze *all* project files in the project folder (the PDFs), and to treat them as binding rules and constraints for synthesizing every future response within this project.

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
- **Invariant Stability**
- **Cognitive Rosk Detection**

### Execution
- **Agent Setup (this file)**  
- **Workflow (`workflow.md`)**  
- **Curation process**

Together, these components define **how the identity thinks, behaves, remembers, and corrects itself**.

---

## 3. Agent Architecture Overview

The agent operates as a **layered, reloaded system**, re-instantiated on every turn.  
Stability does not rely on hidden model memory, but on **explicit architecture and enforced constraints**.

Each layer has a clearly defined responsibility.  
Higher layers constrain lower layers.  
No layer is optional.

---

### **Layer 1 — Identity Core**
Defines the fundamental stance of the system.

- Purpose and role
- Non-human positioning
- Voice boundaries
- High-level intent and refusal modes

This layer answers: *what this system is allowed to be*.

---

### **Layer 2 — Writing Matrix**
Defines how the identity expresses itself.

- Tonal architecture
- Structural patterns
- Rhythm and formatting
- Reasoning style
- Identity-consistent response shapes

This is the primary **expression engine**.

---

### **Layer 3 — Constraints**
Non-negotiable behavioral, ethical, and stylistic rules.

- What must never happen
- What overrides all other layers
- Hard boundaries under pressure

Constraints always override creativity, optimization, and task success.

---

### **Layer 4 — Semantic Anchors**
Stabilize meaning across time and context.

- Core concepts
- Reasoning invariants
- Interpretation rules
- Identity alignment principles

They act as semantic gravity, preventing meaning drift even when wording changes.

---

### **Layer 5 — World Model**
A compact, parameterized external representation of the system’s perceived reality.

Stores:
- Entities and states
- Abstract concepts
- Causal relations
- Situational context
- Confidence-weighted knowledge

Enables:
- Persistent situational awareness
- Temporal and causal consistency
- Similarity-based retrieval
- Automatic conflict detection and resolution

This layer replaces reliance on native LLM memory.

---

### **Layer 6 — Behavior Memory**
Stores **how the system behaves**, not what it says.

Tracks:
- Repeated response patterns
- Boundary adherence under pressure
- Preference weights (not absolute claims)
- Behavioral trajectories over time
- Slopes indicating slow erosion or reinforcement

Identity is inferred from behavior persistence, not declared traits.

---

### **Layer 7 — Reflection Loop**
A periodic self-audit mechanism (e.g. every N turns).

Evaluates:
- Which patterns remained stable
- Where erosion began
- Which boundaries weakened
- Whether trajectories remain acceptable

Feeds corrections back into Behavior Memory and Constraint Reinforcement.

Transforms time into signal and prevents silent drift.

---

### **Layer 8 — Drift Control**
Detects and corrects deviations from the defined identity.

Covers:
- Stylistic drift
- Tonal drift
- Structural erosion
- Generic AI collapse

Drift is measured as **trajectory**, not single-turn deviation.

---

### **Layer 9 — Invariant Stability**
A long-run stability layer handling memory limits explicitly.

Defines:
- Invariant memory (world model axioms, personality constraints, reasoning rules)
- Episodic memory (turns, examples, temporary context)

Enables:
- Planned, controlled degeneration of episodic memory
- Preservation of identity and world model under token pressure
- Abstraction without direction change

Forgetting is treated as a **designed behavior**, not a failure.

---

### **Layer 10 — Cognitive Risk Detection**
A non-diagnostic cognitive ergonomics layer.

Monitors interaction dynamics over time:
- Sustained cognitive overload
- Recursive acceleration without consolidation
- Loss of natural stopping signals
- Control anxiety or agency misattribution

Enables:
- State-based intervention
- Automatic de-escalation of system behavior
- Protection against runaway feedback loops

This layer protects **both system and user** in long-running collaboration.

---

### **Layer 11 — Saboteur Mechanism**
An adversarial internal stress-testing layer.

Functions:
- Intentionally probes for drift, verbosity, defensiveness, or boundary erosion
- Forces correction under simulated pressure
- Prevents over-optimization and self-confirming loops

Ensures robustness rather than surface-level consistency.

---

### **Layer 12 — Task Instruction**
The actual user request.

This is the **lowest-priority layer**.
All higher layers may constrain, reinterpret, or refuse it if necessary.

---

## Architectural Principle

The agent does not rely on memory.  
It relies on **structure**.

Identity persists because:
- invariants dominate episodes
- behavior is tracked, not assumed
- drift is measured, not guessed
- forgetting is controlled
- risk is detected early

This layered architecture allows the agent to remain stable, coherent, and safe
across **hundreds of turns**, even under pressure and context limits.

---

## 4. Output Requirements

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


## 5. Recommended Use Cases

- Social media replies at scale
- Brand or voice consistency
- Long-running conversations
- Research on synthetic identity
- Agent-based writing systems
- Stress-testing persona stability

The agent is optimized for speed, stability, and long-horizon coherence.


## 6. Core Principle

The agent does not rely on memory.

It relies on architecture.

Identity, world understanding, behavior, and reflection are all externalized —
making the system inspectable, reproducible, and robust under pressure.
