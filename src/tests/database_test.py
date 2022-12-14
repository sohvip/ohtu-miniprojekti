import unittest
import reference_database
from bibtex_converter import *

class Testreference_database(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_book(self):
        reference_database.empty_books()
        reference_database.create_book("munkirja1", "Esko Nieminen", "Timo", "Jussin elämänkerta", 1, 2019)
        books = reference_database.get_books()
        length = len(books)
        reference_database.empty_books()
        self.assertEqual(length, 1)

    def test_create_misc(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier61", "My Life", "Jane Doe", "www.lifestory.com", 2007, 5)
        sites = reference_database.get_table_misc_raw()
        length = len(sites)
        reference_database.empty_misc()
        self.assertEqual(length, 1)
    
    def test_book_can_be_found_with_tag(self):
        reference_database.empty_books()
        reference_database.create_book("ekakirja10", "Jussi Nieminen", "Simo", "Jussin elämänkerta", 13, 2009)
        tag_id = reference_database.get_tag_id("testi")
        reference_database.add_tag_to_work("ekakirja10", tag_id)
        book_list = reference_database.list_books_by_tag("testi")
        identifier = book_list[0][0]
        reference_database.empty_books()
        self.assertEqual(identifier, "ekakirja10")

    def test_misc_can_be_found_with_tag(self):
        reference_database.empty_misc()
        reference_database.create_misc("ekasivu01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", 13, 2009)
        tag_id = reference_database.get_tag_id("tagEKA")
        reference_database.add_tag_to_work("ekasivu01", tag_id)
        book_list = reference_database.list_misc_by_tag("tagEKA")
        identifier = book_list[0][0]
        reference_database.empty_misc()
        self.assertEqual(identifier, "ekasivu01")

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
        reference_database.empty_misc()
        reference_database.create_misc("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", 13, 2009)
        reference_database.create_misc("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", 10, 2002)
        misc_list = reference_database.list_misc_by_author_name()
        first_misc_author = misc_list[1][1]
        second_misc_author = misc_list[1][1]
        reference_database.empty_misc()
        self.assertEqual(first_misc_author, "Aapeli Koistinen")
        #self.assertEqual(second_misc_author, "Jussi Nieminen")
    
    def test_list_miscs_by_time_added(self):
        reference_database.empty_misc()
        reference_database.create_misc("ekaweb700", "Jussi Nieminen", "Simo", "Jussin elämänkerta", 13, 2009)
        reference_database.create_misc("tokaweb900", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", 10, 2002)
        misc_list = reference_database.list_misc_by_time_added()
        first_misc_id = misc_list[0][0]
        reference_database.empty_misc()
        self.assertEqual(first_misc_id, "ekaweb700")

    def test_list_books_by_time_added(self):
        reference_database.empty_books()
        reference_database.create_book("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", "Simon julkaisut", 2009)
        reference_database.create_book("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", "Simon julkaisut", 2002)
        book_list = reference_database.list_books_by_time_added()
        first_book_id = book_list[0][0]
        reference_database.empty_books()
        self.assertEqual(first_book_id, "ekakirja01")

    def test_identifier_exists_book(self):
        reference_database.empty_books()
        reference_database.create_book("testID", "Jimbo Simo", "bestEditor", "Ocean Story", "BestPublisher", 2010)
        identifier_exists = reference_database.identifier_already_exists_books("testID")
        reference_database.empty_books()
        self.assertEqual(identifier_exists, True)

    def test_identifier_does_not_exist_book(self):
        reference_database.empty_books()
        reference_database.create_book("testID", "Jimbo Simo", "bestEditor", "Ocean Story", "BestPublisher", 2010)
        identifier_does_not_exist = reference_database.identifier_already_exists_books("test1")
        reference_database.empty_books()
        self.assertEqual(identifier_does_not_exist, False)

    def test_identifier_exists_misc(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier1", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        identifier_exists = reference_database.identifier_already_exists_misc("identifier1")
        reference_database.empty_misc()
        self.assertEqual(identifier_exists, True)

    def test_identifier_does_not_exist_misc(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier3", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        identifier_exists = reference_database.identifier_already_exists_misc("identifier1")
        reference_database.empty_misc()
        self.assertEqual(identifier_exists, False)
    
    def test_get_website_id(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier1", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        for id in range(10000):
            website = reference_database.get_website(id)
            if website is not None:
                break
        reference_database.empty_misc()
        self.assertEqual(str(website[0]), "identifier1")

    def test_get_book_id(self):
        reference_database.empty_books()
        reference_database.create_book("testID", "Jimbo Simo", "bestEditor", "Ocean Story", "BestPublisher", 2010)
        for id in range(10000):
            book = reference_database.get_book(id)
            if book is not None:
                break
        reference_database.empty_misc()
        self.assertEqual(str(book[0]), "testID")

    def test_delete_book(self):
        reference_database.empty_books()
        reference_database.create_book("testID", "Jimbo Simo", "bestEditor", "Ocean Story", "BestPublisher", 2010)
        for id in range(10000):
            book = reference_database.get_book(id)
            book_id = id
            if book is not None:
                break
        book_exists = reference_database.get_book(book_id)
        reference_database.delete_book(book_id)
        book__does_not_exist = reference_database.get_book(book_id)
        reference_database.empty_misc()
        self.assertEqual(str(book_exists[0]), "testID")
        self.assertEqual(book__does_not_exist, None)

    def test_delete_misc(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier1", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        for id in range(10000):
            website = reference_database.get_website(id)
            website_id = id
            if website is not None:
                break
        website_exists = reference_database.get_website(website_id)
        reference_database.delete_website(website_id)
        website_does_not_exist = reference_database.get_book(website_id)
        reference_database.empty_misc()
        self.assertEqual(str(website_exists[0]), "identifier1")
        self.assertEqual(website_does_not_exist, None)

    def test_does_not_create_book_if_identifier_exists(self):
        reference_database.empty_books()
        reference_database.create_book("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", "Simon julkaisut", 2002)
        return_value = reference_database.create_book("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", "Simon julkaisut", 2002)
        reference_database.empty_books()
        self.assertEqual(return_value, "Identifier already in use for another work")
    
    def test_does_not_create_website_if_identifier_exists(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier100", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        return_value = reference_database.create_misc("identifier100", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        reference_database.empty_misc()
        self.assertEqual(return_value, "Identifier already in use for another work")

    def test_get_book_size_(self):
        reference_database.empty_books()
        reference_database.create_book("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", "Simon julkaisut", 2009)
        reference_database.create_book("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", "Simon julkaisut", 2002)
        book_size = reference_database.books_size()
        reference_database.empty_books()
        self.assertEqual(str(book_size[0]), "2")
    
    def test_get_misc_identifiers(self):
        reference_database.empty_misc()
        reference_database.create_misc("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", 13, 2009)
        reference_database.create_misc("tokakirja02", "Aapeli Koistinen", "Simo", "Aapelin elämänkerta", 10, 2002)
        misc_list = reference_database.get_identifiers_dict()
        identifiers = list(misc_list.values())[0]
        #second_misc = misc_list[2]
        reference_database.empty_misc()
        #self.assertEqual(second_misc, "tokakirja02")
        self.assertEqual(identifiers, ['ekakirja01', 'tokakirja02'])
    
    def test_book_to_bibtext(self):
        reference_database.empty_books()
        reference_database.create_book("ekakirja01", "Jussi Nieminen", "Simo", "Jussin elämänkerta", "Simon julkaisut", 2009)
        for id in range(10000):
            book = reference_database.get_book(id)
            book_id = id
            if book is not None:
                break
        bibtext = book_to_bibtex(book_id)
        reference_database.empty_books()
        self.assertEqual(str(bibtext[:42]), "@book{ekakirja01, author = \"Jussi Nieminen")

    def test_website_to_bibtext(self):
        reference_database.empty_misc()
        reference_database.create_misc("identifier100", "Life", "Jane Doe", "www.lifebook.com", 2001, 5)
        for id in range(10000):
            website = reference_database.get_website(id)
            website_id = id
            if website is not None:
                break
        bibtext = website_to_bibtex(website_id)
        reference_database.empty_misc()
        self.assertEqual(str(bibtext[:43]), "@misc{identifier100, title = \"Life\", author")



    def tearDown(self):
        reference_database.empty_all_tables()
