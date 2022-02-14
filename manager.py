import sys
from optparse import OptionParser

import pymysql

from app import create_app
from config import current_config

app = create_app(config="config.current_config")


def runserver(port):
    app.run(host="0.0.0.0", port=port, threaded=True)


def create_table():
    conn = pymysql.connect(
        host=current_config.MYSQL_SETTINGS["host"],
        port=current_config.MYSQL_SETTINGS["port"],
        user=current_config.MYSQL_SETTINGS["user"],
        password=current_config.MYSQL_SETTINGS["password"],
    )
    try:
        conn.cursor().execute(f'CREATE DATABASE {current_config.MYSQL_SETTINGS["db"]}')
    except pymysql.err.ProgrammingError:
        pass
    conn.close()
    from app.ext.database.peewee_db import ms_db
    from app.model.user import User

    ms_db.create_tables([User])


def drop_table():
    from app.ext.database.peewee_db import ms_db
    from app.model.user import User

    y = input("Delete all tables？y/N")
    if y == "y":
        ms_db.drop_tables([User])


def main():
    usage = " %s [Options] \n\t%s runserver (run develop web server)" % (
        sys.argv[0],
        sys.argv[0],
    )
    parser = OptionParser(usage=usage)
    parser.add_option(
        "-c",
        "--create_table",
        dest="create_table",
        action="store_true",
        default=False,
        help="create table",
    )
    parser.add_option(
        "-d",
        "--drop_table",
        dest="drop_table",
        action="store_true",
        default=False,
        help="drop table",
    )
    parser.add_option(
        "-p",
        "--port",
        default=8989,
        dest="port",
        help="listen port",
    )

    options, args = parser.parse_args()

    if options.create_table:
        create_table()
        return

    if options.drop_table:
        drop_table()
        return

    runserver(options.port)


if __name__ == "__main__":
    main()
