from playhouse.pool import PooledPostgresqlExtDatabase

from config import current_config

pg_db = PooledPostgresqlExtDatabase(
    current_config.db_pg_name,
    host=current_config.db_pg_host,
    port=current_config.db_pg_port,
    user=current_config.db_pg_user,
    password=current_config.db_pg_password,
    max_connections=4,
    stale_timeout=500,
    autorollback=True,
    autoconnect=True,
    thread_safe=True,
)

if __name__ == "__main__":
    pg_db.connect()
    print(pg_db.is_connection_usable())
