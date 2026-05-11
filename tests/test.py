from src.loader import load_data

from src.generators import (
    high_screen_time
)
def test_load_data():
    df = load_data(
        "data/daily_usage.csv"
    )
    assert len(df) > 0

def test_columns_exist():
    df = load_data(
        "data/daily_usage.csv"
    )
    required = [
        "telegram",
        "screen_time",
        "sleep"
    ]
    for col in required:
        assert col in df.columns

def test_generator():
    df = load_data(
        "data/daily_usage.csv"
    )
    result = list(
        high_screen_time(df)
    )
    assert isinstance(result, list)