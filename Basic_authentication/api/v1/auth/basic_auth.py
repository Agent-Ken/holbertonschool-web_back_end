#!/usr/bin/env python3
""" BasicAuth module
"""

from api.v1.auth.auth import Auth, TypeVar
from typing import Tuple, List
import base64
from models.user import User


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ method which returns None
        """
        if (base64_authorization_header is None or
                type(base64_authorization_header) is not str):
            return None

        try:
            base64_authorization_header = base64.b64decode(
                base64_authorization_header).decode("utf-8")
            return base64_authorization_header
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> Tuple[str, str]:
        """ method which returns None
        """
        if (decoded_base64_authorization_header is None or
                type(decoded_base64_authorization_header) is not str or
                ":" not in decoded_base64_authorization_header):
            return (None, None)

        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """ authentication of the user """
        if (user_email is None or
            type(user_email) is not str or
            user_pwd is None or
                type(user_pwd) is not str):
            return None

        try:
            users: List[TypeVar('User')]
            users = User.search({"email": user_email})
        except Exception:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None
