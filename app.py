from flask import Flask, send_from_directory, abort, render_template  # , session
from flask_socketio import SocketIO
from host_finder import HostFinder
# from flask_session import Session

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

socketio = SocketIO(app)
hostf = HostFinder()

# Defines the directory where the files will be
FILE_DIRECTORY = app.root_path + "\\download"


@socketio.on('start_scan')
def handle_start_scan(data):
    scan_ports = data.get('ports', [80, 8000, 8080])
    
    def background_task(scan_ports):
        results = hostf.scan_network(scan_ports)
        socketio.emit('scan_results', results)
    
    socketio.start_background_task(target=background_task, scan_ports=scan_ports)


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
    socketio.run(app, host="0.0.0.0", port=8080)
