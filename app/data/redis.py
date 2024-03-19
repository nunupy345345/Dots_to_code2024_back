import os

import redis


class RedisClient:
    def __init__(self):
        self.redis = redis.StrictRedis(host=os.environ.get("REDIS_HOST"), port=6379, db=0)
