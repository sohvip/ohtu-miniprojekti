import unittest
from db import db
import reference_database

class Testreference_database(unittest.TestCase):

    def test_testi(self):
        books_size = reference_database.books_size()
        reference_database.create_book(9, 9, 9, 9, 9, 9)
        reference_database.create_book(9, 9, 9, 9, 9, 9) # shouldn't be added

        self.assertEqual(reference_database.books_size(), books_size + 1)