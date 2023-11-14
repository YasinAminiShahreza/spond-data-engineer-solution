from datetime import datetime
import math


def convert_milliseconds_to_date(timestamp):
    if not math.isnan(timestamp):
        return datetime.utcfromtimestamp(timestamp / 1000.0)
    else:
        return None


def convert_date_to_milliseconds(dt):
    if dt is not None:
        return int((dt - datetime(1970, 1, 1)).total_seconds() * 1000)
    else:
        return None
