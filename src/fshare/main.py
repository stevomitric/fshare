from flask import Flask, send_from_directory, request, send_file, redirect
from json import dumps
from .filemanager import FileManager

import os, pathlib

app = Flask(__name__)

fileManager = FileManager()

static_path = str(pathlib.Path(__file__).parent.resolve().absolute())+"/"

def render_page(page, data):
    f = open(page, 'r')
    page_data = f.read()
    f.close()

    for key in data:
        if (r"{{" + key + r"}}" in page_data):
            page_data = page_data.replace(r"{{" +key+ r"}}", data[key])
    
    return page_data


@app.route("/static/<file>", methods=["GET"])
def static_file(file):
    if (file.endswith(".js") and file in os.listdir(static_path)):
        return send_from_directory(static_path, file )
    return {}, 404

@app.route("/file/<file>", methods=["GET"])
def download_file(file):
    if (not fileManager.getFilePath(file)):
        return {}, 404
    else:
        return send_file( fileManager.getFilePath(file), as_attachment=True, download_name=file )

@app.route("/delete/<file>", methods=["GET"])
def delete_file(file):
    if (not fileManager.getFilePath(file)):
        return {}, 404
    else:
        fileManager.removeFile(file)
    return redirect("/", code=302)

@app.route("/", methods=["GET", "POST"])
def index():
    if (request.method == "POST" and 'file' in request.files and request.files['file'].filename):
        data = request.files['file'].read()
        fileManager.saveFile(request.files['file'].filename, data)

    files = fileManager.getFileData()

    data = render_page(static_path+"index.html", {"form_data": dumps({"data": files}) })

    return data


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)