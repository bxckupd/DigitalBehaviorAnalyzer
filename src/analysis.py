import numpy as np
from src.decorators import (
    logger,
    timer
)

@logger
@timer
def basic_stats(df):
    print("СТАТИСТИКА")
    print(
        "Среднее экранное время:",
        round(np.mean(df["screen_time"]), 2)
    )
    print(
        "Средний сон:",
        round(np.mean(df["sleep"]), 2)
    )
    print(
        "Средняя продуктивность:",
        round(np.mean(df["productivity"]), 2)
    )

@logger
@timer
def weekend_analysis(df):
    print("ВЫХОДНЫЕ И БУДНИ")
    grouped = df.groupby(
        "weekend"
    )["screen_time"].mean()
    print(grouped)


@logger
@timer
def correlation_analysis(df):
    print("СВЯЗЬ ЭКРАННОГО ВРЕМЕНИ И ПРОДУКТИВНОСТИ")
    correlation = df[
        "screen_time"
    ].corr(
        df["productivity"]
    )
    print(
        "Корреляция:",
        round(correlation, 2)
    )


@logger
@timer
def toxic_days(df):
    print("ДНИ С БОЛЬШИМ ЭКРАННЫМ ВРЕМЕНЕМ")
    toxic = df[
        df["screen_time"] > 600
    ]
    print(
        toxic[
            [
                "date",
                "screen_time",
                "mood"
            ]
        ].head(10)
    )
