#!/usr/bin/env python3
"""Writing strings to Redis"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator that counts the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count calls."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """Create a Cache class"""
    def __init__(self):
        """store an instance of the Redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a random key, store data in Redis, and return the key."""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes,
                                                    int, float, None]:
        """
        Retrieve data from Redis and optionally
        apply a conversion function.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis."""
        return self.get(key, int)
