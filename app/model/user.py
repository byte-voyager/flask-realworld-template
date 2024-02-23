from peewee import *
from werkzeug.security import check_password_hash, generate_password_hash

from ._base import BaseModel


class ConstUserType:
    TYPE_NORMAL = 1
    TYPE_ADMIN = 2


class User(BaseModel):
    id = AutoField()
    username = CharField(max_length=255, null=False, help_text="", unique=True)
    nickname = CharField(max_length=255, null=True, help_text="")
    password = CharField(max_length=1000, null=True, help_text="")
    type = SmallIntegerField(default=1, null=True)

    @staticmethod
    def encode_password(password):
        if not password:
            return None
        return generate_password_hash(password)

    @staticmethod
    def check_password(encode_password, orig_password) -> bool:
        """Check whether the password is consistent
        @param encode_password After the encrypted password
        @param orig_password Clear text passwords
        """
        if not encode_password:
            return False
        return check_password_hash(encode_password, orig_password)
