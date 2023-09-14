#!/usr/bin/env python3
"""
web.py - A module to implement an expiring web cache and tracker.
"""

import requests
import redis
import time
from typing import Callable


def get_page(url: str) -> str:
    """
    Fetch the HTML content of the given URL and cache the result with an
    expiration time of 10 seconds.

    Args:
        url (str): The URL to fetch HTML content from.

    Returns:
        str: The HTML content of the given URL.
    """
    # Initialize Redis client
    redis_client = redis.Redis()

    # Check if the URL is already cached
    cached_result = redis_client.get(url)
    if cached_result:
        print(f"Cache hit for URL: {url}")
        return cached_result.decode("utf-8")

    try:
        # If not cached, fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Cache the response with a 10-second expiration time
        redis_client.setex(url, 10, response.text)

        # Track the number of times the URL was accessed
        redis_client.incr(f"count:{url}")

        print(f"Cache miss for URL: {url}")
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {url} - {e}")
        return ""


if __name__ == "__main__":
    # Test the get_page function
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))  # Return from cache due to the 10-second expiration
