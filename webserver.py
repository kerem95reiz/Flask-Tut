#!/usr/bin/env python3
from flask import Flask, request, url_for
app = Flask(__name__)

@app.route('/')
def ana_sayfa():
    cevab = 'Domates biber patlican'
    return cevab

@app.route('/close')
def close():
    kapat = request.environ.get('werkzeug.server.shutdown')
    kapat()

@app.route('/kisiler/')
def kisiler():
    mesaj = 'kisiler sayfasinda bulunuyorsun'
    return mesaj

@app.route('/profil/<int:identity>')
def profil(identity):
    mesaj = 'Suanda {} numarali profile bakiyorsun'.format(identity)
    return mesaj

@app.route('/liste')
def liste():
    return url_for('profil', identity=30)


if __name__ == '__main__':
    app.run(host='localhost', port=4444, debug=True)
