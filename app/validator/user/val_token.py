from pydantic import BaseModel


class TokenField(BaseModel):
    username: str
    password: str


class PostTokenSchema(BaseModel):
    username: str
    password: str
