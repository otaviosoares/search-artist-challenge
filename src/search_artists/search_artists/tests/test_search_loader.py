import unittest
import mock
from search_artists.loader import ArtistLoader
from .mock_data import fake_json

json_path = 'artists.json'


class LoaderTests(unittest.TestCase):
    def setUp(self):
        with mock.patch('__builtin__.open') as m:
            m.return_value.__enter__ = lambda s: s
            m.return_value.__exit__ = m.Mock()
            m.return_value.read.return_value = fake_json
            self.mock = m
            self.artist_loader = ArtistLoader(json_path)

    def test_create_a_new_instance_of_Search(self):
        self.mock.assert_called_with(json_path)

    def test_should_retrieve_data_from_json_string(self):
        self.assertEqual(len(self.artist_loader.data), 7)
