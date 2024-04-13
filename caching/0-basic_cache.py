#!/usr/bin/env python3
"""Caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class"""

    def put(self, key, item):
        """A function"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """A function"""
        if key in self.cache_data:
            return self.cache_data[key]
