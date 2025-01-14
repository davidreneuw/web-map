import os
import warnings

from flask import Flask, url_for, send_from_directory, render_template

BLOB_DIRECTORY = "/blob"

DEPLOY = True

app = Flask(__name__)

@app.route("/")
def index():
    image_filename = "Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi.jpg"
    return render_template("index.html", image_filename=image_filename)

@app.route("/image/<filename>")
def serve_image(filename):
    if DEPLOY:
        proxy_url = "/app/WEB"
        full_url = f"{proxy_url}/filename"
        return send_from_directory(BLOB_DIRECTORY, full_url, as_attachment=False)
    else:
        return send_from_directory(BLOB_DIRECTORY, filename, as_attachment=False)

@app.route("/download/<filename>")
def download_file_from_blob(filename):
    if DEPLOY:
        proxy_url = "/app/WEB"
        full_url = f"{proxy_url}/filename"
        return send_from_directory(BLOB_DIRECTORY, full_url, as_attachment=True)
    else:
        return send_from_directory(BLOB_DIRECTORY, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
