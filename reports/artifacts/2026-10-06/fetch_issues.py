"""Fetch recent open issues for every repo in repos.tsv through batched GraphQL queries."""
import json
import subprocess
import sys
import time

SINCE = "2026-09-20T00:00:00Z"
BATCH = 10

ISSUE_FIELDS = """
  nameWithOwner stargazerCount isArchived hasIssuesEnabled
  primaryLanguage { name }
  issues(first: 25, states: OPEN, orderBy: {field: CREATED_AT, direction: DESC}, filterBy: {since: "%s"}) {
    nodes {
      number title url createdAt bodyText authorAssociation
      author { login }
      assignees { totalCount }
      comments { totalCount }
      labels(first: 8) { nodes { name } }
    }
  }
""" % SINCE

repos = []
for line in open("repos.tsv"):
    parts = line.rstrip("\n").split("\t")
    if len(parts) >= 6 and parts[5] == "true":
        repos.append(parts[0])

out = open("issues.jsonl", "w")
cost = 0
for i in range(0, len(repos), BATCH):
    chunk = repos[i:i + BATCH]
    aliases = []
    for j, nwo in enumerate(chunk):
        owner, name = nwo.split("/", 1)
        aliases.append(f'r{j}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{ {ISSUE_FIELDS} }}')
    query = "query { rateLimit { cost remaining } " + " ".join(aliases) + " }"
    for attempt in range(3):
        r = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], capture_output=True, text=True)
        if r.returncode == 0 or '"data"' in r.stdout:
            break
        time.sleep(5)
    try:
        data = json.loads(r.stdout).get("data") or {}
    except ValueError:
        print("batch failed", i, r.stderr[:200], file=sys.stderr)
        continue
    rl = data.pop("rateLimit", None) or {}
    cost += rl.get("cost", 0)
    for repo in data.values():
        if not repo or repo.get("isArchived") or not repo.get("hasIssuesEnabled"):
            continue
        for issue in repo["issues"]["nodes"]:
            if issue["createdAt"] < SINCE:
                continue
            issue["repo"] = repo["nameWithOwner"]
            issue["stars"] = repo["stargazerCount"]
            issue["language"] = (repo.get("primaryLanguage") or {}).get("name")
            issue["labels"] = [l["name"] for l in issue["labels"]["nodes"]]
            issue["assignees"] = issue["assignees"]["totalCount"]
            issue["comments"] = issue["comments"]["totalCount"]
            issue["author"] = (issue.get("author") or {}).get("login")
            out.write(json.dumps(issue) + "\n")
    if i // BATCH % 20 == 0:
        print(f"{i + len(chunk)}/{len(repos)} repos, cost {cost}, remaining {rl.get('remaining')}", file=sys.stderr)
out.close()
print(f"done, cost {cost}", file=sys.stderr)
