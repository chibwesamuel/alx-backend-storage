# Redis basic

This repository contains code related to Redis, a popular in-memory data store. It includes tasks and exercises to familiarize users with Redis concepts and Python integration.

## Installation
To get started, I installed Redis on my Ubuntu 18.04 machine. Here are the steps I followed:

    First, I installed the Redis server using the command: sudo apt-get -y install redis-server
    To work with Redis in Python, I installed the Redis Python library with: pip3 install redis
    To ensure Redis binds to localhost, I made the necessary configuration change using: sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf

## Using Redis in a Container
When using Redis within a container, it's important to note that the Redis server is stopped by default. So, whenever I start a container, I always remember to start the Redis server using the command: service redis-server start.

### Task 0 - Writing Strings to Redis
In this task, I created a Cache class that interacts with Redis to store and retrieve data. During the class initialization, I instantiated a Redis client and flushed the database using flushdb.

The store method takes some data as input, generates a random key (using uuid), stores the input data in Redis using the generated key, and then returns the key.

### Task 1 - Reading from Redis and Recovering Original Type
To extend the functionality of the Cache class, I implemented two additional methods - get_str and get_int. These methods automatically parametrize the Cache.get method with the correct conversion functions for strings and integers, respectively.

### Task 2 - Incrementing Values
In this task, I implemented a count_calls decorator to keep track of how many times methods of the Cache class are called. The decorator uses the qualified name of the method (using __qualname__) as the key and increments the count for that key each time the method is called. To preserve the original function's name and other attributes, I used functools.wraps.

### Task 3 - Storing Lists
For this task, I implemented a call_history decorator to store the history of inputs and outputs for a particular function. The decorator appends the input parameters and output results to two separate lists in Redis, using the qualified name of the decorated function and adding ":inputs" and ":outputs" to create the appropriate key.

### Task 4 - Retrieving Lists
To visualize the history of calls for the Cache.store method, I created a replay function. This function retrieves the stored inputs and outputs for the method from Redis and presents them in a formatted output.

### Task 5 - Implementing an Expiring Web Cache and Tracker (Advanced)
In a separate file named web.py, I implemented the get_page function, which is designed to fetch the HTML content of a given URL. I incorporated Redis to track the number of times a specific URL was accessed, using a key in the format "count:{url}". Additionally, I cached the result of the HTTP request in Redis with a short expiration time of 10 seconds to improve performance and response times.

### Bonus Task
In the web.py file, I provided an alternative implementation of the get_page function using decorators to achieve caching and tracking functionalities.
