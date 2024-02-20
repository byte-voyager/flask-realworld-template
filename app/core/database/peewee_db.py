from abc import ABC

from peewee import PostgresqlDatabase
from playhouse.shortcuts import ReconnectMixin

from config import current_config


class ReconnectPostgresqlDatabase(ReconnectMixin, PostgresqlDatabase, ABC):
    pass


pg_db = ReconnectPostgresqlDatabase(
    current_config.db_pg_name,
    host=current_config.db_pg_host,
    port=current_config.db_pg_port,
    user=current_config.db_pg_user,
    password=current_config.db_pg_password,
    autorollback=True,
    autoconnect=True,
    thread_safe=True,
)

if __name__ == "__main__":
    pg_db.connect()
    print(pg_db.is_connection_usable())
