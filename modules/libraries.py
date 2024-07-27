if __name__ == "__main__":
    print("Cannot execute libraries.py as main")
    exit(-2)

try:
    from flask import Flask, send_from_directory, abort, render_template, request, session, jsonify, redirect
    from flask_socketio import SocketIO
    from modules.host_finder import HostFinder
    from dotenv import load_dotenv
    import os, requests
except:
    print("Error at libraries.py importations")
    exit(-1)
