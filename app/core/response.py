from typing import Iterable, Tuple

from flask import jsonify, request
from peewee import ModelSelect
from playhouse.shortcuts import model_to_dict


class ResponseCode(object):
    SUCCESS = 2000

    PERMISSION_DENIED = 4001
    TOKEN_INVALID = 4002
    ERROR = 4003
    PARAM_ERROR = 4004


def model2dict(
    obj,
    *,
    append: dict = None,
    exclude: list = None,
    delete_id: bool = False,
    callback: callable = None,
    before: callable = None,
    only: list = None,
    backrefs=False,
    replace=None,
    recurse=True,
) -> dict:

    model_dict = model_to_dict(obj, exclude=exclude, recurse=recurse, backrefs=backrefs)

    if callable(before):
        values = before(obj) or {}
        for k in values.keys():
            model_dict[k] = values[k]

    if delete_id:
        model_dict.pop("id", None)

    if append:
        assert isinstance(append, dict)
        for key, value in append.items():
            if key not in model_dict.keys():
                model_dict[key] = value

    if exclude:
        if isinstance(exclude, str):
            exclude = [exclude]
        assert isinstance(exclude, list)
        for key in exclude:
            if key in model_dict.keys():
                model_dict.pop(key, None)

    if replace:
        assert isinstance(replace, dict)
        for key, value in replace.items():
            # key存在则替换，不存在则新增
            model_dict[key] = value

    if callback and callable(callback):
        callback(model_dict)

    if only:
        assert isinstance(only, list)
        return_data = dict()
        for k in only:
            return_data[k] = model_dict.get(k, "")
        return return_data

    return model_dict


def success_json(data, **kwargs):
    """Return successful json"""
    result = {"errcode": ResponseCode.SUCCESS, "data": data, **kwargs}
    return jsonify(result)


def error_json(errcode, errmsg, data=None):
    """Return failed json"""
    result = {
        "errcode": errcode,
        "errmsg": errmsg,
        "method": request.method,
        "url": request.url,
        "data": data or {},
    }
    return jsonify(result)


def get_offset(page: int, size: int) -> int:
    return (page - 1) * size


def help_paginate_pee(
    dataset: ModelSelect, page: int, size: int
) -> Tuple[int, Iterable]:
    if isinstance(dataset, list) and not len(dataset):
        return 0, []

    if page == 0:
        total_count = dataset.count()
    else:
        total_count = dataset.count()
        if size == 0:
            return total_count, []
        dataset = dataset.paginate(page, size)
    return total_count, dataset
