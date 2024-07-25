from flask import Flask, send_from_directory, abort, render_template  # , session
# from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Defines the directory where the files will be
FILE_DIRECTORY = app.root_path + "\\download"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/download")
def download():
    return render_template("download.html")


@app.route("/download/<filename>")
def download_file(filename):
    try:
        return send_from_directory(FILE_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == "__main__":
    app.run(ssl_context="adhoc", host="0.0.0.0", port=2024)  # remove 'ssl_context="adhoc"' later
