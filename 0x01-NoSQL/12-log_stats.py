#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB
Database: logs
Collection: nginx
"""

from pymongo import MongoClient

def log_stats(mongo_collection):
    """
    Provides statistics about Nginx logs stored in MongoDB.
    """
    total_logs = mongo_collection.count_documents({})
    get_logs = mongo_collection.count_documents({"method": "GET"})
    post_logs = mongo_collection.count_documents({"method": "POST"})
    put_logs = mongo_collection.count_documents({"method": "PUT"})
    patch_logs = mongo_collection.count_documents({"method": "PATCH"})
    delete_logs = mongo_collection.count_documents({"method": "DELETE"})
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_logs}")
    print(f"\tmethod POST: {post_logs}")
    print(f"\tmethod PUT: {put_logs}")
    print(f"\tmethod PATCH: {patch_logs}")
    print(f"\tmethod DELETE: {delete_logs}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    log_stats(nginx_collection)

