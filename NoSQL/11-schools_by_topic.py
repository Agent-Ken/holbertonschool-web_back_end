#!/usr/bin/env python3
"""Finding schools by a specific topic"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school with a specific topic"""
    return list(mongo_collection.find({"topics": topic}))
