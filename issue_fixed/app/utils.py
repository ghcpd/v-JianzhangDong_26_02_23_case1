from datetime import datetime

from dateutil.parser import parse


def parse_iso_date(date_str: str) -> datetime:
    """
    Parse an ISO8601 date string into a datetime object.
    Uses python-dateutil for robust parsing.
    """

    return parse(date_str)
