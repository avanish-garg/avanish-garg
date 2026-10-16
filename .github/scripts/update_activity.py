#!/usr/bin/env python3
"""Rewrites the REPOS and ACTIVITY blocks in readme.md from this account's pull
requests across a fixed list of tracked repos: a per-repo summary (merged and
open counts) and the most recent pull requests. Read-only against the GitHub
REST search API; writes only to readme.md.
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
    "lancedb/lancedb",
    "mastra-ai/mastra",
    "mlflow/mlflow",
    "promptfoo/promptfoo",
    "qdrant/qdrant",
    "roboflow/supervision",
    "temporalio/ai-integrations",
    "truera/trulens",
    "weaviate/weaviate",
]
# One-line focus per repo for the summary table (static; edit when a repo gains a new area).
REPO_NOTES = {
    "apache/airflow": "Listener hooks for task retries and DAG pause state",
    "collabora/WhisperLive": "OpenVINO backend: prompts, hotwords, diarization",
    "ComposioHQ/composio": "Anthropic prompt caching and OpenAI Agents strict mode (Python), cache-breakpoint fix (TypeScript)",
    "docling-project/docling": "Office backends: DOCX/ODF footnotes, PPTX formatting and hyperlinks",
    "etcd-io/etcd": "etcdctl watch --from-key, concurrency.ResumeMutex",
    "getlago/lago-api": "Coupon and add-on lifecycle webhooks",
    "lancedb/lancedb": "Embedding retry/backoff on permanent errors, optimize() keeping tagged versions",
    "mastra-ai/mastra": "Evals and vector store fixes",
    "mlflow/mlflow": "Experiment and run restore, prompt search ordering, GCS/Azure presigned URLs",
    "promptfoo/promptfoo": "exec: provider argument quoting, unquoted YAML dates in config and test files",
    "qdrant/qdrant": "gRPC metrics whitelist, public gRPC Quotas service",
    "roboflow/supervision": "Mask-hole dataset export, CompactMask.resize parity, CSV export of array data",
    "temporalio/ai-integrations": "OpenAI Agents plugin: tool metadata, tool argument errors, RunState resume",
    "truera/trulens": "Bedrock and LangChain provider fixes, Cursor token usage",
    "weaviate/weaviate": "Backup API, tenant filtering, reranker config",
}
MAX_ITEMS = 6
# Reserve slots so merged work stays visible instead of being crowded out by a
# wave of newer open PRs in a pure recency sort - a recruiter skimming this
# list should see completed, accepted work, not just what's currently pending.
MIN_MERGED_ITEMS = 3
START_MARKER = "<!-- ACTIVITY:START -->"
END_MARKER = "<!-- ACTIVITY:END -->"
REPOS_START = "<!-- REPOS:START -->"
REPOS_END = "<!-- REPOS:END -->"
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
    url = "https://api.github.com/search/issues?q=" + urllib.parse.quote(q) + "&sort=created&order=desc&per_page=100"
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


def build_repo_table(all_items):
    """Summarize merged and open pull requests per repo (closed ones are skipped)."""
    stats = {}
    for item in all_items:
        row = stats.setdefault(item["_repo"], {"merged": 0, "open": 0})
        if item["_state"] == "merged":
            row["merged"] += 1
        elif item["_state"] in ("open", "draft"):
            row["open"] += 1
    rows = [(repo, c) for repo, c in stats.items() if c["merged"] or c["open"]]
    rows.sort(key=lambda r: (-r[1]["merged"], -r[1]["open"], r[0].lower()))
    lines = ["| Repository | Merged | Open | Focus |", "| --- | ---: | ---: | --- |"]
    for repo, c in rows:
        link = f"https://github.com/{repo}/pulls?q=is%3Apr+author%3A{USERNAME}"
        lines.append(f"| [{repo}]({link}) | {c['merged']} | {c['open']} | {REPO_NOTES.get(repo, '')} |")
    return lines


def replace_block(content, start, end, block):
    start_idx = content.find(start)
    end_idx = content.find(end)
    if start_idx == -1 or end_idx == -1:
        print(f"error: markers {start} not found in readme.md", file=sys.stderr)
        sys.exit(1)
    return content[:start_idx] + block + content[end_idx + len(end):]


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

    repos_block = "\n".join([REPOS_START, *build_repo_table(all_items), REPOS_END])

    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    new_content = replace_block(content, START_MARKER, END_MARKER, block)
    new_content = replace_block(new_content, REPOS_START, REPOS_END, repos_block)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    main()
