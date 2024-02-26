import requests
import json


def get_user_repo_commits(user_id):
    # GitHub API endpoint for user repositories
    repo_url = f'https://api.github.com/users/{user_id}/repos'

    try:
        # Make a request to the GitHub API to get user repositories
        repo_response = requests.get(repo_url)
        repo_response.raise_for_status()  # Raise an HTTPError for bad responses

        repositories = repo_response.json()

        # Iterate over user repositories
        for repo in repositories:
            repo_name = repo['name']
            commits_url = f'https://api.github.com/repos/{user_id}/{repo_name}/commits'

            try:
                # Make a request to the GitHub API to get commits for the repository
                commits_response = requests.get(commits_url)
                commits_response.raise_for_status()  # Raise an HTTPError for bad responses

                commits = commits_response.json()
                num_commits = len(commits)

                print(f'Repo: {repo_name} Number of commits: {num_commits}')

            except requests.exceptions.RequestException as commits_error:
                print(f'Error fetching commits for repository {repo_name}: {commits_error}')

    except requests.exceptions.RequestException as repo_error:
        print(f'Error fetching repositories for user {user_id}: {repo_error}')

