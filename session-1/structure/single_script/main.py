#!/usr/bin/env python3

import redis

def connect_redis(server, port):
   redis_conn = redis.StrictRedis(host=server,
                                       port=port,
                                       db=0,
                                       charset="utf-8",
                                       decode_responses=True)
   return redis_conn


def set_key(redis_conn, key, value):
    redis_conn.set(key, value)


def get_key(redis_conn, key):
    response = redis_conn.get(key)
    return response


def main():
    server = "localhost"
    port ="6379"
    redis_conn = connect_redis(server, port)
    set_key(redis_conn, "key1", "value1")
    value = get_key(redis_conn, "key1")
    print("The value is {}".format(value))


if __name__ == '__main__':
    main()
