import os
import warnings

from flask import Flask, url_for, send_from_directory, render_template

BLOB_DIRECTORY = "/app/blob"

app = Flask(__name__)

@app.route("/")
def index():
    image_filename = "Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi.jpg"
    return render_template("index.html", image_filename=image_filename)


# FIXME: Should this is be /fetch/<filename>? 
@app.route("/<filename>")
def serve_file_from_blob(filename):
    return send_from_directory(BLOB_DIRECTORY, filename, as_attachment=False)

@app.route("/download/<filename>")
def download_file_from_blob(filename):
    return send_from_directory(BLOB_DIRECTORY, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
