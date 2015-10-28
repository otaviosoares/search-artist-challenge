import unittest


fake_data = [
    {'age': 2}, {'age': 5}, {'age': 9}, {'age': 10},
    {'age': 15}, {'age': 16}, {'age': 20}]


class SearchTests(unittest.TestCase):

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

    def test_filter_the_data_based_on_provided_parameters(self):
        from search_artists.search import Search
        search = Search(fake_data)
        result = search.search(10, 15)
        self.assertEquals(len(result), 2)
