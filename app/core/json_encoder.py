import decimal
from datetime import date, datetime

from flask import g
from flask.json.provider import DefaultJSONProvider

from config import current_config


class UpdatedJSONProvider(DefaultJSONProvider):
    def __init__(self, *args, **kwargs):
        super(UpdatedJSONProvider, self).__init__(*args, **kwargs)

    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            if g.get("decimal_places"):
                return round(float(obj), g.get("decimal_places"))
            return round(float(obj), current_config.DECIMAL_PLACES)

        if isinstance(obj, datetime):
            if g.get("default_datetime_format"):
                return obj.strftime(g.default_datetime_format)

            return obj.strftime(current_config.DATE_FORMAT)

        if isinstance(obj, date):
            if g.get("default_datetime_format"):
                return obj.strftime(g.default_datetime_format)
            return obj.strftime(current_config.DATE_DAY_FORMAT)

        if isinstance(obj, set):
            return list(obj)
