#!/usr/bin/env python3
"""
Returns all students sorted by average score
mongo_collection will be the pymongo collection object
The top must be ordered
The average score must be part of each item returned with key = averageScore
"""

from pymongo import MongoClient

def top_students(mongo_collection):
    """
    Returns a list of students sorted by their average score
    """
    pipeline = [
        {"$unwind": "$topics"},
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

