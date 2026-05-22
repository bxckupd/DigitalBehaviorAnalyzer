import argparse
from src.loader import load_data
from src.analysis import (
    basic_stats,
    weekend_analysis,
    correlation_analysis,
    toxic_days
)
DATA_PATH = "data/daily_usage.csv"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        help="Команда"
    )
    args = parser.parse_args()
    df = load_data(DATA_PATH)
    if args.command == "stats":
        basic_stats(df)
    elif args.command == "weekend":
        weekend_analysis(df)
    elif args.command == "correlation":
        correlation_analysis(df)
    elif args.command == "toxic":
        toxic_days(df)
    elif args.command == "full":
        print(
            "ПОЛНЫЙ АНАЛИЗ ДАННЫХ\n"
        )
        basic_stats(df)
        weekend_analysis(df)
        correlation_analysis(df)
        toxic_days(df)
    else:
        print(
            "Доступные команды:\n"
            "stats\n"
            "weekend\n"
            "correlation\n"
            "toxic\n"
            "full"
        )

if __name__ == "__main__":
    main()
