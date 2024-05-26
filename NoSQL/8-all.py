#!/usr/bin/env python3
"""List all documents in a collection"""

from pymongo


def list_all(mongo_collection):
    """List all documents in a collection"""
    documents = mongo_collection.find()
    return [doc for doc in documents] if documents else []
