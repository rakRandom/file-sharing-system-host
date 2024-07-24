from flask import Flask, send_from_directory, abort, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Defines the directory where the files will be
FILE_DIRECTORY = app.root_path + "\\download"


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/<filename>')
def download_file(filename):
    try:
        return send_from_directory(FILE_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2024)
