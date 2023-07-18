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
    # Total logs count
    total_logs = mongo_collection.count_documents({})

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_counts = {method: mongo_collection.count_documents({"method": method}) for method in methods}

    # Status check count
    status_check = mongo_collection.count_documents({"method": "GET", "path": "/status"})

    # IPs top 10
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ip_counts = list(mongo_collection.aggregate(pipeline))

    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in methods_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check} status check")
    print("IPs:")
    for ip_count in ip_counts:
        print(f"\t{ip_count['_id']}: {ip_count['count']}")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_db = client.logs
    nginx_collection = logs_db.nginx

    log_stats(nginx_collection)

