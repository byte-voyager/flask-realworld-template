import datetime
import time

from marshmallow import EXCLUDE, Schema, ValidationError, fields, validate


class BaseSchema(Schema):
    class Meta:
        unknown = EXCLUDE  # Remove undefined fields

    _default_error_messages = {
        "type": "Submit data format error, need is a JSON object"
    }


class TimestampToUTCDateTime(fields.Int):
    def _deserialize(self, value, attr, data, **kwargs):
        try:
            value = int(value)
            tmp_data = datetime.datetime.utcfromtimestamp(value)
        except Exception:
            raise ValidationError(f"Timestamp is accurate to seconds")
        else:
            return tmp_data


class BaseField(object):
    """To preach not parameters, we end with a single underscore and set up the load_default values"""

    page_ = fields.Int(validate=validate.Range(min=0), load_default=0)
    size_ = fields.Int(validate=validate.Range(min=0, max=100), load_default=0)
    order_ = fields.String(validate=validate.Length(min=1), load_default="desc")
    start_timestamp_ = fields.Int(validate=validate.Range(min=0), load_default=0)
    start_timestamp = fields.Int(validate=validate.Range(min=0), required=True)
    end_timestamp_ = fields.Int(validate=validate.Range(min=0), load_default=time.time)
    end_timestamp = fields.Int(validate=validate.Range(min=0), required=True)

    email = fields.Str(
        required=True, validate=validate.Email(error="Is not a valid email address")
    )

    timestamp2utc_datetime = TimestampToUTCDateTime(required=True)
    timestamp2utc_datetime_default_0_ = TimestampToUTCDateTime(
        required=False, load_default=0
    )
    timestamp2utc_datetime_default_now_ = TimestampToUTCDateTime(
        required=False, load_default=datetime.datetime.utcnow
    )

    str_max_100 = fields.String(validate=validate.Length(min=1, max=100), required=True)
    str_max_100_ = fields.String(
        validate=validate.Length(min=0, max=100), load_default="", required=False
    )
    str_max_500 = fields.String(validate=validate.Length(min=1, max=500), required=True)
    str_max0_500 = fields.String(
        validate=validate.Length(min=0, max=500), required=True
    )
    str_max_500_ = fields.String(
        validate=validate.Length(min=0, max=500), load_default="", required=False
    )
    str_max_1000 = fields.String(
        validate=validate.Length(min=0, max=1000), required=True
    )
    str_max_1000_ = fields.String(
        validate=validate.Length(min=0, max=1000), load_default="", required=False
    )
    str_max_2000 = fields.String(
        validate=validate.Length(min=0, max=2000), required=True
    )
    str_max_2000_ = fields.String(
        validate=validate.Length(min=0, max=2000), load_default="", required=False
    )

    int_max_10 = fields.Int(required=True, validate=validate.Range(min=1, max=10))
    int_max_1000 = fields.Int(required=True, validate=validate.Range(min=1, max=1000))
    int_max0_1000 = fields.Int(required=True, validate=validate.Range(min=0, max=1000))
    int_max_1000_ = fields.Int(
        required=False, validate=validate.Range(min=0, max=1000), load_default=0
    )

    username = fields.String(validate=validate.Length(min=2, max=20), required=True)
    password = fields.String(validate=validate.Length(min=6, max=16), required=True)

    true_name = fields.String(required=True, validate=validate.Length(min=2, max=7))

    phone = fields.String(required=True, validate=validate.Length(min=11, max=11))

    price = fields.Int(
        required=True, validate=validate.Range(min=1), metadata={"strict": True}
    )

    boolean = fields.Bool(required=True, metadata={"strict": True})

    dict_ = fields.Dict(required=False, load_default={})

    dict = fields.Dict(required=True)

    list_str = fields.List(fields.String, required=True)

    @staticmethod
    def validate_timestamp(value):
        try:
            datetime.datetime.utcfromtimestamp(int(value))
        except Exception:
            raise ValidationError("Timestamp is accurate to seconds")
