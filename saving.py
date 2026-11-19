import csv
from pathlib import Path
from datetime import datetime

COMPARISON_DIRECTORY = Path(__file__).resolve().parent / "results" / "comparison"

def save_comparison_benchmark(data_generation_name: str, length: int, additional_arguments: list[any] | None):

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.replace(" ", "_")}_{timestamp}.csv"

    data = []
    if additional_arguments is None:
        data = [
            data_generation_name,
            length,
        ]
    else:
        data = [
            data_generation_name,
            length,
            [*additional_arguments],
        ]

    with (COMPARISON_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        file.write("comparison\n")

        writer = csv.writer(file)
        writer.writerow(data)