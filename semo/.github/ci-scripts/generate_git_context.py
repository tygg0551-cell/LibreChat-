import argparse
import os
import subprocess
import sys
import json
import requests

from helpers import log

def run_command(cmd):
    proc = subprocess.run(cmd, shell=True, text=True, capture_output=True)

    if proc.returncode != 0:
        log(f"Failed to run command: {cmd}", "error")
        log(f"{proc.stderr}", "error")
        sys.exit(proc.returncode)

    return proc.stdout.strip()

def find_last_successful_run(token, workflow_file_name):
    repo = os.environ.get("GITHUB_REPOSITORY")
    current_run_id = os.environ.get("GITHUB_RUN_ID")
    branch = os.environ.get("GITHUB_REF_NAME")

    if not all([repo, current_run_id, branch]):
        log("Missing required GitHub environment variables", "error")
        return None

    api_url = f"https://api.github.com/repos/{repo}/actions/workflows/{workflow_file_name}/runs"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {
        "branch": branch,
        "status": "success",
        "per_page": 100
    }

    try:
        log(f"Querying GitHub API for workflow runs: {api_url}", "info")

        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()

        runs = response.json().get("workflow_runs", [])
        log(f"Found {len(runs)} successful workflow runs", "info")

        # Filter out the current run
        runs = [run for run in runs if str(run["id"]) != current_run_id]

        if not runs:
            log("No previous successful runs found", "info")
            return None

        # Sort runs by created_at in descending order
        runs.sort(key=lambda run: run["created_at"], reverse=True)

        # Get the most recent successful run
        last_successful_run = runs[0]
        log(f"Last successful run: #{last_successful_run['run_number']} on {last_successful_run['created_at']}", "info")

        return last_successful_run["head_sha"]

    except requests.exceptions.RequestException as e:
        log(f"Failed to query GitHub API: {e}", "error")
        return None
    except (KeyError, IndexError, json.JSONDecodeError) as e:
        log(f"Failed to parse API response: {e}", "error")
        return None

def get_commit_range(last_successful_sha):
    current_sha = os.environ.get("GITHUB_SHA", "HEAD")

    if not last_successful_sha:
        log("No last successful SHA found, using fallback", "warning")
        before_sha = os.environ.get("GITHUB_EVENT_BEFORE")
        if before_sha and before_sha != "0" * 40:  # Check if before_sha is valid
            commit_range = f"{before_sha}..{current_sha}"
        else:
            # Default to looking at just the last commit
            commit_range = f"{current_sha}~1..{current_sha}"
    else:
        commit_range = f"{last_successful_sha}..{current_sha}"

    return commit_range

def write_to_github_env(name, value):
    with open(os.environ["GITHUB_ENV"], "a") as env_file:
        env_file.write(f"{name}={value}\n")

def write_multiline_to_github_env(name, value):
    with open(os.environ["GITHUB_ENV"], "a") as env_file:
        env_file.write(f"{name}<<EOF\n")
        env_file.write(value + "\n")
        env_file.write("EOF\n")

def add_to_logs(message):
    log_dir = os.path.join(os.environ["GITHUB_WORKSPACE"], "github_action_logs")
    os.makedirs(log_dir, exist_ok=True)

    with open(os.path.join(log_dir, "all.log"), "a") as log_file:
        log_file.write(message + "\n")

def main():
    log("Starting to prepare Git context...", "info")

    parser = argparse.ArgumentParser(description='Prepare Git context for GitHub Actions')
    parser.add_argument('--token', required=True, help='GitHub token')
    parser.add_argument('--workflow-file-name', default='deploy.yml', help='Workflow file name (default: deploy.yml)')
    args = parser.parse_args()

    # Find the last successful run
    log("Finding last successful run...", "info")
    last_successful_sha = find_last_successful_run(args.token, args.workflow_file_name)

    if last_successful_sha:
        log(f"Last successful commit SHA: {last_successful_sha}", "info")

    # Get commit range
    log("Determining commit range...", "info")
    commit_range = get_commit_range(last_successful_sha)
    log(f"Using commit range: {commit_range}", "info")

    # Get commit info
    log("Retrieving commit information...", "info")
    commit_info = run_command(f'git log "{commit_range}" --pretty=format:"Commit: %H%nAuthor: %an%nMessage: %s%n"')
    log(f"Commit information retrieved:\n{commit_info}", "info")

    # Write commit info to a file
    commit_info_file_path = os.path.join(os.environ["GITHUB_WORKSPACE"], "commit_info.txt")
    with open(commit_info_file_path, "w") as commit_info_file:
        commit_info_file.write(commit_info)
    log(f"Commit info written to {commit_info_file_path}", "info")

    # Get diff
    log("Retrieving diff information...", "info")
    diff = run_command(f'git diff "{commit_range}"')
    log(f"Diff information retrieved.", "info")

    # Write diff to a file
    diff_file_path = os.path.join(os.environ["GITHUB_WORKSPACE"], "diff.txt")
    with open(diff_file_path, "w") as diff_file:
        diff_file.write(diff)
    log(f"Diff written to {diff_file_path}", "info")

    # Set environment variables
    log("Setting environment variables...", "info")
    write_to_github_env("COMMIT_RANGE", commit_range)
    write_multiline_to_github_env("COMMIT_INFO_FILE", commit_info_file_path)
    write_to_github_env("DIFF_FILE", diff_file_path) # Output path to diff file
    log("Environment variables are set.", "info")

    # Log everything
    log("Adding commit information and diff to logs...", "info")
    log_message = f"""
Commit Range: {commit_range}

Commit Info:
{commit_info}

Diff is stored in: {diff_file_path}
"""
    add_to_logs(log_message)
    log("Commit information and diff added to logs.", "info")

    log("Git context preparation completed.", "success")

if __name__ == "__main__":
    main()