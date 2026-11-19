import csv
import questionary
from random import Random
from pathlib import Path
from datetime import datetime
from visualization import visualize_algorithm_test
from benchmark import benchmark_multiple, AMOUNT_OF_TRIALS, BenchmarkResults
from sorts import SORTING_ALGORITHMS
from generate_data import GENERATION_FUNCTIONS

COMPARISON_DIRECTORY = Path(__file__).resolve().parent / "results" / "comparison"

def prompt_load() -> None:
    raw_path = questionary.path("Select a file to load: ").ask()

    if not raw_path:
        return
    file_path = Path(raw_path).resolve()

    with file_path.open("r", newline = "", encoding = "utf-8") as file:
        reader = csv.reader(file)
        header = "".join(next(reader))

        if header == "comparison":
            data = next(reader, None)
            if data:
                print(data)
                try:
                    items = GENERATION_FUNCTIONS[data[0]](int(data[1]), data[2])
                except:
                    items = GENERATION_FUNCTIONS[data[0]](int(data[1]))

                results: dict[str, BenchmarkResults] = {}
            
                for sort_name, sort in SORTING_ALGORITHMS.items():
                    result = benchmark_multiple(sort, items, AMOUNT_OF_TRIALS)
                    results[sort_name] = result
                
                visualize_algorithm_test(results)


def save_comparison_benchmark(data_generation_name: str, length: int, additional_arguments: list[any] | None):

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.csv"

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