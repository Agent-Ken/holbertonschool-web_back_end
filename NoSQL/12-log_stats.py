#!/usr/bin/env python3
"""Provides stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient


def log_stats():
    """print stats about Nginx logs"""
    logs_count = mongo_collection.count_documents({})
    print(f"{logs_count} logs") 
    
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
