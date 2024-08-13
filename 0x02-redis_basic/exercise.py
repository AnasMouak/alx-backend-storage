#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """Create a Cache class"""
    def __init__(self):
        """store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store data in Redis, and return the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
