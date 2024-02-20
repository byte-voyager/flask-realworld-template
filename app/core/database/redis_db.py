import json

from flask import current_app
from redis import Redis

from config import current_config


class RedisDB(object):
    def __init__(self, db):
        self._conn = Redis(
            db=db,
            username=current_config.REDIS_USERNAME,
            port=current_config.REDIS_PORT,
            password=current_config.REDIS_PASSWORD,
        )

    @property
    def conn(self):
        return self._conn

    def set_dict(self, key: str, value, expr=None):
        if not expr and self._conn.ttl(key) >= 0:
            expr = self._conn.ttl(key)
        if isinstance(value, dict):
            value = json.dumps(value)
        self._conn.set(key, value, ex=expr)
        return key

    def get_dict(self, key, dumps=True):
        value = self._conn.get(key)
        if value and dumps:
            try:
                value = value.decode()
                value = json.loads(value)
            except Exception as e:
                current_app.logger.error(e)
                return None
            else:
                return value
        return value

    def get_str(self, key):
        value = self._conn.get(key)
        if value:
            value = value.decode()
        return value

    def delete(self, token):
        return self._conn.delete(token)


r_db = RedisDB(db=0)
