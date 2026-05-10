def row_generator(df):
    for _, row in df.iterrows():
        yield row

def high_screen_time(df, limit=600):
    found = False
    for _, row in df.iterrows():
        if row["screen_time"] > limit:
            found = True
            yield row
    if not found:
        print(
            "Дней с большим экранным "
            "временем не найдено"
        )