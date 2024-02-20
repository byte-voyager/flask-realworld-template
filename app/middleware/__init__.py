from flask import Flask
from flask_pydantic import ValidationError

from .handler import (after_request, before_request, handle_validate_exception,
                      handler_404, handler_405, handler_500, teardown_request)


def init_middleware(app: Flask):
    app.register_error_handler(404, handler_404)
    app.register_error_handler(500, handler_500)
    app.register_error_handler(405, handler_405)
    app.register_error_handler(ValidationError, handle_validate_exception)
    app.before_request(before_request)
    app.after_request(after_request)
    app.teardown_request(teardown_request)
