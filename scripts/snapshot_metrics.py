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


def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    try:
        repo = get(API, token)
        releases = get(f"{API}/releases", token)
        issues = get(f"{API}/issues?state=open&per_page=1", token)
        pulls = get(f"{API}/pulls?state=open&per_page=1", token)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

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
        "note": "Public metrics only. No fabricated values. stars/forks/open issues reflect the snapshot date.",
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"snapshot-{snapshot['snapshot_date']}.json"
    out.write_text(json.dumps(snapshot, indent=2), encoding="utf-8")
    print(f"Wrote {out}")
    print(json.dumps(snapshot["repository"], indent=2))


if __name__ == "__main__":
    main()
