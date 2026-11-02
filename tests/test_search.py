import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.dvds = [
            DigitalVideoDisc(
                "The Lion King", "Animation",
                "Roger Allers", 87, 19.95
            ),
            DigitalVideoDisc(
                "Star Wars", "Science Fiction",
                "George Lucas", 87, 24.95
            )
        ]

    def test_search_by_title_case_insensitive(self):
        result = search_by_title(self.dvds, "lion")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].title, "The Lion King")

    def test_search_by_title_no_match(self):
        result = search_by_title(self.dvds, "Harry Potter")
        self.assertEqual(len(result), 0)


if __name__ == "__main__":
    unittest.main()