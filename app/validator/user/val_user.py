from marshmallow import fields

from ..base import BaseField, BaseSchema


class UserField(BaseField):
    username = BaseField.username
    password = BaseField.password


class GetUserSchema(BaseSchema):
    page = BaseField.page_
    size = BaseField.size_
    username = fields.String(load_default="", required=False)


class PostUserSchema(BaseSchema):
    username = UserField.username
    password = UserField.password


class DeleteUserSchema(BaseSchema):
    username = UserField.username


class PutUserPasswordSchema(BaseSchema):
    password = UserField.password
