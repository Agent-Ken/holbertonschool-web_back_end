#!/usr/bin/env python3
"""Password encryption"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed password"""
    hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    return hashed_pass


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a password is valid"""
    return bcrypt.checkpw(password.encode(), hashed_password)
