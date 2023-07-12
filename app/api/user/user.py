from flask import render_template

from app.api.shortcuts import *
from app.validator.user import val_user

bp = V1BluePoint("user", url_prefix="")


@bp.route("/users", methods=["POST"])
@validate_schema(val_user.PostUserSchema)
def post_user():
    """
    http http://localhost:5002/api/users username=123 password=123456
    :return:
    """
    if User.get_or_none(User.username == current_schema_data.get("username")):
        return error_json(ResponseCode.DISPLAY_ERRMSG, "User name already exists")

    password = current_schema_data.get("password")
    user = User(**current_schema_data)
    user.password = User.encode_password(password)
    user.save()

    return success_json({"id": user.id})


@bp.route("/users/<int:mid>", methods=["DELETE"])
@anyone_required
def delete_user(mid):
    """
    http DELETE http://localhost:5002/api/users/1 Authorization:"Bearer $JWT"
    :return:
    """
    user = User.get_or_none(User.id == mid)
    if user:
        user.delete_instance()
        return success_json({})
    return error_json(ResponseCode.DISPLAY_ERRMSG, "User not exist")


@bp.route("/users", methods=["GET"])
@anyone_required
@validate_schema(val_user.GetUserSchema)
def get_users():
    """
    http GET http://localhost:5002/api/users Authorization:"Bearer $JWT"
    :return:
    """
    page = current_schema_data.get("page")
    size = current_schema_data.get("size")
    username = current_schema_data.get("username")

    query_set = User.select()
    if username:
        query_set = query_set.where(User.username == username)

    count, users = help_paginate_pee(query_set, page, size)
    return success_json(
        {
            "list": [model2dict(user, exclude=["password"]) for user in users],
            "total_count": count,
        }
    )


@bp.route("/users/password", methods=["PUT"])
@anyone_required
@validate_schema(val_user.PutUserPasswordSchema)
def put_users_password():
    """
    http PUT http://localhost:5002/api/users/password Authorization:"Bearer $JWT"
    :return:
    """
    user_id = g.uid
    user = User.get_or_none(User.id == user_id)
    if not user:
        return error_json(ResponseCode.DISPLAY_ERRMSG, "Please Re Login")
    password = current_schema_data.get("password")
    user.password = User.encode_password(password)
    user.save()
    return success_json({})


@bp.route("/html", methods=["GET"])
def get_html():
    return render_template("hello.html")
