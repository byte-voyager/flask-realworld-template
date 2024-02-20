from flask import Flask

from app.help.bp import register_api_v1

from .user.token import bp as token_bp
from .user.user import bp as user_bp


def init_app(app: Flask):
    register_api_v1(app, token_bp)
    register_api_v1(app, user_bp)
