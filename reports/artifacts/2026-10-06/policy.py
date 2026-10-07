"""Collect AI-policy text for each repo (and its org's .github repo) and pre-classify it.

The classification is only a hint: earlier rounds showed it fails both ways, so every
shortlisted repo's policy is read in full afterwards.
"""
import base64
import json
import re
import subprocess

FILES = ["AI.md", "AI_POLICY.md", "AGENT_POLICY.md", "AGENTS.md", "CONTRIBUTING.md", ".github/CONTRIBUTING.md",
         "docs/CONTRIBUTING.md", ".github/PULL_REQUEST_TEMPLATE.md", ".github/pull_request_template.md",
         "CODE_OF_CONDUCT.md"]
AI_LINE = re.compile(r"\b(AI|A\.I\.|LLMs?|GenAI|generative|Copilot|ChatGPT|Claude|agentic|AI[- ]assisted|AI[- ]generated|machine[- ]generated)\b")
PROHIBIT = re.compile(r"(not|never|no longer) (accept|allow|merge|welcome)|prohibit|forbid|ban(ned)?\b|must not|do not (use|submit|open)|"
                      r"will be closed|zero[- ]tolerance|not permitted|strictly", re.I)
DISCLOSE = re.compile(r"disclos|declare|mention (that|if|whether)|state (that|whether)|label|tag|check the box|checkbox|Assisted-by|Co-authored", re.I)
HUMAN = re.compile(r"your own words|written by (a )?human|human[- ]written|do not use .{0,30}(to write|for) (comments|descriptions|communication)", re.I)


def fetch(nwo, path):
    r = subprocess.run(["gh", "api", f"repos/{nwo}/contents/{path}", "--jq", ".content"], capture_output=True, text=True)
    if r.returncode or not r.stdout.strip():
        return ""
    try:
        return base64.b64decode(r.stdout.strip()).decode("utf-8", "ignore")
    except ValueError:
        return ""


def existing(nwo, candidates):
    """Only fetch files that exist: list the root and .github once instead of probing each path."""
    found = set()
    for base in ("", ".github", "docs"):
        r = subprocess.run(["gh", "api", f"repos/{nwo}/contents/{base}", "--jq", ".[].path"], capture_output=True, text=True)
        found |= set(r.stdout.split())
    return [f for f in candidates if f in found]


repos = sorted({json.loads(l)["repo"] for l in open("stage2.jsonl")})
orgs = sorted({r.split("/")[0] for r in repos})
org_text = {o: "\n".join(fetch(f"{o}/.github", f) for f in existing(f"{o}/.github", FILES)) for o in orgs}

out = {}
for nwo in repos:
    text = "\n".join(fetch(nwo, f) for f in existing(nwo, FILES)) + "\n" + org_text[nwo.split("/")[0]]
    lines = [l.strip() for l in text.splitlines() if AI_LINE.search(l)]
    joined = " ".join(lines)
    if not lines:
        kind = "sin política"
    elif PROHIBIT.search(joined):
        kind = "posible prohibición"
    elif HUMAN.search(joined):
        kind = "comunicación humana"
    elif DISCLOSE.search(joined):
        kind = "disclosure"
    else:
        kind = "menciona IA"
    out[nwo] = {"kind": kind, "lines": lines[:12]}
json.dump(out, open("policy.json", "w"), indent=1, ensure_ascii=False)
from collections import Counter
print(Counter(v["kind"] for v in out.values()))
