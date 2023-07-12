import datetime
import time

from config import current_config


def utc2local(utc):
    """To convert UTC datetime for local time"""
    epoch = time.mktime(utc.timetuple())
    offset = datetime.datetime.fromtimestamp(
        epoch
    ) - datetime.datetime.utcfromtimestamp(epoch)
    return utc + offset


def local2utc(local_st):
    """The local time to convert UTC time"""
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st


def date_str_to_utc_datetime(date_str, format_str=current_config.DATE_FORMAT):
    """Convert a string to utc time"""
    try:
        tmp_date = datetime.datetime.strptime(date_str, format_str)
        tmp_date = datetime.datetime.utcfromtimestamp(tmp_date.timestamp())
    except Exception:  # ignore
        return None
    else:
        return tmp_date


def timestamp_to_datetime(time_stamp):
    """Turn a datetime timestamp"""
    time_stamp = int(time_stamp)
    date_object = datetime.datetime.fromtimestamp(time_stamp)
    return date_object


def date_timestamp_to_utc(timestamp):
    try:
        tmp_data = datetime.datetime.utcfromtimestamp(timestamp)
    except:
        return None
    else:
        return tmp_data


def date_utc_to_timestamp(utc):
    time_datetime = utc2local(utc)
    timestamp = int(time.mktime(time_datetime.timetuple()))
    return timestamp
