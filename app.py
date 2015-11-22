from flask import Flask, render_template, request, json, Response
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)

@app.route("/")
def main():
    return "Nothing here"

@app.route("/ci/build", methods=['GET', 'POST'])
def build():
    print "XYZ"
    content = request.json
    print content
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp 

if __name__ == "__main__":
    app.run(threaded=True, debug=True)
