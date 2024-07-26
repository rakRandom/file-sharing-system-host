from flask import Flask, send_from_directory, abort, render_template, request, session
from flask_socketio import SocketIO
from host_finder import HostFinder

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

socketio = SocketIO(app)
hostf = HostFinder()

# Defines the directory where the files will be
FILE_DIRECTORY = app.root_path + "\\download"


@socketio.on('find_hosts_process')
def find_hosts_process():
    def background_task(scan_ports):
        results = hostf.scan_network(scan_ports)
        socketio.emit('find_hosts_process', results)
    
    socketio.start_background_task(target=background_task, scan_ports=[2024])


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/find_hosts")
def find_hosts():
    return render_template("find_host.html")

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
    app.run(host="0.0.0.0", port=2024)
