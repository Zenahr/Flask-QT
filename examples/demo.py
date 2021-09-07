from flask import Flask, render_template, request
from flaskqt import FlaskQT

import os

app = Flask(__name__)
ui  = FlaskQT(app, window_title='App Title', debug=True)

@app.route('/')
def main():
    return "Hello world!"

if __name__ == '__main__':
    ui.run()