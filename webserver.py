#!/usr/bin/env python3
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    cevab = 'Domates biber patlican'
    return cevab

@app.route('/close')
def close():
    kapat = request.environ.get('werkzeug.server.shutdown')
    kapat()

if __name__ == '__main__':
    app.run(host='localhost', port=4444, debug=False)
