"""
This file contains code utilizing a REST-based API that takes in a user's GitHub 
user ID and output's a list of the names of the repositories the user has along 
with number of commits that are in each of the repositories. 
Functions: get_user_repo_commits
Libraries used: requests, json
"""
import requests
import json


def get_user_repo_commits(user_id):
    """
    Prints the the user's repositories and commits in each repository. 
    If the response status code when fetching the user's repositories
    is not 200, an error message is displayed. Else, iterate through each
    repository. If the response status code when fetching the user's 
    repository's commits is not 200, an error message is displayed. Else, 
    the repository and number of commits is displayed on a single line.
    Args:
        user_id: string value of the user's GitHub ID
    Returns:
        N/A
    Raises:
        N/A
    """
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

