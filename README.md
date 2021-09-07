## Create desktop applications powered by Flask
  
<!-- [![Downloads](https://pepy.tech/badge/flaskqt)](https://pepy.tech/project/flaskqt) -->
<!-- [![PyPI](https://img.shields.io/pypi/v/flaskqt?color=blue)](https://pypi.org/project/flaskqt/) -->

## Install

``` py
pip install flaskQT
```
<!-- If you are using `conda` checkout [this link](https://github.com/conda-forge/flaskqt-feedstock). -->
<!-- 
For any framework selected add bellow js code to your app.
Code bellow makes some pooling to the `/flaskqt-keep-server-alive` endpoint and informs flaskqt to keep server running while gui is running. Without code bellow server will close after a few seconds.
```js

async function getRequest(url='') {
    const response = await fetch(url, {
      method: 'GET', 
      cache: 'no-cache'
    })
    return response.json()
}
  
document.addEventListener('DOMContentLoaded', function() {

let url = document.location
let route = "/flaskqt-keep-server-alive"
let interval_request = 3 * 1000 //sec

function keep_alive_server(){
    getRequest(url + route)
    .then(data => console.log(data))
}

setInterval(keep_alive_server, interval_request)()

})

``` -->


## Usage with Flask

Let's say we have the following flask application:
```py
#main.py

from flask import Flask  
from flask import render_template
from flaskqt import flaskQT

app = Flask(__name__)

@app.route("/")
def hello():  
    return render_template('index.html')

@app.route("/home", methods=['GET'])
def home(): 
    return render_template('some_page.html')

ui = flaskQT()
ui.init_app(app)

if __name__ == "__main__":
    # app.run() for debug
    ui.run()
   
```

## Options

* **app**, ==> app instance

* **width=800** ==> window width default 800

* **height=600** ==> default height 600

* **fullscreen=False** ==> start app in fullscreen (equvalent to pressing `F11` on chrome)

* **maximized=False** ==> start app in maximized window

Should work on windows/linux/mac with no isssues.

**flaskqt doesn't interfere with your way of doing a flask application** it just helps converting it into a desktop app more easily with pyinstaller.

### Distribution

You can distribute it as a standalone desktop app with **pyinstaller** or [**pyvan**](https://github.com/ClimenteA/pyvan).

### Credits

Inspired by:
- https://github.com/Widdershin/flask-desktop