import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random


def validate_data(screen_time, sleep):
    if screen_time > 1440:
        raise ValueError(
            "Экранное время больше 24 часов"
        )
    if sleep < 0 or sleep > 24:
        raise ValueError(
            "Неверное время сна"
        )


days = 180
start_date = datetime(2025, 11, 1)
data = []

for i in range(days):
    current_date = start_date + timedelta(days=i)
    weekend = current_date.weekday() >= 5
    telegram = random.randint(140, 340)
    youtube = random.randint(10, 90)
    tiktok = random.randint(0, 20)
    if weekend:
        music = random.randint(80, 180)
    else:
        music = random.randint(20, 90)

    if weekend:
        hud_speed = random.randint(120, 220)
    else:
        hud_speed = random.randint(20, 45)

    safari = random.randint(5, 45)
    screen_time = (
        telegram
        + youtube
        + tiktok
        + music
        + hud_speed
        + safari
    )
    sleep = round(
        np.random.normal(7, 1.1),
        1
    )
    sleep = max(4, min(10, sleep))
    try:
        validate_data(screen_time, sleep)
    except ValueError as error:
        print(error)
        continue

    productivity = round(
        10
        - (telegram / 70)
        - (tiktok / 20)
        - (screen_time / 500)
        + (sleep / 2)
        + np.random.normal(0, 1),
        1
    )
    productivity = max(
        1,
        min(10, productivity)
    )
    mood = round(
        6
        + (music / 90)
        - (telegram / 180)
        + np.random.normal(0, 1),
        1
    )
    mood = max(
        1,
        min(10, mood)
    )
    notifications = random.randint(50, 280)
    unlocks = int(
        notifications * np.random.uniform(0.5, 1.1)
    )
    data.append({
        "date": current_date.strftime("%Y-%m-%d"),
        "telegram": telegram,
        "youtube": youtube,
        "tiktok": tiktok,
        "music": music,
        "hud_speed": hud_speed,
        "safari": safari,
        "screen_time": screen_time,
        "sleep": sleep,
        "productivity": productivity,
        "mood": mood,
        "notifications": notifications,
        "unlocks": unlocks,
        "weekend": weekend
    })

df = pd.DataFrame(data)
os.makedirs("data", exist_ok=True)
df.to_csv(
    "data/daily_usage.csv",
    index=False
)

print("Датасет сгенерирован")