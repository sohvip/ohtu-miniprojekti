from app import app
import reference_database
from bibtex_converter import book_to_bibtex
from flask import request, render_template, redirect

@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'GET':
        book_list = reference_database.get_books()
        return render_template('index.html', book_list=book_list)
    if request.method == 'POST':
        identifier = request.form['identifier']
        author = request.form['author']
        editor = request.form['editor']
        title = request.form['title']
        publisher = request.form['publisher']
        year = request.form['year']
        if identifier and author and editor and title and publisher and year and year.isnumeric():
            reference_database.create_book(identifier, author, editor, title, publisher, year)
        return redirect('/')

@app.route("/addSite", methods=['get', 'post'])
def add_site():
    if request.method == 'GET':
        misc_list = reference_database.get_table_misc_raw()
        return render_template('createSite.html', misc_list=misc_list)
    if request.method == 'POST':
        identifier = request.form['identifier']
        title = request.form['title']
        editor = request.form['editor']
        how_published = request.form['how_published']
        year = request.form['year']
        note = request.form['note']

        if year.isnumeric():
            reference_database.create_misc(identifier, title, editor, how_published, year, note)

        return redirect('/addSite')
@app.route('/book_bibtex/<int:id>', methods=['get'])
def book_bibtex(id):
    if request.method == 'GET':
        bibtex = book_to_bibtex(id)
        return render_template('book_bibtex.html', bibtex=bibtex)
