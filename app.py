# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:29:18 2020

@author: theda
"""

import flask
import time
import os

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

import TDconv

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/rates')
def rates():
    return TDconv.get_rates()

if __name__ == "__main__":
	app.run()
