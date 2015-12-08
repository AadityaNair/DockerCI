from flask import Flask, request, json, Response
app = Flask(__name__)

@app.route("/")
def main():
    return "Nothing here"

@app.route("/ci/build", methods=['GET', 'POST'])
def build():
    content = request.json
    print content
    
    git_dir = str(content[u'git_dir'])
    sha1 = str(content[u'id'])
    msg = str(content[u'msg'])
    
    return Response(request.json, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(threaded=True, debug=True)
