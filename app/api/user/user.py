from flask import render_template

from app.help.shortcuts import *
from app.validator.user import val_user

bp = Blueprint("user", __name__, url_prefix="")


@bp.route("/users", methods=["POST"])
@validate()
def post_user(body: val_user.PostUserSchema):
    """
    http http://localhost:5002/api/users username=123 password=123456
    :return:
    """
    if User.get_or_none(User.username == body.username):
        return error_json(ResponseCode.ERROR, "User name already exists")

    user = User(**body.model_dump())
    user.password = User.encode_password(body.password)
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
    return error_json(ResponseCode.ERROR, "User not exist")


@bp.route("/users", methods=["GET"])
@anyone_required
@validate()
def get_users(query: val_user.GetUserSchema):
    """
    http GET http://localhost:5002/api/users Authorization:"Bearer $JWT"
    :return:
    """
    page = query.get("page")
    size = query.get("size")
    username = query.get("username")

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
@validate()
def put_users_password(body: val_user.PutUserPasswordSchema):
    """
    http PUT http://localhost:5002/api/users/password Authorization:"Bearer $JWT"
    :return:
    """
    user_id = g.uid
    user = User.get_or_none(User.id == user_id)
    if not user:
        return error_json(ResponseCode.ERROR, "Please Re Login")
    password = body.password
    user.password = User.encode_password(password)
    user.save()
    return success_json({})


@bp.route("/html", methods=["GET"])
def get_html():
    return render_template("hello.html")
