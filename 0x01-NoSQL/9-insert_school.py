#!/usr/bin/env python3
"""Insert a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    :param mongo_collection: The pymongo collection object
    :param kwargs: Key-value pairs to be inserted as the document
    :return: The _id of the inserted document
    """
    return mongo_collection.insert_one(kwargs).inserted_id
