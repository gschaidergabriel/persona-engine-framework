# How to Use persona-engine-framework (v1.5.0)
Simple, explicit, and hard to misuse

This guide explains how to use the persona-engine-framework in practice.
No theory. No abstraction. Just the exact steps.

If you can upload files and copy–paste text, you can use this system.

---

## What This Framework Does (In One Sentence)

It turns ChatGPT from a generic chatbot into a **stable, rule-bound writing identity**
that keeps the same tone, structure, and reasoning across many replies.

It does this by **externalizing identity and context into files**.

---

## What You Need

You need the PSF (Persona System Files).  
They already exist in the repository.

Main files:

- Writing Matrix
- Constraints
- Semantic Anchors
- Style Rules
- Drift Control
- World Model
- Behavior Memory
- Reflection Loop
- Agent Setup
- Workflow
- Examples

You do **not** need:
- fine-tuning
- plugins
- APIs
- memory features
- special models

---

## Step 1 — Upload the Files into ChatGPT

Open a ChatGPT project.

Upload **all PSF files**.

That’s it.

What happens:
- ChatGPT can now *read* the identity architecture
- The identity is defined externally, not guessed

Important rule:

Do NOT summarize the files.  
Do NOT rewrite them.  
Just upload them.

---

## Step 2 — Activate the Agent

Open the file:

`agent/agent-setup.md`

Copy it.

Paste it into ChatGPT.

This does ONE thing:
→ it turns the identity on

Internally, this initializes:

- tone and structure (Writing Matrix)
- hard rules (Constraints)
- meaning boundaries (Semantic Anchors)
- style enforcement
- drift detection
- behavior patterns
- reflection rules
- the World Model (empty but ready)

You only do this **once per chat**.

---

## Step 3 — Give It a Task

Now just talk to it.

Examples:
- “Write a reply to this tweet”
- “Summarize this text”
- “Answer this question”
- “Generate a thread”

There is no special syntax.

---

## Step 4 — What the Agent Does Automatically

For every input, the agent does this:

1. Extracts important facts or context  
2. Updates the World Model  
3. Resolves contradictions  
4. Generates output using:
   - Writing Matrix
   - Constraints
   - Style Rules
   - Semantic Anchors
   - Behavior Memory
   - Reflection Loop
   - Current World Model
5. Checks for drift

You do not trigger these steps.
They are mandatory and automatic.

---

## Step 5 — Check the Output

Read the output.

Ask ONE question:

“Does this sound like the same identity as before?”

- Yes → use it
- No → regenerate

That’s the entire quality control process.

---

## Step 6 — Publish or Reuse

Take the output and use it anywhere:
- social media
- documentation
- research
- long conversations
- agent systems

---

## The Most Important Rule

The agent does NOT rely on memory.

It relies on architecture.

Nothing is “remembered” implicitly.
Everything important lives in files.

This makes the system:
- stable
- inspectable
- reproducible
- resistant to drift
- safe under long usage

---

## If You Forget Everything Else, Remember This

1. Upload the files  
2. Paste the agent setup  
3. Give tasks  

That’s it.

If it drifts:
→ regenerate  
→ tighten constraints  
→ continue  

This is exactly how persona-engine-framework v1.5.0 is meant to be used.
