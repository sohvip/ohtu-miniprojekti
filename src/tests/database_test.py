import unittest
import reference_database


class Testreference_database(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_book(self):
        reference_database.empty_books()
        reference_database.create_book("test", "toka", 9, 9, 9, 9)
        books = reference_database.get_books()
        length = len(books)
        reference_database.empty_books()
        self.assertEqual(length, 1)
    
    def test_create_misc(self):
        reference_database.empty_misc()
        reference_database.create_misc("test", "toka", 9, 9, 9, 9)
        sites = reference_database.get_table_misc_raw()
        length = len(sites)
        reference_database.empty_misc()
        self.assertEqual(length, 1)

    def test_identifier_exists_book(self):
        reference_database.empty_books()
        reference_database.create_book("test", "eka", 9, 9, 9, 9)
        identifier_exists = reference_database.identifier_already_exists_books("test")
        identifier_does_not_exist = reference_database.identifier_already_exists_books("test1")
        self.assertEqual(identifier_exists, True)
        self.assertEqual(identifier_does_not_exist, False)

    def test_does_not_create_book_if_identifier_exists(self):
        reference_database.empty_books()
        reference_database.create_book("test", "toka", 9, 9, 9, 9)
        return_value = reference_database.create_book("test", "eka", 9, 9, 9, 9)
        self.assertEqual(return_value, "Identifier already in use for another work")


