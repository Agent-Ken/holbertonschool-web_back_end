#!/usr/bin/env python3
"""List all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in a collection"""
    documents = mongo_collection.find()
    if mongo_collection.count() == 0:
        return []

    return list(mongo_collection)
