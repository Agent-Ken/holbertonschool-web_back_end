#!/usr/bin/env python3
"""
A Redis basic module.
"""

import redis
import requests
from typing import Callable


redis_client = redis.Redis()


def cache_page(func: Callable[[str], str]) -> Callable[[str], str]:
    """
    Caches the result of a function for 10 secs
    and tracks access count.
    """
    def wrapper(url: str) -> str:
        cached_content = redis_client.get(f"cache:{url}")
        if cached_content:
            return cached_content.decode('utf-8')

        content = func(url)
        redis_client.setex(f"cache:{url}", 10, content)
        redis_client.incr(f"count:{url}")
        
        return content

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """
    Fetches the HTML content of URL.
    """
    response = requests.get(url)
    return response.text
