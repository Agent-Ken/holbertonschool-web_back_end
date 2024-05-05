#!/usr/bin/env python3
"""
This module sets up Flask with Flask-Babel
for internationalization
"""

from flask import Flask, render_template
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """ Configuration class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Select a language translation """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ template with parametrized text
    render by using message IDs. """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
