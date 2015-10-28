import unittest
from search_artists.searcher import ArtistSearcher
from .mock import fake_data


class CreatingSearchTests(unittest.TestCase):

    def test_create_a_new_instance_of_Search(self):
        searcher = ArtistSearcher([])
        self.assertIsInstance(searcher, ArtistSearcher)

    def test_should_fail_if_data_provided_is_not_type_list(self):
        with self.assertRaises(TypeError) as cm:
            searcher = ArtistSearcher('some string')
        exception = cm.exception
        self.assertEquals(exception.message, 'data should be of type list')


class SearchingTests(unittest.TestCase):
    def setUp(self):
        self.searcher = ArtistSearcher(fake_data)

    def test_min_value_should_not_be_equal_or_lesser_than_zero(self):

        with self.assertRaises(ValueError) as cm:
            self.searcher.search_by_age(0, 5)
        exception = cm.exception

        error_message = 'min age can not be equal or less than 0'
        self.assertEquals(exception.message, error_message)

    def test_max_value_should_not_be_less_than_min_value(self):
        with self.assertRaises(ValueError) as cm:
            self.searcher.search_by_age(50, 5)
        exception = cm.exception

        error_message = 'max age can not be greater min age'
        self.assertEquals(exception.message, error_message)

    def test_filter_the_data_based_on_provided_parameters(self):
        result = self.searcher.search_by_age(10, 15)
        self.assertEquals(len(result), 2)
