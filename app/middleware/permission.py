import functools

from flask import g
from flask_jwt_extended import get_jwt, get_jwt_identity, verify_jwt_in_request

from app.core.response import ResponseCode, error_json
from app.model.user import ConstUserType, User
from config import current_config


def anyone_required(view_func):
    @functools.wraps(view_func)
    def inner(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception:
            if current_config.DEBUG and current_config.DEBUG_IGNORE_AUTH:
                user: User = User.select().first()

                if not user:
                    return error_json(ResponseCode.TOKEN_INVALID, "No user")

                g.uid = user.id
                g.username = user.username
                g.claims = {"username": user.username}
                return view_func(*args, **kwargs)
            else:
                return error_json(
                    ResponseCode.TOKEN_INVALID, errmsg="The token is missing"
                )

        uid = get_jwt_identity()
        if not uid:
            return error_json(
                ResponseCode.TOKEN_INVALID, errmsg="The token expired or invalid"
            )
        claims = get_jwt()
        g.uid = uid
        g.username = claims.get("username")
        g.claims = claims
        return view_func(*args, **kwargs)

    return inner


def admin_required(view_func):
    @functools.wraps(view_func)
    def inner(*args, **kwargs):
        try:
            verify_jwt_in_request()
        except Exception:
            if current_config.DEBUG and current_config.DEBUG_IGNORE_AUTH:
                user: User = User.select().first()

                if not user:
                    return error_json(ResponseCode.TOKEN_INVALID, "No user")

                g.uid = user.id
                g.username = user.username
                g.claims = {"username": user.username}
                return view_func(*args, **kwargs)
            else:
                return error_json(
                    ResponseCode.TOKEN_INVALID, errmsg="The token is missing"
                )

        uid = get_jwt_identity()
        if not uid:
            return error_json(
                ResponseCode.TOKEN_INVALID, errmsg="The token expired or invalid"
            )

        user: User = User.select(User.type).where(User.id == uid).first()
        if not user:
            return error_json(
                ResponseCode.TOKEN_INVALID,
                errmsg="Token of failure, please login again",
            )

        if user.type != ConstUserType.TYPE_ADMIN:
            return error_json(
                ResponseCode.PERMISSION_DENIED,
                errmsg="Token of failure, please login again",
            )

        claims = get_jwt()
        g.uid = uid
        g.username = claims.get("username")
        g.claims = claims
        return view_func(*args, **kwargs)

    return inner
