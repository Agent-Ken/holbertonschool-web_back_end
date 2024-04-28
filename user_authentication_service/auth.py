#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password
        """
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """register a new user
        """
        user = self._db._session.query(User).filter_by(email=email).first()
        if user:
            raise ValueError(f'User {email} already exists')
        else:
            hashed_password = self._hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
