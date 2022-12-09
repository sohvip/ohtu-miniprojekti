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
        book_list = reference_database.get_books()
        return render_template("create_book.html", book_list=book_list)
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
        misc_list = reference_database.get_table_misc_raw()
        return render_template("createSite.html", misc_list=misc_list)
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

    return redirect("/")

@app.route("/deleteMisc/<int:id>")
def delete_misc(id):
    reference_database.delete_website(id)

    return redirect("/addSite")

@app.route("/addTagBook", methods=["POST"])
def add_tag_to_book(id):
    tag_text = request.form["tag_text"]
    identifier_text = request.form["identifier"]

    tag_id = reference_database.get_tag_id(tag_text)

    reference_database.add_tag_to_work(identifier_text, tag_id)
    
    return redirect("/")

@app.route("/addTagMisc", methods=["POST"])
def add_tag_to_misc(id):
    tag_text = request.form["tag_text"]
    identifier_text = request.form["identifier"]

    tag_id = reference_database.get_tag_id(tag_text)

    reference_database.add_tag_to_work(identifier_text, tag_id)
    
    return redirect("/addSite")


