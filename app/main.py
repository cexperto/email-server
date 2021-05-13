import os
from flask import Flask, request, render_template, jsonify, send_from_directory, abort
from app.config import UPLOAD_DIRECTORY
from app.separator import separator
from app.character import character

# UPLOAD_DIRECTORY = "/project/api_uploaded_files"



app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/',methods=['POST'])
def email():
    sender = request.form['sender']
    copys = request.form['copys']
    message = request.form['message']
    other = request.form['other']

    my_emails = []
    for item in separator(other):
        my_emails.append(item)    

    # Return 201 CREATED
    return f"{sender} {copys} {message} {my_emails}", 201
    

@app.route("/myFiles")
def list_files():
    """Endpoint to list files on the server."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify({
        "files created": files
    })



@app.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


 
@app.route("/files/<filename>", methods=["POST"])
def post_file(filename):
    """Upload a file."""

    if "/" in filename:
        # Return 400 BAD REQUEST
        abort(400, "no subdirectories allowed")

    with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
        fp.write(request.data)

    # Return 201 CREATED
    return "", 201