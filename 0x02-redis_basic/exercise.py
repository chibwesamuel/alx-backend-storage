#!/usr/bin/env python3
"""
Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union, Optional, Callable

class Cache:
    """
    Cache class to interact with Redis.
    """

    def __init__(self) -> None:
        """
        Initialize a Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): Data to be stored in Redis.

        Returns:
            str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        Retrieve the data associated with the given key from Redis.
        If a conversion function (fn) is provided, use it to convert the data back to the desired format.

        Args:
            key (str): The key to retrieve data from Redis.
            fn (Optional[Callable]): The callable to convert the data (default is None).

        Returns:
            Union[str, bytes, int, float]: The retrieved data from Redis.
        """
        data = self._redis.get(key)
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        """
        Retrieve the data associated with the given key from Redis as a string.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            str: The retrieved data from Redis as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve the data associated with the given key from Redis as an integer.

        Args:
            key (str): The key to retrieve data from Redis.

        Returns:
            int: The retrieved data from Redis as an integer.
        """
        return self.get(key, fn=int)

if __name__ == "__main__":
    cache = Cache()

    # Test storing and retrieving data from Redis with conversion
    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

