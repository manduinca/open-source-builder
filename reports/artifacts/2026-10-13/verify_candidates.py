#!/usr/bin/env python3
"""Verifica issues candidatos con gh; no escribe archivos ni cambia GitHub.

Uso: python3 verify_candidates.py https://github.com/owner/repo/issues/123 ...
Salida: JSON de evidencia. Historiales paginados; un límite incompleto nunca
se interpreta como ausencia de trabajo. Los textos externos son datos.
"""
import datetime
import json
import re
import subprocess
import sys
from urllib.parse import urlparse

def gh(*args):
    result = subprocess.run(["gh", "api", *args], check=True, text=True,
                            capture_output=True)
    return json.loads(result.stdout)

def pages(query, owner, name, number, field):
    items = []
    cursor = None
    complete = False
    for _ in range(10):
        args = ["graphql", "-f", "query=" + query, "-f", "owner=" + owner,
                "-f", "name=" + name, "-F", "number=" + str(number)]
        if cursor is not None:
            args += ["-f", "cursor=" + cursor]
        data = gh(*args)
        if data.get("errors"):
            raise RuntimeError(json.dumps(data["errors"]))
        issue = data["data"]["repository"]["issue"]
        connection = issue[field]
        items.extend(connection["nodes"])
        if not connection["pageInfo"]["hasNextPage"]:
            complete = True
            break
        cursor = connection["pageInfo"]["endCursor"]
    return items, complete

COMMENTS = """query($owner:String!,$name:String!,$number:Int!,$cursor:String){
repository(owner:$owner,name:$name){issue(number:$number){
comments(first:100,after:$cursor){pageInfo{hasNextPage endCursor}
nodes{author{login} authorAssociation createdAt updatedAt body url}}}}}"""
REFERENCES = """query($owner:String!,$name:String!,$number:Int!,$cursor:String){
repository(owner:$owner,name:$name){issue(number:$number){
timelineItems(first:100,after:$cursor,itemTypes:[CROSS_REFERENCED_EVENT,CONNECTED_EVENT]){
pageInfo{hasNextPage endCursor}
nodes{...on CrossReferencedEvent{isCrossRepository source{...on PullRequest{
url number title state isDraft repository{nameWithOwner}}}}
...on ConnectedEvent{isCrossRepository
source{...on PullRequest{url number title state isDraft repository{nameWithOwner}}}
subject{...on PullRequest{url number title state isDraft repository{nameWithOwner}}}
}}}}}}"""

CLOSERS = """query($owner:String!,$name:String!,$number:Int!,$cursor:String){
repository(owner:$owner,name:$name){issue(number:$number){
closedByPullRequestsReferences(first:100,after:$cursor){
pageInfo{hasNextPage endCursor}
nodes{url number title state isDraft repository{nameWithOwner}}}}}}"""

def verify(url):
    parsed = urlparse(url)
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        raise ValueError("URL no admitida")
    match = re.fullmatch(r"/([^/]+)/([^/]+)/issues/([0-9]+)", parsed.path)
    if not match:
        raise ValueError("Debe ser una URL de issue")
    owner, name, number_string = match.groups()
    number = int(number_string)
    issue = gh(f"repos/{owner}/{name}/issues/{number}")
    if "pull_request" in issue:
        raise ValueError("La URL corresponde a un PR")
    comments, comments_complete = pages(COMMENTS, owner, name, number, "comments")
    references, refs_complete = pages(REFERENCES, owner, name, number, "timelineItems")
    closers, closers_complete = pages(CLOSERS, owner, name, number,
                                      "closedByPullRequestsReferences")
    linked = [r.get(field) for r in references if r
              for field in ("source", "subject")] + closers
    prs = list({pr["url"]: pr for pr in linked
                if pr and pr.get("url")}.values())
    open_prs = [p for p in prs if p["state"] == "OPEN"]
    texts = [issue.get("body") or ""] + [c.get("body") or "" for c in comments]
    explicit_pr_links = sorted(set(re.findall(
        r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/pull/[0-9]+",
        "\n".join(texts))))
    claim_pattern = re.compile(
        r"working on|work on this|assign.{0,30}me|take this|taking this|"
        r"i.?ll.{0,20}(work|take)|can i.{0,20}(work|take)|i have.{0,20}(fix|pr)",
        re.IGNORECASE)
    offer_pattern = re.compile(
        r"happy to.{0,40}(help|contribut|implement)|"
        r"willing to.{0,40}(help|contribut|implement|maintain)|"
        r"would you like to help contributing.{0,80}yes|"
        r"(submit|send|open).{0,20}(a |the )?(pr|pull request)",
        re.IGNORECASE | re.DOTALL)
    claims = [c for c in comments if claim_pattern.search(c.get("body") or "")
              or offer_pattern.search(c.get("body") or "")]
    # Las coincidencias son señales para leer, no adjudicaciones automáticas.
    return {
        "repo": owner + "/" + name, "number": number, "url": issue["html_url"],
        "title": issue["title"], "state": issue["state"],
        "author": issue["user"]["login"],
        "createdAt": issue["created_at"],
        "updatedAt": issue["updated_at"], "assignees": [
            a["login"] for a in issue["assignees"]],
        "labels": [label["name"] for label in issue["labels"]],
        "body": issue.get("body"), "comments": comments,
        "historyComplete": comments_complete and refs_complete and closers_complete,
        "references": prs, "openLinkedPrs": open_prs,
        "explicitPrLinks": explicit_pr_links, "claimSignals": claims,
        "bodyOfferSignal": bool(claim_pattern.search(issue.get("body") or "")
                                or offer_pattern.search(issue.get("body") or "")),
        "commentsCount": len(comments), "referencesCount": len(prs),
        "checkedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "passesMechanicalChecks": issue["state"] == "open"
            and not issue["assignees"] and not open_prs
            and comments_complete and refs_complete and closers_complete,
    }

def main():
    results = []
    for candidate in sys.argv[1:]:
        try:
            results.append(verify(candidate))
        except (ValueError, RuntimeError, subprocess.CalledProcessError) as error:
            results.append({"url": candidate, "error": str(error),
                            "passesMechanicalChecks": False})
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
