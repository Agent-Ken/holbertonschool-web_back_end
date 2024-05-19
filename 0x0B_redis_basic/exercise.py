#!/usr/bin/env python3
"""
A Cache class for interaction with a Redis db
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    counts how many times a method is called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


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

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in Redis using a random key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieves the data from Redis via provided key
        and converts it using `fn` if provided.
        """
        value = self._redis.get(key)
        if fn is not None and value is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves str value from Redis.
        """
        value = self.get(key)
        return value.decode('utf-8') if value is not None else None

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves int value from Redis.
        """
        value = self.get(key)
        return int(value) if value is not None else None
