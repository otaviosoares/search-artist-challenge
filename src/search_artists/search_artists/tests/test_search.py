import unittest
from .mock import fake_data


class CreatingSearchTests(unittest.TestCase):

    def test_create_a_new_instance_of_Search(self):
        from search_artists.search import Search
        search = Search([])
        self.assertIsInstance(search, Search)

    def test_should_fail_if_data_provided_is_not_type_list(self):
        from search_artists.search import Search
        with self.assertRaises(TypeError) as cm:
            search = Search('some string')
        exception = cm.exception
        self.assertEquals(exception.message, 'data should be of type list')


class SearchingTests(unittest.TestCase):
    def test_min_value_should_not_be_equal_or_lesser_than_zero(self):
        from search_artists.search import Search
        search = Search([])

        with self.assertRaises(ValueError) as cm:
            search.search(0, 5)
        exception = cm.exception

        error_message = 'min value can not be equal or less than 0'
        self.assertEquals(exception.message, error_message)

    def test_filter_the_data_based_on_provided_parameters(self):
        from search_artists.search import Search
        search = Search(fake_data)
        result = search.search(10, 15)
        self.assertEquals(len(result), 2)
