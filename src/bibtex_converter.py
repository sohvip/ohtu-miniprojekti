from reference_database import get_book

def book_to_bibtex(id):
    book = get_book(id)
    bibtex = f'@book{{{book[0]}, author = \"{book[1]}\", editor = \"{book[2]}\", title = \"{book[3]}\", publisher = \"{book[4]}\", year = {book[5]}}}'
    return bibtex

# def website_to_bibtex(id):
#     website = get_website(id)
#     bibtex = ''
#     return bibtex