from flask import Flask

from .user import init_api as init_user_api

"""This module is mainly used to register blueprints"""


def init_app(app: Flask):
    init_user_api(app)
