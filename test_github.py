import pytest
from Get_GitHub_Commits import get_user_repo_commits

def test_user_github_commits(capsys):
    user_id='sidhdhuk09'
    get_user_repo_commits(user_id)
    out,err=capsys.readouterr()
    assert "Repo:" in out, "Output should list all repos"
    assert "Number of commits:" in out, "Output should list the number of commits"

def test_invalid_user(capsys):
    user_id=' nonexistent_user'
    get_user_repo_commits(user_id)
    out,err=capsys.readouterr()
    assert "Error" in out, "Output should indicate an error for invalid or nonexisting user"

def test_user_with_no_repos(capsys):
    user_id='tushar2808'
    get_user_repo_commits(user_id)
    out ,err=capsys.readouterr()
    assert out == "", "Expected no output for a user with no repositories or a non-existent user"
