import reference_database


def book_to_bibtex(id):
    book = reference_database.get_book(id)
    bibtex = f'@book{{{book[0]}, author = \"{book[1]}\", editor = \"{book[2]}\", title = \"{book[3]}\", publisher = \"{book[4]}\", year = {book[5]}}}'
    return bibtex
