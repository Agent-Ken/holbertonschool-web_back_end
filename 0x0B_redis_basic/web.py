#!/usr/bin/env python3
"""
Retrieves web pages and caches their contents.
"""

import requests
import redis
from functools import wraps

redis_client = redis.Redis()


def count_url_accesses(func):
    """
    Counts the number of times URL is accessed.
    """
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        redis_client.incr(count_key)
        return func(url)
    return wrapper

def cache_page(func):
    """
    Caches the page content with expiration time.
    """
    @wraps(func)
    def wrapper(url):
        cache_key = f"cache:{url}"
        cached_content = redis_client.get(cache_key)
        
        if cached_content:
            return cached_content.decode('utf-8')
        
        page_content = func(url)
        redis_client.setex(cache_key, 10, page_content)
        return page_content
    return wrapper

@count_url_accesses
@cache_page
def get_page(url: str) -> str:
    """
    Gets HTML content of the URL.
    """
    response = requests.get(url)
    return response.text
