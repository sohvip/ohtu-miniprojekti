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
    
    def test_book_can_be_found_with_tag(self):
        reference_database.empty_books()
        reference_database.create_book("testbook", "eka", 9, 9, 9, 9)
        tag_id = reference_database.get_tag_id("testi")
        reference_database.add_tag_to_work("testbook", tag_id)
        book_list = reference_database.list_books_by_tag("testi")
        identifier = book_list[0][0]
        reference_database.empty_books()
        self.assertEqual(identifier, "testbook")

    def test_list_books_by_author_name_(self):
        reference_database.empty_books()
        reference_database.create_book("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", "Simon julkaisut", 2009)
        reference_database.create_book("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", "Simon julkaisut", 2002)
        book_list = reference_database.list_books_by_author_name()
        first_book_author = book_list[0][1]
        second_book_author = book_list[1][1]
        reference_database.empty_books()
        self.assertEqual(first_book_author, "Aapeli Koistinen")
        self.assertEqual(second_book_author, "Jussi Nieminen")
    
    def test_list_miscs_by_author_name_(self):
        reference_database.empty_books()
        reference_database.create_misc("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", 13, 2009)
        reference_database.create_misc("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", 10, 2002)
        misc_list = reference_database.list_misc_by_author_name()
        first_book_author = misc_list[0][1]
        second_book_author = misc_list[1][1]
        reference_database.empty_books()
        self.assertEqual(first_book_author, "Aapeli Koistinen")
        self.assertEqual(second_book_author, "Jussi Nieminen")

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

    def tearDown(self):
        reference_database.empty_all_tables()
