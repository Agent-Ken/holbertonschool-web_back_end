#!/usr/bin/env python3
"""
A Redis basic module.
"""

import redis
import requests
from typing import Callable
from functools import wraps


redis_client = redis.Redis()


def count_calls(method: Callable) -> Callable:
    """
    Caches the result of a function for 10 secs
    and tracks access count.
    """
    @wraps(method)
    def wrapper(url):
        """ Wrapper decorator """
        redis_client.incr(f"count:{url}")
        cached_html = redis_client.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        redis_client.setex(f"cached:{url}", 10, html)
        return html

    return wrapper

@count_calls
def get_page(url: str) -> str:
    """
    Fetches the HTML content of URL.
    """
    response = requests.get(url)
    return response.text
