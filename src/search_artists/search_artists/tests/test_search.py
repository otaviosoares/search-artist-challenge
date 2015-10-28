import unittest


class SearchTests(unittest.TestCase):

    def test_create_a_new_instance_of_Search(self):
        from search_artists.search import Search
        search = Search()
        self.assertIsInstance(search, Search)
