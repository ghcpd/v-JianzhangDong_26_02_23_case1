from app.services import generate_summary

def test_generate_summary():
    result = generate_summary()
    assert result["mean"] > 0
    assert result["max"] <= 100
