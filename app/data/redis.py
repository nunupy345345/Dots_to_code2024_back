import os

import redis


class RedisClient:
    def __init__(self):
        if os.environ.get("ENV") == "production":
            self.redis = redis.StrictRedis(host=os.environ.get("REDIS_HOST"), port=int(os.environ.get("REDIS_PORT")),
                                           password=os.environ.get("REDIS_PASSWORD"),
                                           ssl=True,
                                           db=0)
        else:
            self.redis = redis.StrictRedis(host=os.environ.get("REDIS_HOST"), port=6379, db=0)
