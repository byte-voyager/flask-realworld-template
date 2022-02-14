from flask_jwt_extended import JWTManager

from .database import app_init as database_init


def init_app(app):
    database_init(app)
    JWTManager(app)
