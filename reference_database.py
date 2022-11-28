# connect to the database etc.
from db import db

def create_book(identifier, author, editor, title, publisher, year):

    if identifier_already_exists(identifier):
        return "Identifier already in use for another work"
    
    sql = "INSERT INTO books (ref_type, identifier, author, editor, title, publisher, year) VALUES (book, :id, :auth, :edit, :title, :publ, :year)"
    db.session.execute(sql, {"id":identifier, "auth":author, "edit":editor, "title":title, "publ":publisher, "year":year})
    db.session.commit()

def identifier_already_exists(identifier):

    if identifier_already_exists_books(identifier):
        return True

    return False

def identifier_already_exists_books(identifier):
    sql = "SELECT FROM books WHERE identifier=:id"
    result = db.session.execute(sql, {"id":identifier})
    result = result.fetchone()

    if result:
        return True

    return False
