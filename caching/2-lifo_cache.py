#!/usr/bin/env python3
"""Caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class"""

    def __init__(self):
        super().__init__()
        self.previous_added = None

    def put(self, key, item):
        """A function"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.previous_added)
                print("DISCARD: {}".format(self.previous_added))
            self.previous_added = key

    def get(self, key):
        """A function"""
        if key in self.cache_data:
            return self.cache_data[key]
