from ..base import BaseField, BaseSchema


class TokenField(BaseField):
    username = BaseField.str_max_100
    password = BaseField.str_max_100


class PostTokenSchema(BaseSchema):
    username = TokenField.username
    password = TokenField.password
