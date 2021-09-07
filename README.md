## Create desktop applications powered by Flask
  
<!-- [![Downloads](https://pepy.tech/badge/flaskqt)](https://pepy.tech/project/flaskqt) -->
<!-- [![PyPI](https://img.shields.io/pypi/v/flaskqt?color=blue)](https://pypi.org/project/flaskqt/) -->

## Installation

```
pip install flask-QT
```

## Hello World with Flask-QT

```py
from flask import Flask, render_template, request
from flaskqt import FlaskQT
import os

app = Flask(__name__)
ui  = FlaskQT(app, window_title='App Title')

@app.route('/')
def main():
    return "Hello world!"

if __name__ == '__main__':
    ui.run()
```

## Packaging

```
pip install pyinstaller
pyinstaller your_app.py --onefile
```

This will leave you with compiled executables.

## Options

* **width=800** ==> window width default 800

* **height=600** ==> default height 600

* **fullscreen=False** ==> start app in fullscreen (equvalent to pressing `F11` on chrome)

* **maximized=False** ==> start app in maximized window

Should work on windows/linux/mac with no isssues.

**flaskqt does not interfere with your way of doing a flask application** it just helps converting it into a desktop app more easily with pyinstaller.

### Distribution

You can distribute your Flask app as a standalone desktop app with **pyinstaller** and **InnoSetup**.

### Credits

Inspired by:
- https://github.com/Widdershin/flask-desktop