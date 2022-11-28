# connect to the database etc.

def create_book(identifier, author, editor, title, publisher, year):
    sql = "INSERT INTO books (ref_type, identifier, author, editor, title, publisher, year) VALUES (book, :id, :auth, :edit, :title, :publ, :year)"
    db.session.execute(sql, {"id":identifier, "auth":author, "edit":editor, "title":title, "publ":publisher, "year":year})
    db.session.commit()