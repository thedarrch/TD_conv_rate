# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:29:18 2020

@author: theda
"""

import flask
import time

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

import TDconv

app = flask.Flask(__name__)

@app.route('/home')
def index():
    def inner():
        for x in range(100):
            a = TDconv.get_rates()
            time.sleep(5)
            yield '%s<br/>' % a
    return flask.Response(inner(), mimetype='text/html')
app.run()