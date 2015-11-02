import unittest
import mock
import json
from pyramid import testing


from .mock_data import fake_data, fake_full_data
from search_artists.searcher import ArtistSearcher
from search_artists.loader import ArtistLoader
from search_artists.sorter import MedianSorter


class HomeViewTests(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest()

    def tearDown(self):
        testing.tearDown()

    def test_should_return_empty_dict(self):
        from search_artists.views import home

        response = home(self.request)

        self.assertEqual(response, dict())

searcher_module = 'search_artists.searcher.ArtistSearcher'
loader_module = 'search_artists.loader.ArtistLoader'


class SearchViewTests(unittest.TestCase):
    def create_patch(self, name, return_value=None):
        patcher = mock.patch(name)
        thing = patcher.start()
        thing.return_value = return_value
        self.addCleanup(patcher.stop)
        return thing

    def setUp(self):
        self.request = testing.DummyRequest()
        self.request.params['age'] = '10,20'
        self.create_patch('%s.__init__' % loader_module)
        mock_data = self.create_patch('%s.data' % loader_module)
        mock_data.__get__ = mock.Mock(return_value=fake_full_data)

    def tearDown(self):
        testing.tearDown()

    def test_should_parse_the_params_and_call_the_search(self):
        from search_artists.views import search
        searcher_mock = self.create_patch(
            '%s.search_by_age' % searcher_module,
            return_value=fake_data)

        response = search(self.request)

        searcher_mock.assert_called_with(10, 20, sorterKlass=MedianSorter)

    def test_response_dict(self):
        from search_artists.views import search
        searcher_mock = self.create_patch(
            '%s.search_by_age' % searcher_module,
            return_value=fake_data)

        response = search(self.request)

        self.assertEqual(response, {
            'artists': fake_data,
            'artists_json': json.dumps(fake_data, indent=4),
            'minAge': 10,
            'maxAge': 20
            })
