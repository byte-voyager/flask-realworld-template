from ..base import BaseField, BaseSchema


class UserField(BaseField):
    username = BaseField.username
    password = BaseField.password


class GetUserSchema(BaseSchema):
    page = BaseField.page_
    size = BaseField.size_


class PostUserSchema(BaseSchema):
    username = UserField.username
    password = UserField.password


class DeleteUserSchema(BaseSchema):
    username = UserField.username


class PutUserPasswordSchema(BaseSchema):
    password = UserField.password
