from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager

from app.api import init_app as init_api
from app.core.json_encoder import UpdatedJSONProvider
from app.core.logger import config_logger
from app.middleware import init_middleware
from config import current_config

# http://127.0.0.1:8989/api/v1/static/1.png
app = Flask(
    __name__,
    static_url_path="/api/v1/static",
    static_folder="./static/",
    template_folder="./templates",
)


def create_app(config):
    app.config.from_object(config)

    app.json = UpdatedJSONProvider(app)

    config_logger(app, current_config)

    CORS(app, supports_credentials=True)

    JWTManager(app)

    from app.validator.conveter import RegexConverter

    app.url_map.converters["re"] = RegexConverter

    init_api(app)
    init_middleware(app)

    return app
