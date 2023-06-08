import datetime
from ninja import Field, Router, Schema


class UserCreateSchema(Schema):
    email: str
    username: str
    password: str


class UserLoginSchema(Schema):
    email: str
    password: str


class UserSchema(Schema):
    id = int
    email: str
    username: str


"""
"""


class ProfileSchema(Schema):
    birth_year: int = Field(..., gt=1900, lt=datetime.datetime.now().year)
    weight: float = Field(..., gt=30, lt=300)
    height: float = Field(..., gt=100, lt=250)
