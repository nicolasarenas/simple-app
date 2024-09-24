#!/usr/bin/env python 

import flask 
from flask import jsonify
import os 
import requests

app = flask.Flask(__name__)
app.config["DEBUG"] = True
REMOTE_SERVER = os.environ.get('REMOTE_SERVER', '127.0.0.1')
REMOTE_PORT = os.environ.get('REMOTE_PORT', '5002')
APP_SERVER = os.environ.get('APP_SERVER', '127.0.0.1')
APP_PORT = os.environ.get('APP_PORT', '5001')

@app.route('/', methods=['GET'])
def home():
    return "<h1> My awsome app </h1>"

@app.route('/api/v1/local', methods=['GET'])
def api_all():
    return jsonify({'answer': 'hello world from front'})

@app.route('/api/v1/remote', methods=['GET'])
def api_remote():
    url = f'http://{REMOTE_SERVER}:{REMOTE_PORT}/api/v1/remote'
    try: 
        response = requests.get(url)
        response.raise_for_status() 
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}) , 500

if __name__ == "__main__":
    app.run(port=int(APP_PORT), host=APP_SERVER)
