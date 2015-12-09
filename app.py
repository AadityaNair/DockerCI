from flask import Flask, request, Response, jsonify
app = Flask(__name__)

import db

@app.route("/")
def main():
    return "Nothing here", 408

@app.route("/ci/build", methods=['GET', 'POST'])
def build():
    content = request.json
    print content
    
    git_dir = str(content[u'git_dir'])
    sha1 = str(content[u'id'])
    msg = str(content[u'msg'])
    db.new_commit(git_dir, sha1, msg)

    return Response(request.json, status=200, mimetype='application/json')

@app.route("/ci/status/all")
def status_all():
    return jsonify(db.find_build(allbuilds=True))

@app.route("/ci/status/last")
def status_last():
    return jsonify(db.find_build(allbuilds=False))


if __name__ == "__main__":
    app.run(threaded=True, debug=True)
