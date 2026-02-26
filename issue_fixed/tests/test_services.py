from app.services import generate_summary


def test_generate_summary():
    result = generate_summary(seed=42)
    assert result.mean > 0
    assert result.max <= 100
    assert result.rows == 100
