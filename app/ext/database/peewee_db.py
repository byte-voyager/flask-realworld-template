from abc import ABC

from peewee import PostgresqlDatabase
from playhouse.shortcuts import ReconnectMixin

from config import current_config


class ReconnectPostgresqlDatabase(ReconnectMixin, PostgresqlDatabase, ABC):
    pass


pg_db = ReconnectPostgresqlDatabase(
    current_config.db.pg.name,
    host=current_config.db.pg.host,
    port=current_config.db.pg.port,
    user=current_config.db.pg.user,
    password=current_config.db.pg.password,
    autorollback=True,
    autoconnect=True,
    thread_safe=True,
)

if __name__ == "__main__":
    pg_db.connect()
    print(pg_db.is_connection_usable())
