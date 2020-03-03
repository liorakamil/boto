""" Redis operation package """
#!/usr/bin/env python3

import logging
import redis
import config


class RedisOps():
    """
    Redis operation, ex: Creating connection, getting lock, etc
    """
    def __init__(self):
        """
        Initialize server and port and call connect_redis to initiate
        connection to redis for operations (EX: get, set, etc)
        """

        self.server = config.REDIS_SERVER
        self.port = config.REDIS_PORT
        self.redis_conn = self.connect_redis()


    def connect_redis(self):
        """
        This function create a connection to redis and return
        a connection reference
        :return: reference to redis connection
        """
        try:
            redis_conn = redis.StrictRedis(host=self.server,
                                           port=self.port,
                                           db=0,
                                           charset="utf-8",
                                           decode_responses=True)
        except Exception as error:
            logging.error("Failed to connect to redis server: %s,"
                          " with error: %s",
                          self.server, error)
        return redis_conn


    def set_key(self, key, value):
        """
        This function accept key value and operate set in redis
        :param key: String of key to set
        :param value: String of value to set
        :return: None
        """
        try:
            self.redis_conn.set(key, value)
        except Exception as error:
            logging.error("Failed to set to redis: %s,"
                          " with error: %s",
                          self.server, error)


    def get_key(self, key):
        """
        Get value according to key
        :param key: String of key to get
        :return: String og value
        """
        try:
            response = self.redis_conn.get(key)
            return response
        except Exception as error:
            logging.error("Failed to get from redis: %s,"
                          " with error: %s",
                          self.server, error)
