'''Parses database data to desired forms'''
import reference_database

def get_books_human_readable():
    '''
    Parses raw book data to human readable form
    RETURNS list of parsed strings
    '''
    raw_list = reference_database.get_books_raw()
    book_list = []

    i = 0
    while i < reference_database.books_size()[0]:
        add = "Book, identifier: " + raw_list[i][0] + '\n' + raw_list[i][3] + " by " + raw_list[i][1] + '\n' + raw_list[i][4] + ", " + raw_list[i][2] + '\n'

        book_list.append(add)
        i += 1



    return book_list