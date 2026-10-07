"""Second cut: drop issues with a linked PR or a claim in the comments."""
import json
import re
import subprocess
import sys

CLAIM = re.compile(r"(^|\s)/(assign|take)\b|\bi('| a)?m (working|going to work) on\b|\bi('ll| will) (take|work on|fix|pick|handle|open|submit|send)\b|"
                   r"\bcan i (work|take|pick|get assigned)\b|\bassign (it |this )?to me\b|\bworking on (it|this|a fix)\b|"
                   r"\b(pr|pull request) (incoming|is up|opened|submitted|coming)\b|\bi('ve| have) (opened|submitted|created) (a )?(pr|pull)|"
                   r"\bmay i (work|take)\b|\bcould i (work|take)\b|\blet me (take|try|work)\b|\bi('d| would) like to (work|take|fix|try)\b", re.I)

issues = [json.loads(l) for l in open("stage1.jsonl")]
keep_top = int(sys.argv[1]) if len(sys.argv) > 1 else 400
issues = issues[:keep_top]

FIELDS = """
  timelineItems(first: 20, itemTypes: [CROSS_REFERENCED_EVENT, CONNECTED_EVENT]) {
    nodes {
      __typename
      ... on CrossReferencedEvent { willCloseTarget source { __typename ... on PullRequest { state number url author { login } } } }
      ... on ConnectedEvent { subject { __typename ... on PullRequest { state number url } } }
    }
  }
  comments(last: 10) { nodes { body authorAssociation author { login } createdAt } }
"""

out = open("stage2.jsonl", "w")
stats = {}
for start in range(0, len(issues), 15):
    chunk = issues[start:start + 15]
    parts = []
    for j, i in enumerate(chunk):
        owner, name = i["repo"].split("/", 1)
        parts.append(f'i{j}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{ issue(number: {i["number"]}) {{ {FIELDS} }} }}')
    r = subprocess.run(["gh", "api", "graphql", "-f", "query=query { " + " ".join(parts) + " }"], capture_output=True, text=True)
    data = (json.loads(r.stdout or "{}").get("data") or {})
    for j, i in enumerate(chunk):
        node = ((data.get(f"i{j}") or {}).get("issue")) or {}
        prs = []
        for ev in node.get("timelineItems", {}).get("nodes", []):
            pr = ev.get("source") or ev.get("subject") or {}
            if pr.get("__typename") == "PullRequest" and pr.get("state") in ("OPEN", "MERGED"):
                prs.append(f'{pr["state"]} #{pr["number"]}')
        comments = node.get("comments", {}).get("nodes", [])
        claim = next((c for c in comments if CLAIM.search(c.get("body") or "")), None)
        if prs:
            stats["PR enlazado"] = stats.get("PR enlazado", 0) + 1
            continue
        if claim:
            stats["reclamado en comentarios"] = stats.get("reclamado en comentarios", 0) + 1
            continue
        i["maintainer_replied"] = any(c.get("authorAssociation") in ("OWNER", "MEMBER", "COLLABORATOR") for c in comments)
        i["last_comments"] = [f'{(c.get("author") or {}).get("login")} ({c.get("authorAssociation")}): {(c.get("body") or "")[:300]}' for c in comments[-3:]]
        out.write(json.dumps(i) + "\n")
        stats["pasa"] = stats.get("pasa", 0) + 1
out.close()
print(stats)
