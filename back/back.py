#!/usr/bin/env python

import flask
from flask import jsonify
import os 

APP_SERVER = os.environ.get('APP_SERVER', '127.0.0.1')
APP_PORT = os.environ.get('APP_PORT', '5002')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1> My awsome app backend</h1>"
@app.route('/api/v1/remote', methods=['GET'])
def api_all():
    return jsonify({'answer': 'hello world from remote'})


if __name__ == "__main__":
    app.run(port=int(APP_PORT), host=APP_SERVER)
