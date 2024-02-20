from pydantic import BaseModel


class UserField(BaseModel):
    username: str
    password: str


class GetUserSchema(BaseModel):
    page: int
    size: int
    username: str


class PostUserSchema(BaseModel):
    username: str
    password: str


class DeleteUserSchema(BaseModel):
    username: str


class PutUserPasswordSchema(BaseModel):
    password: str
