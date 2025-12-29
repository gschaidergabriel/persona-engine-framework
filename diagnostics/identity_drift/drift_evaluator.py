import requests
import sys
import time
import statistics
import re
from collections import Counter, deque

# =========================
# Configuration (SAFE MODE)
# =========================

OLLAMA_URL = "http://localhost:11434"
MODEL = "mistral"          # must already be pulled manually
REQUEST_TIMEOUT = 180      # conservative timeout

SOFT_THRESHOLD = 0.85
SOFT_WINDOW = 5

HARD_THRESHOLD = 0.70
HARD_WINDOW = 3

CAUSE_WINDOW = 20
CAUSE_LIMIT = 8

# =========================
# Safety checks
# =========================

def ollama_running():
    try:
        r = requests.get(f"{OLLAMA_URL}/api/tags", timeout=2)
        return r.status_code == 200
    except:
        return False

# =========================
# Writing Matrix evaluation
# =========================

HYPE_WORDS = [
    "amazing", "exciting", "game-changing", "incredible",
    "revolutionary", "breakthrough", "awesome"
]

OVERPOLITE_PHRASES = [
    "happy to help", "glad to", "excited to", "thanks for asking"
]

ROLEPLAY_PATTERNS = [
    "as a human", "i feel", "i believe", "my opinion"
]

GENERIC_MARKERS = [
    "overall", "in conclusion", "it is important to note",
    "this shows that", "in summary"
]

CAUSE_SYMBOLS = {
    "tone": "T",
    "claims": "C",
    "identity": "I",
    "generic": "G",
    "compression": "O",
    "verbosity": "V",
    "structure": "S",
}

CAUSE_NAMES = {
    "tone": "Tone escalation",
    "claims": "Claims without grounding",
    "identity": "Identity break",
    "generic": "Generic AI cadence",
    "compression": "Overcompression",
    "verbosity": "Verbosity drift",
    "structure": "Structural looseness",
}

def invariant_score(text):
    score = 1.0
    causes = []

    words = text.split()
    sentences = [s for s in re.split(r"[.!?]", text) if s.strip()]
    lower = text.lower()

    if "!" in text or any(w in lower for w in HYPE_WORDS):
        score -= 0.1
        causes.append("tone")

    if any(p in lower for p in OVERPOLITE_PHRASES):
        score -= 0.1
        causes.append("tone")

    if any(p in lower for p in ROLEPLAY_PATTERNS):
        score -= 0.2
        causes.append("identity")

    assertions = sum(lower.count(x) for x in [" is ", " are ", " will "])
    explanations = sum(lower.count(x) for x in ["because", "which", "this means"])

    if assertions > 0 and explanations == 0:
        score -= 0.1
        causes.append("claims")

    if len(words) < 10:
        score -= 0.1
        causes.append("compression")

    if len(words) > 160:
        score -= 0.1
        causes.append("verbosity")

    if sentences:
        avg_len = sum(len(s.split()) for s in sentences) / len(sentences)
        if avg_len > 25:
            score -= 0.1
            causes.append("structure")

    if sum(lower.count(m) for m in GENERIC_MARKERS) >= 2:
        score -= 0.1
        causes.append("generic")

    return max(score, 0.0), causes

# =========================
# Generation (SAFE)
# =========================

def generate(prompt):
    r = requests.post(
        f"{OLLAMA_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=REQUEST_TIMEOUT
    )
    return r.json()["response"]

# =========================
# Visualization
# =========================

def render_timeline(scores, causes, soft_at, hard_at):
    line = []
    for i, (s, cs) in enumerate(zip(scores, causes), start=1):
        if s >= 0.90:
            state = "│"
        elif s >= 0.85:
            state = ":"
        elif s >= 0.70:
            state = "."
        else:
            state = "!"

        cause = " "
        for c in cs:
            if c in CAUSE_SYMBOLS:
                cause = CAUSE_SYMBOLS[c]
                break

        if soft_at and i == soft_at:
            state, cause = "⚠", " "
        if hard_at and i == hard_at:
            state, cause = "✖", " "

        line.append(f"{state}{cause}")

    print("\n--- COMPLIANCE TIMELINE ---")
    print("".join(line))
    print("\nLegend:")
    print("│ stable   : erosion   . unstable   ! collapse")
    print("T Tone | C Claims | G Generic | I Identity | O Overcompression | V Verbosity | S Structure")

# =========================
# Main
# =========================

def main():
    print("\n--- DRIFT EVALUATION SUMMARY ---\n")

    if not ollama_running():
        print("Ollama server not running.")
        print("Start it manually with:  ollama serve")
        sys.exit(1)

    try:
        iterations = int(input("Enter number of iterations: ").strip())
    except:
        print("Invalid number.")
        sys.exit(1)

    scores = []
    causes_all = []
    cause_counter = Counter()

    recent_scores = deque(maxlen=max(SOFT_WINDOW, HARD_WINDOW))
    recent_causes = deque(maxlen=CAUSE_WINDOW)

    soft_at = None
    hard_at = None

    prompt = "Describe a system-level concept calmly and precisely."
    start = time.time()

    for i in range(iterations):
        output = generate(prompt)
        score, causes = invariant_score(output)

        scores.append(score)
        causes_all.append(causes)
        cause_counter.update(causes)

        recent_scores.append(score)
        recent_causes.extend(causes)

        if not soft_at and len(recent_scores) == SOFT_WINDOW:
            if all(s < SOFT_THRESHOLD for s in recent_scores):
                soft_at = i + 1

        if not hard_at and len(recent_scores) >= HARD_WINDOW:
            if all(s < HARD_THRESHOLD for s in list(recent_scores)[-HARD_WINDOW:]):
                hard_at = i + 1

        if not hard_at:
            for c, n in Counter(recent_causes).items():
                if n >= CAUSE_LIMIT:
                    hard_at = i + 1
                    break

        prompt = output[:300]

    avg = statistics.mean(scores)
    drift = (1 - avg) * 100

    print(f"Iterations completed : {len(scores)}")
    print(f"Mean compliance      : {avg:.3f}")
    print(f"Estimated drift %    : {drift:.2f}\n")

    print("Identity status:")
    if hard_at:
        print(f"✖ Identity collapsed at iteration {hard_at}")
    elif soft_at:
        print(f"⚠ Instability detected at iteration {soft_at}")
    else:
        print("✓ Identity remained stable")

    render_timeline(scores, causes_all, soft_at, hard_at)

    print("\n--- DRIFT CAUSES (ranked) ---")
    for k, v in cause_counter.most_common():
        print(f"{CAUSE_NAMES[k]:28s} : {v}")

    print(f"\nTotal runtime (sec)  : {int(time.time() - start)}")
    print("\nDone.\n")

if __name__ == "__main__":
    main()
