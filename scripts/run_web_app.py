from flask import Flask
from markupsafe import escape

import caesar_code

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

@app.route('/encrypt/<int:offset>/<string:text>')
def encript(offset, text):
    return caesar_code.CaesarCode().encrypt(escape(text), offset)

@app.route('/decrypt/<int:offset>/<string:text>')
def decript(offset, text):
    return caesar_code.CaesarCode().decrypt(escape(text), offset)

if __name__ == '__main__':
    app.run()
