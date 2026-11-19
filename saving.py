import csv
import questionary
from pathlib import Path
from datetime import datetime
from visualization import visualize_algorithm_test
from benchmark import BenchmarkResults
from sorts import SORTING_ALGORITHMS

COMPARISON_DIRECTORY = Path(__file__).resolve().parent / "results" / "comparison"

def prompt_load() -> None:
    raw_path = questionary.path("Select a file to load: ", default = "./results/").ask()

    if not raw_path:
        return
    file_path = Path(raw_path).resolve()

    with file_path.open("r", newline = "", encoding = "utf-8") as file:
        reader = csv.reader(file)

        # Get header to determine type of test done with the file.
        header = "".join(next(reader))
        if header == "comparison":

            results: dict[str, BenchmarkResults] = {}
            for name in SORTING_ALGORITHMS.keys():
                row = [float(f) for f in next(reader)]
                results[name] = BenchmarkResults(row)
            visualize_algorithm_test(results)

def save_comparison_benchmark(results: dict[str, BenchmarkResults], data_generation_name: str):

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.csv"

    data = [r.data for r in results.values()]

    with (COMPARISON_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        file.write("comparison\n")

        writer = csv.writer(file)
        writer.writerows(data)