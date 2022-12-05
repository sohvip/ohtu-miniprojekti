'''Handles database operations'''
from db import db

def create_misc(identifier, title, editor, how_published, year, note): # create website

    if identifier_already_exists(identifier):
       return "Identifier already in use for another work"

    sql = "INSERT INTO misc (ref_type, identifier, author, editor, title, publisher, year)"\
        " VALUES (:misc, :id, :title, :edit, :how_published, :year, :note)"

    db.session.execute(sql, {"misc":"misc", "id":identifier, "title":title, "edit":editor,
                             "how_published":how_published, "year":year, "note":note})
    db.session.commit()

    return "Miscin isääminen onnistui"


def create_book(identifier, author, editor, title, publisher, year):
    '''
    Inserts into books table, checks that identifier is not already in use and
    that the added book is not a duplicate
    RETURNS string describing how the insertion went
    '''

    if identifier_already_exists(identifier):
       return "Identifier already in use for another work"

    # book_exists = already_exists_book()
    # if book_exists is not None:
    #     return "Identicial book already exists already with identifier " + book_exists


    sql = "INSERT INTO books (ref_type, identifier, author, editor, title, publisher, year) VALUES (:book, :id, :auth, :edit, :title, :publ, :year)"
    db.session.execute(sql, {"book":"book", "id":identifier, "auth":author, "edit":editor, "title":title, "publ":publisher, "year":year})
    db.session.commit()

    return "Bookin lisääminen onnistui"

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
    Called by "parent" function identifier_already_exists, checks table books
    RETURNS True if exists
    '''
    
    sql = "SELECT * FROM books WHERE identifier=:id"
    result = db.session.execute(sql, {"id":identifier})
    result = result.fetchone()

    if result:
        return True

    return False

def identifier_already_exists_misc(identifier):

    sql = "SELECT * FROM misc WHERE identifier=:id"
    result = db.session.execute(sql, {"id":identifier})
    result = result.fetchone()

    if result:
        return True

    return False

def already_exists_book(author, editor, title, publisher, year):
    '''
    Checks table books if a book with argumented attributes exists, if exists
    RETURN identifier
    '''

    sql = "SELECT identifier FROM books WHERE author=:a, editor=:e, title=:t, publisher=:p, year=:y"
    result = db.session.execute(sql, {"a":author, "e":editor, "t":title, "p":publisher, "y":year})
    result = result.fetchone()[0]

    if result is not None:
        return result

    return None

def get_books_raw():
    '''
    RETRUNS table books as a raw version, parsing done elsewhere
    '''

    sql = "SELECT identifier, author, editor, title, publisher, year FROM books"
    result = db.session.execute(sql)
    return result.fetchall()

def get_books():
    sql = "SELECT identifier, author, editor, title, publisher, year FROM books"
    result = db.session.execute(sql)
    result = result.fetchall()
    return result

def get_book(identifier):
    sql = "SELECT identifier, author, title, publisher, address, year FROM books WHERE identifier=:identifier"
    result = db.session.execute(sql, {'identifier':identifier})
    result = result.fetchone()
    return result

# aux

def books_size():
    sql = "SELECT COUNT(*) FROM books"
    result = db.session.execute(sql)

    return result.fetchone()

def empty_books():
    sql = "DELETE FROM books"
    db.session.execute(sql)
