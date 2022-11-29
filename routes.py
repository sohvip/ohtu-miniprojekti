from app import app
import reference_database
from printing_stuff import get_books_human_readable
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
        if year.isnumeric():
            reference_database.create_book(identifier, author, editor, title, publisher, year)
        return redirect('/')