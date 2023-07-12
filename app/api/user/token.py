from flask_jwt_extended import create_access_token

from app.api.shortcuts import *
from app.validator.user import val_token

bp = V1BluePoint("api_token", url_prefix="")


@bp.route("/token", methods=["POST"])
@validate_schema(val_token.PostTokenSchema)
def post_token():
    """
    http http://localhost:5002/api/token username=123 password=123456
    :return:
    """
    username = current_schema_data.get("username")
    password = current_schema_data.get("password")

    user: User = (
        User.select(User.username, User.id, User.password)
        .where(User.username == username)
        .first()
    )

    if not user:
        return error_json(ResponseCode.DISPLAY_ERRMSG, "No user")

    if not User.check_password(user.password, password):
        return error_json(ResponseCode.DISPLAY_ERRMSG, "Incorrect username or password")

    token = create_access_token(
        identity=user.id, additional_claims={"username": username}
    )
    for k, v in current_config.items():
        print(k, "=", v)
    return success_json({"token": token})
