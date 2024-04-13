#!/usr/bin/env python3
"""Caching"""

from base_caching import BaseCaching


class FIFOCache (BaseCaching):
    """A class"""

    def __init__(self):
        """A function"""
        super().__init__()

    def put(self, key, item):
        """A function"""
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_item = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(first_item))
                self.cache_data.pop(first_item)

    def get(self, key):
        """A function"""
        if key in self.cache_data:
            return self.cache_data[key]
