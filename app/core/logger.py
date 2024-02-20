import logging
import os
import sys
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.logging import default_handler


def config_logger(app: Flask, current_config):
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
