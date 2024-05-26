#!/usr/bin/env python3
"""Insert a document based on kwargs
"""

import pymongo


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs"""
    if kwargs:
        result = mongo_collection.insert_one(kwargs)
        return result.inserted_id
    return None
