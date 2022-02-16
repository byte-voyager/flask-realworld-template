import time
import traceback

from flask import Response, current_app, g, request

from app.ext.database.peewee_db import ms_db
from app.response import ResponseCode, error_json
from config import current_config


def handler_405(e):
    if current_app.debug:
        return error_json(405, str(e))
    # Not in development mode, we change to 404 for any 405
    return Response(status=404)


def handler_500(e):
    data = f"""
    original_exception: {e.original_exception} \n
    request.url: {request.url} \n
    request.method: {request.method} \n
    request.args: {request.args} \n
    request.json: {request.json} \n
    request.headers: {request.headers} \n
    Exception: \n
    {traceback.format_exc()}
    """
    current_app.logger.exception("Internal server error")
    current_app.logger.error(str(data))

    exc_repr = str(e.original_exception).lower()

    if "1064" in exc_repr:
        return error_json(
            ResponseCode.DISPLAY_ERRMSG, "Database syntax errors", data=f"{exc_repr}"
        )

    if "1062" in exc_repr:
        return error_json(
            ResponseCode.DISPLAY_ERRMSG,
            "The only conflict database data",
            data=f"{exc_repr}",
        )

    if "instance matching query does not exist" in exc_repr:
        return error_json(
            ResponseCode.DISPLAY_ERRMSG,
            "Data does not exist, not get at least 1 the data",
            data=f"{exc_repr}",
        )

    if "1451" in exc_repr:
        return error_json(
            ResponseCode.DISPLAY_ERRMSG,
            "There are other associated data",
            data=f"{exc_repr}",
        )

    # This returns the HTTP status code is 200
    return error_json(
        ResponseCode.DISPLAY_ERRMSG, "Internal server error", data=f"{exc_repr}"
    )


def handler_404(e):
    if current_config.DEBUG:
        return error_json(
            404, "Interface is not found, please check whether the interface is correct"
        )
    return Response(status=404)


def before_request():
    g.start_time = time.time()


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def after_request(response):
    if current_config.DEBUG:
        used_time = time.time() - g.start_time
        if used_time > 0.6:
            print(
                f"{bcolors.WARNING}Route: {request.path}\
               Time used: {used_time}{bcolors.ENDC}"
            )
        else:
            print(
                f"{bcolors.OKGREEN}Route: {request.path}\
               Time used: {used_time}{bcolors.ENDC}"
            )
    return response


def teardown_request(response):
    if not ms_db.is_closed():
        ms_db.close()
