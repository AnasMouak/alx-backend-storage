#!/usr/bin/env python3
"""returns the list of school having a specific topic"""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    :param mongo_collection: The pymongo collection object
    :param topic: The topic searched
    :return: List of schools with the specific topic
    """
    return mongo_collection.find({"topics": topic})
