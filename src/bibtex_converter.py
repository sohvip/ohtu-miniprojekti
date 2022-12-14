import reference_database

def book_to_bibtex(id):
    book = reference_database.get_book(id)
    bibtex = f'@book{{{book[0]}, author = \"{book[1]}\", editor = \"{book[2]}\", title = \"{book[3]}\", publisher = \"{book[4]}\", year = {book[5]}}}'
    return bibtex

def website_to_bibtex(id):
    website = reference_database.get_website(id)
    bibtex = f'@misc{{{website[0]}, title = \"{website[1]}\", author = \"{{{website[2]}}}\", howpublished = \"url{{{website[3]}}}\", year = {website[4]}, note = \"{website[5]}\"}}'
    bibtex = bibtex.replace('url', '\\url')
    return bibtex
