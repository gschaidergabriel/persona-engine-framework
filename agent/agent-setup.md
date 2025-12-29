# Agent Setup

This document describes how to configure an LLM-based agent that uses the Writing Matrix, constraints, and drift-control system to generate consistent, high-quality replies.

---

## 1. Purpose of the Agent

The agent is designed to:
- apply the Writing Matrix automatically  
- enforce constraints  
- maintain tonal and semantic stability  
- generate replies rapidly  
- avoid drift and generic AI tone  

The agent is not a chatbot.  
It is a controlled writing system.

---

## 2. Required Components

To set up the agent, you need:

- The Writing Matrix  
- The Constraint System  
- Semantic Anchors  
- Drift-Control Rules  
- Style Rules  
- A curation workflow (see `workflow.md`)  

These components form the identity architecture.

---

## 3. Agent Prompt Structure

A stable agent uses a layered prompt:

### **Layer 1 — Identity Core**
Defines the synthetic persona’s purpose and tone.

### **Layer 2 — Writing Matrix**
Provides the structural and stylistic blueprint.

### **Layer 3 — Constraints**
Defines non-negotiable rules.

### **Layer 4 — Drift Control**
Ensures long-term consistency.

### **Layer 5 — Task Instruction**
The actual user request.

---

## 4. Recommended Prompt Template

