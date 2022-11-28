import reference_database

def get_books_human_readable():
    list = reference_database.get_books_raw()
    book_list = []

    i = 0
    while list[i] is not None:
        add = "Book, identifier: ", list[i][0] + '\n' + list[i][3] + " by " + list[i][1] + '\n' + list[i][4] + ", " + list[i][2] + '\n'

        book_list.append(add)



    return book_list
