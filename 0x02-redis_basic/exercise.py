#!/usr/bin/env python3
"""
Cache class to interact with Redis.
"""

import redis
import uuid
from typing import Union, Optional, Callable
import functools

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

    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count how many times a method is called.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            key = method.__qualname__
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper

    def call_history(method: Callable) -> Callable:
        """
        Decorator to store the history of inputs and outputs for a method.

        Args:
            method (Callable): The method to be decorated.

        Returns:
            Callable: The decorated method.
        """
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"

            self._redis.rpush(inputs_key, str(args))

            result = method(self, *args, **kwargs)

            self._redis.rpush(outputs_key, result)

            return result

        return wrapper

    def replay(self, method: Callable) -> None:
        """
        Display the history of calls of a particular function.

        Args:
            method (Callable): The method to retrieve history for.

        Returns:
            None
        """
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        inputs = self._redis.lrange(inputs_key, 0, -1)
        outputs = self._redis.lrange(outputs_key, 0, -1)

        for input_args, output in zip(inputs, outputs):
            input_str = input_args.decode("utf-8")
            output_str = output.decode("utf-8")

            print(f"{method.__qualname__}{input_str} -> {output_str}")

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the input data in Redis with a random key and return the key.
        This method is decorated with count_calls and call_history to track its usage and store history.

        Args:
            data (Union[str, bytes, int, float]): Data to be stored in Redis.

        Returns:
            str: The generated random key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

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

    # Test counting method calls
    cache.store(b"first")
    print(cache.get(cache.store.__qualname__))  # Output: b'1'

    cache.store(b"second")
    cache.store(b"third")
    print(cache.get(cache.store.__qualname__))  # Output: b'3'

    # Test call history
    s1 = cache.store("first")
    s2 = cache.store("second")
    s3 = cache.store("third")

    cache.replay(cache.store)

