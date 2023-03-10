import sys
import json
from datetime import datetime, timedelta
from collections import defaultdict, namedtuple
from urllib.request import urlopen, Request


Commit = namedtuple("Commit", ["hash", "timestamp"])


def get_commit_to_run_map(repo_name: str, username: str, github_token: str):
    three_days_ago = datetime.now() - timedelta(days=3)

    url = f"https://api.github.com/repos/embodiedintelligence/{repo_name}/actions/runs?actor={username}&created=>{three_days_ago.date()}"
    url = f"https://api.github.com/repos/embodiedintelligence/{repo_name}/actions/runs?actor={username}"

    httprequest = Request(url, headers={"Authorization": f"Bearer {github_token}"})

    with urlopen(httprequest) as response:
        response_json = json.loads(response.read().decode())

    hash_to_workflows = defaultdict(list)
    for workflow_run in response_json["workflow_runs"]:
        commit = Commit(hash=workflow_run["head_commit"]["id"], timestamp=datetime.strptime(workflow_run["head_commit"]["timestamp"],'%Y-%m-%dT%H:%M:%SZ'))
        hash_to_workflows[commit].append(workflow_run)

    return hash_to_workflows

def get_pr_to_runs_map(repo_name: str, username: str, github_token: str, commit_to_runs_map: dict):
    pr_to_commits = defaultdict(list)

    for commit in commit_to_runs_map.keys():
        url = f"https://api.github.com/repos/embodiedintelligence/{repo_name}/commits/{commit.hash}/pulls"
        httprequest = Request(url, headers={"Authorization": f"Bearer {github_token}"})

        with urlopen(httprequest) as response:
            response_json = json.loads(response.read().decode())

        for pr in response_json:
            if pr["user"]["login"] != username:
                continue
            pr_to_commits[pr["number"]].append(commit)

    pr_to_runs = {}
    for pr, commits in pr_to_commits.items():
        latest_commit = sorted(commits, key=lambda c: c.timestamp)[0]
        pr_to_runs[pr] = commit_to_runs_map[latest_commit]

    pr_to_runs = dict(sorted(pr_to_runs.items(), key=lambda k_v: int(k_v[0])))

    return pr_to_runs


def generate_statusline(pr_to_runs_map: dict):
    pr_statuses = []
    for pr, runs in pr_to_runs_map.items():
        pr_status = ""
        pr_status += f"PR {pr}: "
        successes = 0
        failures = 0
        pending = 0
        other = 0
        for run in runs:
            if run["status"] != "completed":
                pending += 1
                continue
            if run["conclusion"] == "success":
                successes += 1
            elif run["conclusion"] == "failure":
                failures += 1
            else:
                other += 1
        statuses = []
        if successes > 0:
            statuses.append(f"{successes} ✅")
        if failures > 0:
            statuses.append(f"{failures} ❌")
        if pending > 0:
            statuses.append(f"{pending} ⏳")
        if other > 0:
            statuses.append(f"{other} ❓")
        pr_status += ", ".join(statuses)
        pr_statuses.append(pr_status)

    print(" | ".join(pr_statuses))

if __name__ == "__main__":
    github_repo = sys.argv[1]
    github_username = sys.argv[2]
    github_token = sys.argv[3]

    commit_to_runs_map = get_commit_to_run_map(github_repo, github_username, github_token)
    pr_to_runs_map = get_pr_to_runs_map(github_repo, github_username, github_token, commit_to_runs_map)
    generate_statusline(pr_to_runs_map)
