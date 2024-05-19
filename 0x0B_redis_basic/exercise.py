#!/usr/bin/env python3
"""
A Cache class for interaction with a Redis db
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class for storing data in a Redis db.
    """
    
    def __init__(self):
        """
        Initializes the Cache instance with a Redis client.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis using a random key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
