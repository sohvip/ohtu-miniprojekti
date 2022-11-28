from app import app
from flask import request, render_template

@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        pass