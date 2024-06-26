#!/usr/bin/env python3
"""
Auth methods
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """Hash a password
    """
    byte = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(byte, salt)
    return hashed


def _generate_uuid() -> str:
    """
    Returns a string representation of a new UUID
    """
    return str(uuid.uuid4())


class Auth:
    """class to interact with the authentication DB.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            pass
        hashed = _hash_password(password).decode()
        user = self._db.add_user(email, hashed)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """
        checks password
        """
        try:
            usr = self._db.find_user_by(email=email)
            password = password.encode("utf-8")
            usr_pass = usr.hashed_password.encode("utf-8")
            return bcrypt.checkpw(password, usr_pass)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """
        Creates a session
        """
        try:
            usr = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(usr.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Returns the user"""
        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """deletes the session"""
        try:
            user = self._db.find_user_by(id=user_id)
            self._db.update_user(user.id, session_id=None)
        except Exception:
            return

    def get_reset_password_token(self, email: str) -> str:
        """retrieves the token"""
        try:
            user = self._db.find_user_by(email=email)
            token = _generate_uuid()
            self._db.update_user(user.id, reset_token=token)
            return token
        except Exception:
            raise ValueError

    def update_password(self, reset_token: str, password: str) -> None:
        """updates the password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
            hashed = _hash_password(password).decode()
            self._db.update_user(user.id, hashed_password=hashed,
                                 reset_token=None)
        except Exception:
            raise ValueError
