from flask import Flask

from .token import bp as token_bp
from .user import bp as user_bp


def init_api(app: Flask):
    app.register_blueprint(token_bp)
    app.register_blueprint(user_bp)
