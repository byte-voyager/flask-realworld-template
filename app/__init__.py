import datetime
import decimal
import json
import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from flask import Flask, g
from flask.logging import default_handler
from flask_cors import CORS

from app.api import init_app as init_api
from app.ext import init_app as init_ext
from app.middleware import init_middleware
from config import current_config

# http://127.0.0.1:8989/api/v1/static/1.png
app = Flask(
    __name__,
    static_url_path="/api/v1/static",
    static_folder="./static/",
    template_folder="./templates",
)


def _config_logger(app: Flask):
    app.logger.removeHandler(default_handler)

    fmt = logging.Formatter(
        fmt="[%(levelname)s] %(asctime)s %(filename)s[%(lineno)d, f%(funcName)s] %(message)s"
    )
    fmt2 = logging.Formatter(
        fmt="%(asctime)s [%(process)d] [%(threadName)s(%(thread)d)] [%(name)s] [%(levelname)s(%(levelno)s)] "
        "%(pathname)s.%(filename)s[line:%(lineno)d, funcName:%(funcName)s] %(message)s"
    )

    stream_handler = logging.StreamHandler(stream=sys.stdout)
    stream_handler.setFormatter(fmt)

    app.logger.addHandler(stream_handler)  # print to terminal

    if not os.path.exists(current_config.LOGFILE_DIR):
        os.makedirs(current_config.LOGFILE_DIR, exist_ok=True)

    file_handler = RotatingFileHandler(
        os.path.join(current_config.LOGFILE_DIR, current_config.LOGFILE_NAME),
        maxBytes=current_config.LOGFILE_MAX_SIZE,
        backupCount=current_config.LOGFILE_MAX_COUNT,
        mode="a",
        encoding="utf-8",
    )
    file_handler.setFormatter(fmt2)

    app.logger.addHandler(file_handler)  # save to the file

    file_handler.setLevel(current_config.LOG_LEVEL)
    stream_handler.setLevel(
        logging.DEBUG if current_config.DEBUG else current_config.LOG_LEVEL
    )

    log = logging.getLogger("werkzeug")
    log.setLevel(logging.DEBUG if current_config.DEBUG else current_config.LOG_LEVEL)


class Encoder(json.JSONEncoder):
    def __init__(self, *args, **kwargs):
        super(Encoder, self).__init__(*args, **kwargs)

    def default(self, obj):

        if isinstance(obj, decimal.Decimal):
            return round(float(obj), current_config.DECIMAL_PLACES)

        if isinstance(obj, datetime.datetime):
            if g.get("default_datetime_format"):
                return obj.strftime(g.default_datetime_format)
            return obj.strftime(current_config.DATE_FORMAT)

        if isinstance(obj, datetime.date):
            if g.get("default_datetime_format"):
                return obj.strftime(g.default_datetime_format)
            return obj.strftime(current_config.DATE_DAY_FORMAT)

        if isinstance(obj, set):
            return list(obj)


def create_app(config):
    app.config.from_object(config)

    app.json_encoder = Encoder

    _config_logger(app)

    CORS(app, supports_credentials=True)

    from app.validator.conveter import MongoDBIDConverter, RegexConverter

    app.url_map.converters["re"] = RegexConverter
    app.url_map.converters["mid"] = MongoDBIDConverter

    init_ext(app)
    init_api(app)
    init_middleware(app)

    return app
