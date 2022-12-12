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

def delete_book(book_id):
    sql = "DELETE FROM books WHERE id=:book_id"
    db.session.execute(sql, {'book_id':book_id})
    db.session.commit()

def delete_website(misc_id):
    sql = "DELETE FROM misc WHERE id=:misc_id"
    db.session.execute(sql, {'misc_id':misc_id})
    db.session.commit()

def create_tag(tag_text):
    sql = "INSERT INTO tags (tag_text) VALUES (:text) RETURNING id"
    tag_id = db.session.execute(sql, {'text':tag_text})
    db.session.commit()

    return tag_id.fetchone()[0]

def add_tag_to_work(identifier, tag_id):
    sql = "INSERT INTO work_tag_pairs (citation_identifier, tag_id) VALUES (:id, :t_id)"
    db.session.execute(sql, {'id':identifier, 't_id':tag_id})
    db.session.commit()

def list_books_by_tag(tag_text):
    sql = "SELECT B.identifier, B.author, B.editor, B.title, B.publisher, B.year, B.id "\
        "FROM books B, tags T, work_tag_pairs W WHERE B.identifier=W.citation_identifier"\
        " AND W.tag_id=T.id AND T.tag_text=:text"
    result = db.session.execute(sql, {'text':tag_text})
    return result.fetchall()

def list_misc_by_tag(tag_text):
    sql = "SELECT M.identifier, M.title, M.editor, M.how_published, M.year, M.note, M.id "\
        "FROM misc M, tags T, work_tag_pairs W WHERE M.identifier=W.citation_identifier"\
        " AND W.tag_id=T.id AND T.tag_text=:text"
    result = db.session.execute(sql, {'text':tag_text})
    return result.fetchall()

def list_books_by_time_added():
    sql = "SELECT identifier, author, editor, title, publisher, year, id FROM books ORDER BY ASC"
    result = db.session.execute(sql)
    result = result.fetchall()
    return result

def list_misc_by_time_added():
    sql = "SELECT identifier, title, editor, how_published, year, note, id FROM misc ORDER BY id ASC"
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

def get_tag_id(tag_text):
    sql = "SELECT id FROM tags WHERE tag_text=:text"
    result = db.session.execute(sql, {'text':tag_text}).fetchone()
    if result is None:
        tag_id = create_tag(tag_text)
        return tag_id

    return result[0]

def get_identifiers_dict():
    sql = "SELECT identifier FROM books UNION SELECT identifier FROM misc"
    result = db.session.execute(sql)
    identifiers = result.fetchall()
    identifier_list = []
    for identifier in identifiers:
        identifier_list.append(identifier[0])
    identifier_dict = {}
    identifier_dict["identifiers"] = identifier_list

    return identifier_dict

def get_work_tag_pairs_dict():
    sql = "SELECT WT.citation_identifier, T.tag_text FROM tags T, work_tag_pairs WT WHERE WT.tag_id=T.id"
    result = db.session.execute(sql)
    data = result.fetchall()
    work_tag_pairs_dict = {}
    for pair in data:
        if pair[0] not in work_tag_pairs_dict:
            work_tag_pairs_dict[pair[0]] = []
            work_tag_pairs_dict[pair[0]].append(pair[1])
        else:
            work_tag_pairs_dict[pair[0]].append(pair[1])

    return work_tag_pairs_dict
