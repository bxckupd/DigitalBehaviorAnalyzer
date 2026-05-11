import matplotlib.pyplot as plt

def screen_time_plot(df):
    if "screen_time" not in df.columns:
        raise ValueError(
            "Колонка screen_time не найдена"
        )
    plt.figure(figsize=(10, 5))
    plt.plot(df["screen_time"])
    plt.title(
        "Экранное время"
    )
    plt.xlabel("День")
    plt.ylabel("Минуты")
    plt.grid()
    plt.show()