#!/usr/bin/env python3
"""
Auth module
"""
from db import DB
from user import User
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash a password
    """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


class Auth:
    """class for interacting with the authentication DB.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """register a new user
        """
        user = self._db._session.query(User).filter_by(email=email).first()
        if user:
            raise ValueError(f'User {email} already exists')
        else:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            new_user = self._db.add_user(email, hashed_password)
            return new_user
