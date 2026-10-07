"""First deterministic cut over issues.jsonl: actionable, unclaimed-looking bugs."""
import json
import math
import re

ours = {l.strip().lower() for l in open("our_repos.txt") if l.strip()}
# Restrictive AI policies or closed contribution models found in earlier rounds.
BLOCKED_REPOS = {
    "bevyengine/bevy", "jesseduffield/lazygit", "influxdata/telegraf",
    "cookiecutter/cookiecutter-django", "frappe/frappe", "frappe/erpnext",
    # 2026-10-06: AI prohibited, unsolicited PRs closed, vouch-only, or no external merges.
    "TeamNewPipe/NewPipe", "imputnet/helium", "syncthing/syncthing", "lightgbm-org/LightGBM",
    "odysseus-dev/odysseus", "stashapp/stash", "cjpais/Handy", "open-webui/open-webui",
    "godotengine/godot", "juanfont/headscale", "netdata/netdata", "opendatalab/MinerU",
}
BLOCKED_OWNERS = {"astral-sh", "open-telemetry", "fatiando", "elastic"}
# Need an approved, assigned issue before any PR (bots close the rest).
ASSIGNMENT_GATED_OWNERS = {"langchain-ai"}

BUG_LABEL = re.compile(r"(^|[^a-z])(bug|defect|regression|crash|panic|kind/bug|type: ?bug|t-bug|c-bug|confirmed)([^a-z]|$)", re.I)
HELP_LABEL = re.compile(r"good first issue|help wanted|contributions? welcome|easy", re.I)
SKIP_LABEL = re.compile(r"question|discussion|feature|enhancement|proposal|wontfix|won't fix|duplicate|invalid|stale|"
                        r"needs[- ]?(info|repro|reproduction|more)|waiting|blocked|upstream|security|epic|rfc|design", re.I)
BUG_TITLE = re.compile(r"\b(bug|crash|crashes|panic|error|fails?|failing|broken|regression|incorrect|wrong|"
                       r"exception|segfault|leak|hang|hangs|not work|doesn't|does not|ignored?)\b", re.I)
SELF_FIX = re.compile(r"(i('| a)?m (working|going) on|i('ll| will) (open|submit|send|create|make) (a )?(pr|pull)|"
                      r"pr (incoming|coming|is on the way)|i have a (fix|patch)|happy to (open|submit|send) a (pr|pull)|"
                      r"i can (open|submit|send) a (pr|pull)|willing to (open|submit) a (pr|pull)|"
                      r"would like to (work on|fix|contribute)|i('d| would) like to (open|submit|send) a)", re.I)

kept, stats = [], {}


def drop(reason):
    stats[reason] = stats.get(reason, 0) + 1


for line in open("issues.jsonl"):
    i = json.loads(line)
    repo = i["repo"].lower()
    if repo in ours:
        drop("repo con PR nuestro"); continue
    if repo in {r.lower() for r in BLOCKED_REPOS} or repo.split("/")[0] in BLOCKED_OWNERS | ASSIGNMENT_GATED_OWNERS:
        drop("repo/org con política restrictiva"); continue
    if i["assignees"]:
        drop("asignado"); continue
    if i["authorAssociation"] in ("OWNER", "MEMBER", "COLLABORATOR"):
        drop("abierto por el equipo"); continue
    labels = i["labels"]
    if any(SKIP_LABEL.search(l) for l in labels):
        drop("label no accionable"); continue
    bugish = any(BUG_LABEL.search(l) for l in labels)
    helpish = any(HELP_LABEL.search(l) for l in labels)
    if not (bugish or helpish or (not labels and BUG_TITLE.search(i["title"]))):
        drop("no parece bug"); continue
    body = i["bodyText"] or ""
    if len(body) < 300:
        drop("cuerpo sin contexto"); continue
    if sum(ord(c) > 127 for c in body) / max(len(body), 1) > 0.05:
        drop("no está en inglés"); continue
    if i["comments"] > 6:
        drop("hilo largo"); continue
    if SELF_FIX.search(body):
        drop("el reportante trae el fix"); continue
    score = (math.log10(i["stars"]) * 2 + (2 if bugish else 0) + (1.5 if helpish else 0)
             + min(len(body), 3000) / 1500 - i["comments"] * 0.3
             + (1 if "```" in body or "Traceback" in body or "Steps to reproduce" in body or "reproduc" in body.lower() else 0))
    i["score"] = round(score, 2)
    kept.append(i)

kept.sort(key=lambda x: -x["score"])
with open("stage1.jsonl", "w") as f:
    for i in kept:
        f.write(json.dumps(i) + "\n")
for k, v in sorted(stats.items(), key=lambda kv: -kv[1]):
    print(f"{v:6d}  {k}")
print(f"{len(kept):6d}  pasan el primer corte ({len({i['repo'] for i in kept})} repos)")
