#!/usr/bin/env python3
"""
Unit tests for client module
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""

    @parameterized_class([{
        "org_payload": {"repos_url": "http://repos.url"},
        "repos_payload": [{"name": "repo1"}],
        "expected_repos": ["repo1"],
        "apache2_repos": [{"name": "apache_repo1"}],
    }])
    class TestIntegrationGithubOrgClient(unittest.TestCase):
        """Integration test class"""

        @classmethod
        def setUpClass(cls, **kwargs):
            """Set up the test class"""
            cls.get_patcher = patch('requests.get')
            cls.mock_get = cls.get_patcher.start()

            cls.mock_get.side_effect = [
                Mock(json=lambda: cls.org_payload),
                Mock(json=lambda: cls.repos_payload),
                Mock(json=lambda: cls.apache2_repos),
            ]

        @classmethod
        def tearDownClass(cls):
            """Tear down the test class"""
            cls.get_patcher.stop()

        @patch('client.GithubOrgClient.org', return_value="http://repos.url")
        def test_public_repos(self, mock_org):
            """Test public_repos method"""
            client = GithubOrgClient("test_org")
            self.assertEqual(client.public_repos(), self.expected_repos)

        @patch('client.GithubOrgClient.org', return_value="http://repos.url")
        def test_public_repos_with_license(self, mock_org):
            """Test public_repos method with license argument"""
            client = GithubOrgClient("test_org")
            self.assertEqual(
                    client.public_repos(license="apache-2.0"),
                    self.apache2_repos
                    )


if __name__ == "__main__":
    unittest.main()
