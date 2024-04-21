#!/usr/bin/env python3
""" Session Auth
"""

from api.v1.auth.auth import Auth
from typing import Dict
import uuid


class SessionAuth(Auth):
    """ Inherited from Auth
    """
    user_id_by_session_id: Dict = {}

    def create_session(self, user_id: str = None) -> str:
        """ Session ID creation
        """
        if user_id is None or type(user_id) is not str:
            return None
        session_id: str = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id
