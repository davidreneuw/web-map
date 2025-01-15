import os
import warnings

from flask import Flask, url_for, send_from_directory, render_template

AZURE_BLOB_MOUNT = "/blob"

app = Flask(__name__)

# Define your base directory relative to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BLOB_DIRECTORY = os.path.join(BASE_DIR, AZURE_BLOB_MOUNT)

@app.route("/")
def index():
    image_filename = "Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi.jpg"
    return render_template("index.html", image_filename=image_filename)

@app.route("image/<filename>")
def serve_file(filename):
    return send_from_directory(BLOB_DIRECTORY, filename)
    
@app.route("download/<filename>")
def download_file_from_blob(filename):
    return send_from_directory(BLOB_DIRECTORY, filename, as_attachment=True)
