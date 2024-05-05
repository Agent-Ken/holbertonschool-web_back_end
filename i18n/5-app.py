#!/usr/bin/env python3
"""Flask app module
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Union

app = Flask(__name__)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ language translation """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


def get_user() -> Union[dict, None]:
    """ Get and retrieve the
    user of the dict
    """
    login_user = request.args.get('login_as', None)

    if login_user is None:
        return None

    user: dict = {}
    user[login_user] = users.get(int(login_user))

    return user[login_user]


@babel.localeselector
def get_locale():
    """ language translation """
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """ a simple template
    """
    return render_template('5-index.html')


@app.before_request
def before_request():
    """ get user bef req """
    g.user = get_user()


if __name__ == "__main__":
    app.run()
