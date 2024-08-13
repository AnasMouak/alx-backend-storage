#!/usr/bin/env python3
"""Top students"""
import pymongo


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.

    :param mongo_collection: The pymongo collection object
    :return: List of students sorted by their average score with key
    'averageScore'
    """
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
