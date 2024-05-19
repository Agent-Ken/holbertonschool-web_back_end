#!/usr/bin/env python3
"""
A basic Redis web.py module
"""

import redis
import requests
from typing import Callable
from functools import wraps

redis_client = redis.Redis()


def cache_with_expiry(expiry: int):
    """
    cache the result of a function
    with an expiry time.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            cached_result = redis_client.get(f"cache:{url}")
            if cached_result:
                return cached_result.decode('utf-8')
            result = func(url)
            redis_client.setex(f"cache:{url}", expiry, result)

            return result
        return wrapper
    return decorator


@cache_with_expiry(10)
def get_page(url: str) -> str:
    """
    Fetches the content of a URL.
    Tracks the number of accesses to the URL.
    """
    redis_client.incr(f"count:{url}")
    response = requests.get(url)
    return response.text
