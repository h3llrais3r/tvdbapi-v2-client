# coding: utf-8

import unittest

from tvdb_api.client import TvdbClient
from tvdb_api.models.episode import Episode
from tvdb_api.rest import ApiException


class TestClientEpisodes(unittest.TestCase):
    """Client episodes unit tests."""

    def setUp(self):
        self.client = TvdbClient()
        self.client.login()

    def tearDown(self):
        self.client.clear_token()
        pass

    def test_get_episode(self):
        response = self.client.get_episode(5255064)
        # asserts
        self.assertIsNotNone(response)
        self.assertIsInstance(response, Episode)
        self.assertTrue(response.series_id == '296295')
        self.assertTrue(response.aired_season == 1)
        self.assertTrue(response.aired_episode_number == 1)

    def test_get_episode_401(self):
        self.client.clear_token()
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_episode(5255064)
        self.assertTrue(e.exception.status == 401)

    def test_get_episode_404(self):
        # asserts
        with self.assertRaises(ApiException) as e:
            self.client.get_episode(0)
        self.assertTrue(e.exception.status == 404)


if __name__ == '__main__':
    unittest.main()
