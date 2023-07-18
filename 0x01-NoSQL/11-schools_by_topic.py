#!/usr/bin/env python3
"""
Returns the list of schools having a specific topic
mongo_collection will be the pymongo collection object
topic (string) will be the topic searched
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools that have the specified topic
    in the pymongo collection object.
    """
    return list(mongo_collection.find({"topics": topic}))

