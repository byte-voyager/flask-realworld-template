from flask_jwt_extended import create_access_token

from app.help.shortcuts import *
from app.validator.user import val_token

bp = Blueprint("api_token", __name__, url_prefix="")


@bp.route("/token", methods=["POST"])
@validate()
def post_token(schema: val_token.PostTokenSchema):
    """
    http http://localhost:5002/api/token username=123 password=123456
    :return:
    """
    username = schema.username
    password = schema.password

    user: User = (
        User.select(User.username, User.id, User.password)
        .where(User.username == username)
        .first()
    )

    if not user:
        return error_json(ResponseCode.ERROR, "No user")

    if not User.check_password(user.password, password):
        return error_json(ResponseCode.ERROR, "Incorrect username or password")

    token = create_access_token(
        identity=user.id, additional_claims={"username": username}
    )
    for k, v in current_config.items():
        print(k, "=", v)
    return success_json({"token": token})
