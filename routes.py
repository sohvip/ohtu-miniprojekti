from app import app
from reference_database import create_book
from printing_stuff import get_books_human_readable
from flask import request, render_template, redirect

@app.route('/', methods=['get', 'post'])
def index():
    book_list = get_books_human_readable()
    if request.method == 'GET':
        return render_template('index.html', book_list=book_list)
    if request.method == 'POST':
        identifier = request.form['identifier']
        author = request.form['author']
        editor = request.form['editor']
        title = request.form['title']
        publisher = request.form['publisher']
        year = request.form['year']
        create_book(identifier, author, editor, title, publisher, year)
        return redirect('/')