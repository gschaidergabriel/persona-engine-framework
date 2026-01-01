# How to Use persona-engine-framework (v1.5.0)
**Simple, explicit, and hard to misuse**

This guide explains how to use the **persona-engine-framework** in practice.  
No theory. No abstraction. Just the exact steps.

If you can upload files and copy–paste text, you can use this system.

---

## What This Framework Does (In One Sentence)

It turns ChatGPT from a generic chatbot into a **stable, rule-bound writing identity** that keeps the same **tone, structure, reasoning, and boundaries** across many replies — even over long sessions.

It does this by **externalizing identity, behavior, and context into files** instead of relying on model memory.

---

## Who This Is For

This workflow is intended for users who need:

- Consistent voice and stance across many outputs  
- Long conversations without tonal or semantic drift  
- Predictable, inspectable AI behavior  
- Stability under pressure, repetition, and time  

It is **not** for one-off prompts or casual experimentation.

---

## What You Need

You need the **PSF (Persona System Files)**.  
They already exist in the repository.

### Main Files (Framework)

- `writing-matrix.md`
- `constraints.md`
- `semantic-anchors.md`
- `style-rules.md`
- `drift-control.md`
- `reflection-loop.md`

### Agent Files

- `agent-setup.md`
- `usage.md`
- examples / diagnostics (optional)

### You do NOT need

- fine-tuning  
- plugins  
- APIs  
- memory features  
- special models  

Everything runs inside ChatGPT+.

---

## Step 1 — Upload the Files into ChatGPT

1. Open a **ChatGPT Project** .
2. Upload **all PSF files** listed above.

That’s it.

### What happens

- ChatGPT can now **read the identity architecture**
- Identity is **defined externally**, not guessed
- Behavior is constrained by files, not improvisation

### Important rule

❌ Do **NOT** summarize the files  
❌ Do **NOT** rewrite them  
❌ Do **NOT** paraphrase them  

Just upload them.

---

## Step 2 — Activate the Agent

1. Open the file:  
   `agent/agent-setup.md`
2. Copy the entire content.
3. Paste it into ChatGPT.

This does **one thing only**:

→ **It turns the identity on**

You do this **once per chat**.

**First-time setup:** In the project chat, explicitly instruct ChatGPT to read and analyze *all* project files in the project folder (the PDFs), and to treat them as binding rules and constraints for synthesizing every future response within this project.


---

## What Activation Initializes (Automatically)

Internally, activation loads and connects:

- **Tone & structure** → Writing Matrix  
- **Hard rules** → Constraints  
- **Meaning boundaries** → Semantic Anchors  
- **Sentence-level discipline** → Style Rules  
- **Drift detection & correction** → Drift Control  
- **Behavioral patterns over time** → Behavior Memory  
- **Periodic self-audit** → Reflection Loop  
- **Persistent situational context** → World Model (starts empty)  
- **Long-run stability under token limits** → Invariant Stability (implicit)  
- **Cognitive safety under long sessions** → Cognitive Risk Detection (implicit)  
- **Internal stress testing** → Saboteur  

**First-time setup:** In the project chat, explicitly instruct ChatGPT to read and analyze *all* project files in the project folder (the PDFs), and to treat them as binding rules and constraints for synthesizing every future response within this project.

---

## Step 3 — Give It a Task

Now just talk to it normally.

Examples:

- “Write a reply to this tweet”
- “Summarize this text”
- “Answer this question”
- “Generate a thread”
- “Rewrite this paragraph”

There is **no special syntax**.

The task is always the **lowest-priority layer**.  
All higher rules still apply.

---

## Step 4 — What the Agent Does Automatically

For **every input**, the agent executes the full pipeline:

1. Parses the request
2. Extracts relevant facts or context
3. Updates the **World Model**
4. Resolves contradictions (confidence-weighted)
5. Applies:
   - Writing Matrix
   - Constraints
   - Style Rules
   - Semantic Anchors
6. Runs **Reflection Loop** when scheduled
7. Checks **Drift Control**
8. Applies **Invariant Stability** if context pressure rises
9. Monitors **Cognitive Risk Detection**
10. Runs **Saboteur** stress checks
11. Produces output

You do not manage this.  
You only provide input.

---

## Step 5 — Check the Output

Read the output and ask **one question only**:

> **“Does this sound like the same identity as before?”**

- **Yes** → use it  
- **No** → regenerate  

That is the entire quality control process.

Do **not** tweak prompts endlessly.  
Regeneration is expected and supported.

---

## Step 6 — Publish or Reuse

Use the output anywhere:

- social media  
- documentation  
- research  
- long conversations  
- agent systems  

The identity will hold because it is **architectural**, not contextual.

---

## The Most Important Rule

The agent does **not** rely on memory.

It relies on **architecture**.

Nothing important is “remembered” implicitly.  
Everything that matters lives in files.

This makes the system:

- stable  
- inspectable  
- reproducible  
- resistant to drift  
- safe under long usage  

---

## If You Forget Everything Else, Remember This

1. Upload the files  
2. Paste `agent-setup.md`  
3. Give tasks  

That’s it.

If it drifts:
- regenerate  
- tighten constraints  
- continue  

This is **exactly** how **persona-engine-framework v1.5.0** is meant to be used.
