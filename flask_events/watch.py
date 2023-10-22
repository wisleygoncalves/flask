from flask import Flask, render_template, request, jsonify
import os, json
from flask_sockets import Sockets

app = Flask(__name__)
sockets = Sockets()
sockets.init_app(app)


@sockets.route('/websocket')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        if message is not None:
            ws.send(message)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('localhost', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
