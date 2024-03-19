import redis


class RedisClient:
    def __init__(self):
        self.redis = redis.StrictRedis(host='localhost', port=6379, db=0)

