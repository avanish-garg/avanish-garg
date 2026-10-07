#!/usr/bin/env python3
"""Rewrites the ACTIVITY block in readme.md with this account's most recent
pull requests across a fixed list of tracked repos. Read-only against the
GitHub REST search API; writes only to readme.md.
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

USERNAME = "avanish-garg"
TRACKED_REPOS = [
    "apache/airflow",
    "collabora/WhisperLive",
    "ComposioHQ/composio",
    "docling-project/docling",
    "etcd-io/etcd",
    "getlago/lago-api",
    "mastra-ai/mastra",
    "mlflow/mlflow",
    "qdrant/qdrant",
    "temporalio/ai-integrations",
    "truera/trulens",
    "weaviate/weaviate",
]
MAX_ITEMS = 6
# Reserve slots so merged work stays visible instead of being crowded out by a
# wave of newer open PRs in a pure recency sort - a recruiter skimming this
# list should see completed, accepted work, not just what's currently pending.
MIN_MERGED_ITEMS = 3
START_MARKER = "<!-- ACTIVITY:START -->"
END_MARKER = "<!-- ACTIVITY:END -->"
README_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "readme.md")

TOKEN = os.environ.get("GITHUB_TOKEN", "")


def api_get(url):
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp)


def fetch_prs_for_repo(repo):
    q = f"is:pr author:{USERNAME} repo:{repo}"
    url = "https://api.github.com/search/issues?q=" + urllib.parse.quote(q) + "&sort=created&order=desc&per_page=10"
    data = api_get(url)
    return data.get("items", [])


def pr_state(item):
    pr = item.get("pull_request") or {}
    if pr.get("merged_at"):
        return "merged"
    if item.get("state") == "closed":
        return "closed"
    if pr.get("draft"):
        return "draft"
    return "open"


def main():
    all_items = []
    for repo in TRACKED_REPOS:
        try:
            items = fetch_prs_for_repo(repo)
        except Exception as exc:  # noqa: BLE001 - one repo's failure shouldn't kill the run
            print(f"warning: failed to fetch {repo}: {exc}", file=sys.stderr)
            items = []
        for item in items:
            item["_repo"] = repo
        all_items.extend(items)

    for item in all_items:
        item["_state"] = pr_state(item)

    merged_items = [i for i in all_items if i["_state"] == "merged"]
    other_items = [i for i in all_items if i["_state"] != "merged"]
    merged_items.sort(key=lambda i: i["pull_request"]["merged_at"], reverse=True)
    other_items.sort(key=lambda i: i["created_at"], reverse=True)

    # Reserved merged slots first (most recently merged), then fill the rest of
    # the list with whatever's most recent overall - merged or not.
    top = merged_items[:MIN_MERGED_ITEMS]
    selected_ids = {i["id"] for i in top}
    fill_pool = sorted(
        (i for i in (merged_items[MIN_MERGED_ITEMS:] + other_items) if i["id"] not in selected_ids),
        key=lambda i: i["created_at"],
        reverse=True,
    )
    top += fill_pool[: MAX_ITEMS - len(top)]

    lines = []
    for item in top:
        lines.append(f"- **[{item['_repo']}]** [{item['title']}]({item['html_url']}) &mdash; _{item['_state']}_")

    if not lines:
        lines = ["- No tracked pull requests found yet."]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    block = "\n".join([START_MARKER, *lines, f"\n_Last updated {now}._", END_MARKER])

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find(START_MARKER)
    end_idx = content.find(END_MARKER)
    if start_idx == -1 or end_idx == -1:
        print("error: markers not found in readme.md", file=sys.stderr)
        sys.exit(1)

    new_content = content[:start_idx] + block + content[end_idx + len(END_MARKER):]

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    main()
