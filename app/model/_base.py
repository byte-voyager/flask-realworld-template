import datetime

from peewee import DateTimeField, Model

from app.core.database.peewee_db import pg_db


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = pg_db
