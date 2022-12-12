from app import app
import reference_database
import bibtex_converter
from flask import request, render_template, redirect
import pyperclip


@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")

@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    if request.method == "GET":
        identifiers = reference_database.get_identifiers_dict()
        work_tag_pairs = reference_database.get_work_tag_pairs_dict()
        book_list = reference_database.get_books()
        return render_template("create_book.html", book_list=book_list, identifiers=identifiers, work_tag_pairs=work_tag_pairs)
    if request.method == "POST":
        identifier = request.form["identifier"]
        author = request.form["author"]
        editor = request.form["editor"]
        title = request.form["title"]
        publisher = request.form["publisher"]
        year = request.form["year"]
        if identifier and author and editor and title and publisher and year and year.isnumeric():
            reference_database.create_book(identifier, author, editor, title, publisher, year)
        return redirect("/add_book")

@app.route("/addSite", methods=["GET", "POST"])
def add_site():
    if request.method == "GET":
        identifiers = reference_database.get_identifiers_dict()
        work_tag_pairs = reference_database.get_work_tag_pairs_dict()
        misc_list = reference_database.get_table_misc_raw()
        return render_template("createSite.html", misc_list=misc_list, identifiers=identifiers, work_tag_pairs=work_tag_pairs)
    if request.method == "POST":
        identifier = request.form["identifier"]
        title = request.form["title"]
        editor = request.form["editor"]
        how_published = request.form["how_published"]
        year = request.form["year"]
        note = request.form["note"]
        if identifier and title and editor and how_published and note and year.isnumeric():
            reference_database.create_misc(identifier, title, editor, how_published, year, note)

        return redirect('/addSite')

@app.route("/book_bibtex/<int:id>", methods=["GET", "POST"])
def book_bibtex(id):
    bibtex = bibtex_converter.book_to_bibtex(id)
    if request.method == "GET":
        return render_template("book_bibtex.html", bibtex=bibtex, id=id)
    if request.method == "POST":
        pyperclip.copy(bibtex)
        return render_template("book_bibtex.html", bibtex=bibtex, id=id)

@app.route("/website_bibtex/<int:id>", methods=["GET", "POST"])
def website_bibtex(id):
    bibtex = bibtex_converter.website_to_bibtex(id)
    if request.method == "GET":
        return render_template("website_bibtex.html", bibtex=bibtex, id=id)
    if request.method == "POST":
        pyperclip.copy(bibtex)
        return render_template("website_bibtex.html", bibtex=bibtex, id=id)

@app.route("/deleteBook/<int:id>")
def delete_book(id):
    reference_database.delete_book(id)

    return redirect("/add_book")

@app.route("/deleteMisc/<int:id>")
def delete_misc(id):
    reference_database.delete_website(id)

    return redirect("/addSite")

@app.route("/addTagBook", methods=["POST"])
def add_tag_to_book():
    tag_text = request.form["tag_text"]
    identifier_text = request.form["identifier"]

    tag_id = reference_database.get_tag_id(tag_text)

    reference_database.add_tag_to_work(identifier_text, tag_id)
    
    return redirect("/add_book")

@app.route("/addTagMisc", methods=["POST"])
def add_tag_to_misc():
    tag_text = request.form["tag_text"]
    identifier_text = request.form["identifier"]

    tag_id = reference_database.get_tag_id(tag_text)
    

    reference_database.add_tag_to_work(identifier_text, tag_id)
    
    return redirect("/addSite")

@app.route("/listByTag", methods=["POST"])
def list_by_tag():
    tag_text = request.form["tag_text"]
    
    book_list = reference_database.list_books_by_tag(tag_text)
    misc_list = reference_database.list_misc_by_tag(tag_text)

    return render_template("list.html", book_list=book_list, misc_list=misc_list)

@app.route("/sortByDateAddedBook")
def sort_by_date_books():
    book_list = reference_database.list_books_by_time_added()
    return render_template("dateSortedBooks.html", book_list=book_list)

@app.route("/sortByDateAddedMisc")
def sort_by_date_miscs():
    misc_list = reference_database.list_misc_by_time_added()
    return render_template("dateSortedMiscs.html", misc_list=misc_list)

@app.route("/sortByNameBook")
def sort_by_name_books():
    book_list = reference_database.list_books_by_author_name()
    return render_template("nameSortedBooks.html", book_list=book_list)

@app.route("/sortByNameMisc")
def sort_by_name_miscs():
    misc_list = reference_database.list_misc_by_author_name()
    return render_template("nameSortedMiscs.html", misc_list=misc_list)



