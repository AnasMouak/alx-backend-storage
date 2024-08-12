#!/usr/bin/env python3
"""List all documents in Python"""
import pymongo


def list_all(mongo_collection):
    """
    Lists all documents in a collection.

    :param mongo_collection: The pymongo collection object
    :return: A list of documents, or an empty list if the collection is empty
    """
    return list(mongo_collection.find())
