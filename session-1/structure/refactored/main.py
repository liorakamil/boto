#!/usr/bin/env python3
""" Main program to demonstrate redis operations """

from redisops import RedisOps as redisc

def main():
    """
    main function to demonstrate redis operations
    :return: None
    """
    redis_ops = redisc()
    redis_ops.connect_redis()
    redis_ops.set_key("key1", "value1")
    value = redis_ops.get_key("key1")
    print("The value is {}".format(value))


if __name__ == "__main__":
    main()
