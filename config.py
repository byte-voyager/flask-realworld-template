class BaseConfig(object):
    DEBUG = True

    LOGFILE_DIR = "./log_files/"
    LOGFILE_NAME = "app.log"
    LOGFILE_MAX_SIZE = 5
    LOGFILE_MAX_COUNT = 10
    LOG_LEVEL = 12
    DATE_FORMAT = "%y-%m-%d %h:%m:%s"
    DATE_FORMAT2 = "%y-%m-%d_%h:%m:%s"
    DATE_DAY_FORMAT = "%y-%m-%d"

    JWT_SECRET_KEY = ""
    JWT_ACCESS_TOKEN_EXPIRES = 3600

    FLASK_PYDANTIC_VALIDATION_ERROR_RAISE = True

    db_pg_name = "db_test"
    db_pg_host = "127.0.0.1"
    db_pg_port = 5432
    db_pg_user = "root"
    db_pg_password = "123456"

    db_redis_user = ""
    db_redis_password = ""
    db_redis_port = 6379
    db_redis_host = "127.0.0.1"


current_config = BaseConfig()
