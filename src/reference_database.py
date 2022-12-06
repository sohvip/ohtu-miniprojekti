'''Handles database operations'''
from db import db


def create_misc(identifier, title, editor, how_published, year, note): # create website
    '''
    Inserts into misc table, checks that identifier is not already in use
    RETURNS string describing how the insertion went
    '''

    if identifier_already_exists(identifier):
        return "Identifier already in use for another work"

    sql = "INSERT INTO misc (ref_type, identifier, title, editor, how_published, year, note)"\
        " VALUES (:misc, :id, :title, :edit, :how_published, :year, :note)"

    db.session.execute(sql, {"misc":"misc", "id":identifier, "title":title, "edit":editor,
                             "how_published":how_published, "year":year, "note":note})
    db.session.commit()

    return "Misc (website) created successfully"


def create_book(identifier, author, editor, title, publisher, year):
    '''
    Inserts into books table, checks that identifier is not already in use
    RETURNS string describing how the insertion went
    '''

    if identifier_already_exists(identifier):
        return "Identifier already in use for another work"

    # book_exists = already_exists_book()
    # if book_exists is not None:
    #     return "Identicial book already exists already with identifier " + book_exists


    sql = "INSERT INTO books (ref_type, identifier, author, editor, title, publisher, year)"\
        " VALUES (:book, :id, :auth, :edit, :title, :publ, :year)"
    db.session.execute(sql, {"book":"book", "id":identifier, "auth":author, "edit":editor,
                             "title":title, "publ":publisher, "year":year})
    db.session.commit()

    return "Book created successfully"

def identifier_already_exists(identifier):
    '''
    Checks all tables for argumented identifier,
    RETURNS True if identifier exists in any table
    '''

    if identifier_already_exists_books(identifier):
        return True
    if identifier_already_exists_misc(identifier):
        return True

    return False

def identifier_already_exists_books(identifier):
    '''
    Called by "parent" function identifier_already_exists(), checks table books
    RETURNS True if identifier is used in this table
    '''

    sql = "SELECT * FROM books WHERE identifier=:id"
    result = db.session.execute(sql, {"id":identifier})
    result = result.fetchone()

    if result:
        return True

    return False

def identifier_already_exists_misc(identifier):
    '''
    Called by "parent" function identifier_already_exists(), checks table misc
    RETURNS True if identifier is used in this table
    '''

    sql = "SELECT * FROM misc WHERE identifier=:id"
    result = db.session.execute(sql, {"id":identifier})
    result = result.fetchone()

    if result:
        return True

    return False


def get_books():
    sql = "SELECT identifier, author, editor, title, publisher, year, id FROM books"
    result = db.session.execute(sql)
    result = result.fetchall()
    return result

def get_book(id):
    sql = "SELECT identifier, author, editor, title, publisher, year FROM books WHERE id=:id"
    result = db.session.execute(sql, {'id':id})
    result = result.fetchone()
    return result

def get_table_misc_raw():
    sql = "SELECT identifier, title, editor, how_published, year, note, id FROM misc"
    result = db.session.execute(sql)
    result = result.fetchall()
    return result


# aux

def books_size():
    sql = "SELECT COUNT(*) FROM books"
    result = db.session.execute(sql)

    return result.fetchone()

def empty_books():
    sql = "DELETE FROM books"
    db.session.execute(sql)

def get_website(id):
    sql = "SELECT identifier, title, editor, how_published, year, note FROM misc WHERE id=:id"
    result = db.session.execute(sql, {'id':id})
    result = result.fetchone()
    return result

def empty_misc():
    sql = "DELETE FROM misc"
    db.session.execute(sql)
