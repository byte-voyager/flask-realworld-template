from abc import ABC

from peewee import MySQLDatabase
from playhouse.shortcuts import ReconnectMixin

from config import current_config


class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase, ABC):
    pass


ms_db = ReconnectMySQLDatabase(
    current_config.MYSQL_SETTINGS["db"],
    host=current_config.MYSQL_SETTINGS["host"],
    port=current_config.MYSQL_SETTINGS["port"],
    user=current_config.MYSQL_SETTINGS["user"],
    password=current_config.MYSQL_SETTINGS["password"],
    autorollback=True,
    autoconnect=True,
    thread_safe=True,
)

if __name__ == "__main__":
    ms_db.connect()
    print(ms_db.is_connection_usable())
