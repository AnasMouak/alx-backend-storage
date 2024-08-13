#!/usr/bin/env python3
"""Log stats"""
from pymongo import MongoClient


def log_stats():
    """Provides some stats about Nginx logs"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of logs
    log_count = collection.count_documents({})
    print(f"{log_count} logs")

    # Count the number of occurrences for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Count the number of logs with method GET and path /status
    status_check_count = collection.count_documents({"method": "GET",
                                                    "path": "/status"})
    print(f"{status_check_count} status check")

    # Top 10 most present IPs
    print("IPs:")
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    top_ips = collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
