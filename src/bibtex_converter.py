import reference_database

def book_to_bibtex(id):
    book = reference_database.get_book(id)
    bibtex = f'@book{{{book[0]}, author = \"{book[1]}\", title = \"{book[2]}\", publisher = \"{book[3]}\", address = \"{book[4]}\", year = {book[5]}}}'
    return bibtex