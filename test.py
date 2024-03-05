import unittest
from unittest.mock import patch, Mock


class TestGitHubAPI(unittest.TestCase):

    @patch('GitHub_API.requests.get')
    def test_get_user_repo_commits(self, mock_requests_get):
        # Prepare a mock response for the repositories API
        repositories_response = Mock()
        repositories_response.json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        # Prepare a mock response for the commits API
        commits_response = Mock()
        commits_response.json.return_value = [{'commit': {'message': 'Commit 1'}}, {'commit': {'message': 'Commit 2'}}]

        # Set the side effect to return different responses for each call
        mock_requests_get.side_effect = [repositories_response, commits_response]


if __name__ == '__main__':
    unittest.main()
