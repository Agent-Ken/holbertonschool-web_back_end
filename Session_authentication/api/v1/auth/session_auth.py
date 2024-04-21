#!/usr/bin/env python3
""" Session Auth
"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """ Inherited from Auth
    """

    def __init__(self):
        super().__init__()
