#!/usr/bin/env python3
"""
A Redis basic module
"""
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Counts how many times a method is called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """
    Stores history of inputs/outputs for a function.
    """
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result
    return wrapper

def replay(method: Callable):
    """
    Function that displays the call history of a function.
    """
    redis_instance = method.__self__._redis
    inputs_key = method.__qualname__ + ":inputs"
    outputs_key = method.__qualname__ + ":outputs"
    inputs = redis_instance.lrange(inputs_key, 0, -1)
    outputs = redis_instance.lrange(outputs_key, 0, -1)
    count = redis_instance.get(method.__qualname__).decode('utf-8')

    print(f"{method.__qualname__} was called {count} times:")
    for input, output in zip(inputs, outputs):
        print(f"{method.__qualname__}(*{input.decode('utf-8')}) -> {output.decode('utf-8')}")


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
    @call_history
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
