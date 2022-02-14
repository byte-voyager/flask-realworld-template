import logging
import os
import platform


class ImmutableObject(object):
    def __setattr__(self, key, value):
        raise AttributeError("Cannot reassign/assign members")

    def __call__(self, *args, **kwargs):
        return self


class BaseConfig(ImmutableObject):
    DEBUG = True
    DEBUG_IGNORE_AUTH = False

    # JWT CONFIG
    JWT_SECRET_KEY = "yRVHDTLfpoKGDJyfK9aTAAJ3uELNPxH9"
    JWT_ACCESS_TOKEN_EXPIRES = 3600 * 24 * 7  # 7 days

    # Log file config
    LOGFILE_DIR = "./log_files/"
    LOGFILE_NAME = "app.log"
    LOGFILE_MAX_SIZE = 5 * 1024 * 1024  # 5M
    LOGFILE_MAX_COUNT = 10
    LOG_LEVEL = logging.INFO

    DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    DATE_FORMAT2 = "%Y-%m-%d_%H:%M:%S"
    DATE_DAY_FORMAT = "%Y-%m-%d"

    MYSQL_SETTINGS = {
        "db": "db_test",
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "baloneolike@x",
    }

    REDIS_USERNAME = ""
    REDIS_PASSWORD = ""
    REDIS_PORT = 6379


class TestConfig(BaseConfig):
    DEBUG = (
        True if os.getenv("XDG_CURRENT_DESKTOP") else False
    )  # The retrieval system is a desktop environment

    if platform.system().lower() == "windows":  # Debug when system is windows
        DEBUG = True

    if os.getenv("OFF_DEBUG"):
        DEBUG = False

    MYSQL_SETTINGS = {
        "db": "db_test",
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "baloneolike@x",
    }


class ProdConfig(BaseConfig):
    DEBUG = False
    MYSQL_SETTINGS = {
        "db": "db_test",
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "baloneolike@x",
    }


current_config = ProdConfig() if os.getenv("PROD_MODE") else TestConfig()
