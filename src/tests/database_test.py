import unittest
import reference_database


class Testreference_database(unittest.TestCase):

    def test_create_book(self):
        reference_database.empty_books()
        reference_database.create_book("test", "toka", 9, 9, 9, 9)
        books = reference_database.get_books()
        length = len(books)
        reference_database.empty_books()
        self.assertEqual(length, 1)
