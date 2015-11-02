import unittest
import json
from search_artists.searcher import ArtistSearcher
from .mock_data import fake_data


class OrderingTests(unittest.TestCase):
    def setUp(self):
        self.searcher = ArtistSearcher(fake_data)

    def test_should_not_order_if_not_told_to_do_so(self):
        result = self.searcher.search_by_age(1, 100)
        self.assertEquals(result, fake_data)

    def test_should_order_from_middle_to_edges(self):
        from search_artists.sorter import MedianSorter
        result = self.searcher.search_by_age(1, 100, sorterKlass=MedianSorter)

        expected = [{"age": 10}, {"age": 9}, {"age": 15},
                    {"age": 16}, {"age": 5}, {"age": 2},
                    {"age": 20}]
        self.assertEquals(result, expected)
