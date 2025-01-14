import os
import warnings

from flask import Flask, url_for, send_from_directory, render_template

# Define where the blob directory is
BLOB_DIRECTORY = "/app/blob"

app = Flask(__name__)


@app.route("/")
def index():
    print(f"<p>{BLOB_DIRECTORY}</p>")
    image_filename = "Orange_tabby_cat_sitting_on_fallen_leaves-Hisashi.jpg"
    return render_template("index.html", image_filename=image_filename)


@app.route("/image/<filename>")
def serve_image(filename):
    return send_from_directory(BLOB_DIRECTORY, filename)

# if __name__ == "__main__":
#     app.run(debug=True, host='0.0.0.0')
