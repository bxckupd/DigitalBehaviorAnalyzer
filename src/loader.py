import os
import pandas as pd


def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Файл {path} не найден"
        )
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError(
            "Файл пустой"
        )
    required_columns = [
        "telegram",
        "youtube",
        "screen_time",
        "sleep"
    ]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(
                f"Нет колонки: {col}"
            )
    print("Данные успешно загружены")
    return df