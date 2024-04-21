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
        """ Method returns True
        if the path is not in the list
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        for exclude_path in excluded_paths:
            if path.strip("/") in exclude_path.strip("/"):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that returns None
        """
        return request

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method returns None
        """
        return request
