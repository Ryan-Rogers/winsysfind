import flask
import finder
import indexer
import json

app = flask.Flask(__name__)
# index = indexer.index()
with open('index.json', 'r') as index_file:
    index = json.load(index_file)


@app.route('/')
def home():

    return """
        <!DOCTYPE html>
        <head>
            <title>winsysfind</title>
        </head>
        <body>
            <input id="term" />
            <div id="files"></div>

            <script>
                const $term = document.querySelector('#term');
                const $files = document.querySelector('#files');

                const typeHandler = function(e) {
                    var request = new XMLHttpRequest()
                    var term = e.target.value
                    var url = '/find?term=' + term

                    request.open('GET', url, true)
                    request.onload = function() {
                        var data = this.response  // JSON.parse(this.response)
                        $files.innerHTML = this.response;
                    }
                    request.send()
                }

                $term.addEventListener('input', typeHandler)
            </script>
        </body>
    """


@app.route('/find')
def find():
    term = flask.request.args.get('term')
    results = finder.find(index, term)
    return "<p>" + "<br>".join(results) + "<p>"  # json.dumps(results)

if __name__ == '__main__':
    app.run()
