#!/usr/bin/env python3
"""Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class"""

    def put(self, key, item):
        """A function"""
        if key and item:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last = self.cache_data.popitem()
                print("DISCARD:", last[0])
            self.cache_data[key] = item

    def get(self, key):
        """A function"""
        if key in self.cache_data:
            returned_value = self.cache_data[key]
            self.cache_data.pop(key)
            self.cache_data[key] = returned_value
            return returned_value
