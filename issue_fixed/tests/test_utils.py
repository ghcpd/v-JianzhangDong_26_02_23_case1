from app.utils import parse_iso_date

def test_parse_date():
    d = parse_iso_date("2024-01-01T00:00:00")
    assert d.year == 2024