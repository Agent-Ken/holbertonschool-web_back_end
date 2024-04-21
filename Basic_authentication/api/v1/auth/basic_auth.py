#!/usr/bin/env python3
""" BasicAuth module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class
    """

    def __init__(self):
        """ Constructor of the class
        """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ method which returns None
        """
        if (authorization_header is None or
            type(authorization_header) is not str or
                authorization_header.startswith("Basic ") is False):
            return None

        return authorization_header[6:]
