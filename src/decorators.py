import time


def logger(func):
    def wrapper(*args, **kwargs):
        print(
            f"\nЗапуск функции: "
            f"{func.__name__}"
        )
        return func(*args, **kwargs)
    return wrapper

def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(
            f"Время выполнения: "
            f"{round(end - start, 4)} сек"
        )
        return result
    return wrapper