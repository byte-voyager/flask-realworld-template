import functools

from flask import _request_ctx_stack, request
from marshmallow import Schema, ValidationError
from werkzeug.local import LocalProxy

from app.response import ResponseCode, error_json
from config import current_config

current_schema_data = LocalProxy(lambda: get_current_schema_data())


def get_current_schema_data():
    return getattr(_request_ctx_stack.top, "schema_data", {})


def validate_schema(schema_class):
    assert issubclass(schema_class, Schema)

    def decorator(view_func):
        @functools.wraps(view_func)
        def inner(*args, **kwargs):
            if request.method == "GET":
                form_data = request.args
            else:
                form_data = request.json
            try:
                data = schema_class().load(form_data)
                # request.schema_data = data
                _request_ctx_stack.top.schema_data = data
            except ValidationError as e:
                if current_config.DEBUG:
                    return error_json(ResponseCode.DISPLAY_ERRMSG, e.messages)
                else:
                    return error_json(ResponseCode.DISPLAY_ERRMSG, "Parameter error")
            return view_func(*args, **kwargs)

        return inner

    return decorator
