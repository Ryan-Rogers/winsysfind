import json

from flask import Flask
from flask import render_template
from flask import request

import finder
import indexer

indexed_files = list()

app = Flask(__name__, template_folder='templates')
app.debug = True


@app.route('/')
def home():
    return render_template('index.html', index_length=len(indexed_files))


@app.route('/index')
def index():
    global indexed_files
    indexed_files = indexer.index()

    return str(len(indexed_files))


@app.route('/find')
def find():
    term = request.args.get('term')
    files_found = finder.find(indexed_files, term)

    return json.dumps(files_found)

if __name__ == '__main__':
    app.run()
