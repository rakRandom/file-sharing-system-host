from modules.libraries import *

# ==============================================================================================

# Load environment variables
load_dotenv()

# Flask app configuration
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET-KEY")
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Create SocketIO object for WebSocket applications
socketio = SocketIO(app)

# Create HostFinder object to find hosts for client
hostf = HostFinder()

# Defines the directory where the files will be
FILE_DIRECTORY = app.root_path + "\\download"

# ==============================================================================================

# WebSocket function
@socketio.on('find_hosts')
def find_hosts():
    def background_task(scan_ports):
        results = hostf.scan_network(scan_ports)
        socketio.emit('find_hosts', results)
    
    socketio.start_background_task(target=background_task, scan_ports=[2024])


PAGES = {
    "host_finder": "host_finder.html",
    "download": "download.html",
    "files": "files.html"
}

# ========================= Pages =========================
@app.route("/")
@app.route("/<page>")
def render_page(page="index"):
    if page == "index":
        return render_template("index.html", host=request.args.get('h'))
    return render_template("not_found.html")

@app.route("/host_finder")
def host_finder():
    return render_template("host_finder.html")

@app.route("/download")
def download():
    return render_template("download.html", name=request.args.get("name"))

@app.route("/files")
def files():
    return render_template("files.html")


# ===============================================
TOTALLY_SECRET_PASSWORD = "1234"

# Todo: Client version with this endpoint (Delete this before release)
@app.route("/verify")
def verify():
    if request.args.get('p') != TOTALLY_SECRET_PASSWORD:
        return jsonify({"response": False}), 200
    
    return jsonify({"response": True}), 200

# Todo: Client version with this endpoint (Delete this before release)
@app.route("/list_files2")
def list_files2():
    if request.args.get('p') != TOTALLY_SECRET_PASSWORD:
        return jsonify({"response": []}), 200

    file_list: list[str] = []

    for dirpath, _, filenames in os.walk("."):
        for filename in filenames:
            if dirpath.startswith(".\\download"):
                file_list.append(filename)
    
    return jsonify({"response": file_list}), 200

# ===============================================


# Connect user
@app.route("/connect")
def login():
    request_code = request.args.get('c')
    request_password = request.args.get('p')

    if request_code not in hostf.scan_network():
        return jsonify({"error": 1}), 200

    r = requests.get(f"http://{request_code}/verify?p={request_password}")

    if r.status_code != 200:
        return jsonify({"error": 3}), 400
    res = r.json()
    
    if res.get("response", False) is True:
        session['connection-code'] = request_code, request_password
        return jsonify({"error": 0}), 200
    else:
        return jsonify({"error": 2}), 200


# Disconnect user
@app.route("/disconnect")
def disconnect():
    session['connection-code'] = 0
    return redirect(request.host_url)


# Get file list of the host
@app.route("/list_files")
def list_files():
    conn_code = session.get("connection-code")
    r = requests.get(f"http://{conn_code[0]}/list_files2?p={conn_code[1]}")

    if r.status_code != 200:
        return jsonify({"response": []}), 400
    
    res = r.json()

    return jsonify({"response": res["response"]}), 200

# Request a download
@app.route("/download/<filename>")
def download_file(filename):
    try:
        return send_from_directory(FILE_DIRECTORY, filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

# ==============================================================================================

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2024)
