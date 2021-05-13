from app.process import process
import os
from flask import Flask, request, render_template, jsonify, send_from_directory, abort
from app.config import UPLOAD_DIRECTORY
from app.separator import separator
from app.character import character
import shutil

# UPLOAD_DIRECTORY = "/project/api_uploaded_files"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")



@app.route('/',methods=['POST'])
def email():
    """capture request and precess data """
    sender = request.form['sender']
    copys = request.form['copys']
    message = request.form['message']
    other = request.form['other']
    

    my_emails = []
    for item in separator(other):
        clean_item = character(str(item))
        my_emails.append(clean_item)

    process(sender, my_emails, message, copys)
    
    return f'files generated', 201
    

@app.route("/myFiles")
def list_files():
    """Get list all files from the server."""
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
    """Download a specific file."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@app.route('/delete')
def delete():
    shutil.rmtree(UPLOAD_DIRECTORY)
    return 'all directory deleted, please generate news files in / route for query myFiles'