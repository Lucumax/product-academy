#!/usr/bin/env python3
"""
Snapshot public repository metrics into a dated JSON file.

Read-only: uses the public GitHub API (GITHUB_TOKEN env var with read-only scope, or
unauthenticated which is rate-limited). Run at each release and commit the snapshot so
history accrues.

Usage:
    GITHUB_TOKEN=... python scripts/snapshot_metrics.py
"""

import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path

OWNER = "Lucumax"
REPO = "product-academy"
API = f"https://api.github.com/repos/{OWNER}/{REPO}"
OUT_DIR = Path(__file__).resolve().parent.parent / "docs" / "growth" / "metrics"


def get(url, token):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    req.add_header("User-Agent", "product-academy-metrics-snapshot")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def post_graphql(token, query):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query}).encode("utf-8"),
        method="POST",
    )
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "product-academy-metrics-snapshot")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def discussion_count(token):
    """Returns open discussion count via GraphQL, or None when unavailable."""
    if not token:
        return None
    query = (
        "query { repository(owner: \"%s\", name: \"%s\") {"
        " discussions { totalCount } } }" % (OWNER, REPO)
    )
    try:
        data = post_graphql(token, query)
        return data.get("data", {}).get("repository", {}).get("discussions", {}).get(
            "totalCount"
        )
    except Exception:
        return None


def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    try:
        repo = get(API, token)
        releases = get(f"{API}/releases", token)
        issues = get(f"{API}/issues?state=open&per_page=1", token)
        pulls = get(f"{API}/pulls?state=open&per_page=1", token)
        contributors = get(f"{API}/contributors?per_page=100", token)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    discussions = discussion_count(token)
    has_discussions = repo.get("has_discussions", False)
    # GraphQL returns totalCount 0 even when discussions are DISABLED; distinguish the two.
    open_discussions = discussions if has_discussions else None

    external_contributors = [
        {"login": c.get("login"), "contributions": c.get("contributions")}
        for c in contributors
        if c.get("login") != OWNER
    ]

    snapshot = {
        "snapshot_date": datetime.date.today().isoformat(),
        "repository": {
            "full_name": repo.get("full_name"),
            "description": repo.get("description"),
            "homepage": repo.get("homepage"),
            "topics": repo.get("topics", []),
            "stars": repo.get("stargazers_count"),
            "forks": repo.get("forks_count"),
            "watchers": repo.get("subscribers_count"),
            "open_issues": len(issues),
            "open_pulls": len(pulls),
            "default_branch": repo.get("default_branch"),
        },
        "external_contributors": external_contributors,
        "discussions_enabled": has_discussions,
        "open_discussions": open_discussions,
        "releases": [
            {
                "tag": r.get("tag_name"),
                "published_at": r.get("published_at"),
                "assets": [
                    {"name": a.get("name"), "download_count": a.get("download_count")}
                    for a in r.get("assets", [])
                ],
            }
            for r in releases
        ],
        "note": "Public metrics only. No fabricated values. stars/forks/open issues reflect the snapshot date. open_discussions is null when discussions are disabled (a disabled feature is not '0 discussions').",
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"snapshot-{snapshot['snapshot_date']}.json"
    out.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(snapshot["repository"], indent=2))
    print("external_contributors:", len(external_contributors))
    print("discussions_enabled:", has_discussions, "| open_discussions:", open_discussions)


if __name__ == "__main__":
    main()
