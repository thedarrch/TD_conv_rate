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

@app.route('/')
def index():
    return "Hello World!"
app.run()