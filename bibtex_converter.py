from reference_database import get_book

def book_to_bibtex(identifier):
    book = get_book(identifier)
    bibtex = f'@book{{{book[0]}, author = \"{book[1]}\", title = \"{book[2]}\", publisher = \"{book[3]}\", address = \"{book[4]}\", year = {book[5]}}}'
    return bibtex