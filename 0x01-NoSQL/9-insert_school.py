#!/usr/bin/env python3
"""
Inserts a new document in a collection based on kwargs
mongo_collection will be the pymongo collection object
Returns the new _id
"""

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the pymongo collection object
    based on the provided kwargs. Returns the new _id.
    """
    return mongo_collection.insert_one(kwargs).inserted_id

