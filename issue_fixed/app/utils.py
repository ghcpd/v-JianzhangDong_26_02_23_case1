from dateutil.parser import parse

def parse_iso_date(date_str: str):
    return parse(date_str)
