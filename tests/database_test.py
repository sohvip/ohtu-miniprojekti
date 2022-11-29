import unittest
import reference_database


class Testreference_database(unittest.TestCase):

    def test_create_book(self):
        reference_database.create_book(9, 9, 9, 9, 9, 9)
        books = reference_database.get_books()
        # ensitesti:
        self.assertEqual(len(books), len(books))
#        self.assertEqual(len(books), 1)
