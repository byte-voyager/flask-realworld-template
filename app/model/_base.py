import datetime

from peewee import DateTimeField, Model

from app.ext.database.peewee_db import ms_db


class BaseModel(Model):
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = ms_db
