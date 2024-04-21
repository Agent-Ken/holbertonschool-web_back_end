#!/usr/bin/env python3
""" Authorization module
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class
    """

    def __init__(self):
        """ Auth class constructor
        """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method returns True if the path is not in the list of excluded paths,
        taking into account possible wildcards at the end of the paths.
        """

        if path is None or not excluded_paths:
            return True

        path = path.strip('/')

        for pattern in excluded_paths:
            pattern = pattern.strip('/')
            if pattern.endswith('*'):
                # Remove the '*' and check if the path starts with the pattern
                if path.startswith(pattern[:-1]):
                    return False
            else:
                # Exact match
                if path == pattern:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that returns None
        """
        if request is None:
            return None

        return request.headers.get('Authorization', None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method returns None
        """
        return request
