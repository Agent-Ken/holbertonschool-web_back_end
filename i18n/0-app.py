#!/usr/bin/env python3
"""
This module initializes a basic Flask
application with a single route.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Render a simple template with a welcome message. """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
