import csv
import questionary
from pathlib import Path
from datetime import datetime
from visualization import visualize_algorithm_test
from benchmark import BenchmarkResults
from sorts import SORTING_ALGORITHMS

COMPARISON_DIRECTORY = Path(__file__).resolve().parent / "results" / "comparison"
SCALED_DIRECTORY = Path(__file__).resolve().parent / "results" / "scaled"

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

def save_scaling_benchmark(lengths: list[int], results: dict[str, list[BenchmarkResults]], data_generation_name: str) -> None:

    print(lengths)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.csv"

    data = []
    field_names = ["algorithm", "lengths", "times"]
    # Create list of data to be saved.
    for name, result in results.items():

        sub_data = {}
        sub_data["algorithm"] = name
        sub_data["times"] = {}
        
        for i, length in enumerate(lengths):
            benchmarks = result[i]
            times = benchmarks.data

            l = sub_data["times"][str(length)] = []
            l.append(times)

        data.append(sub_data)

    print(data)

    with (SCALED_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        file.write("scaled\n")

        writer = csv.DictWriter(file, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(data)

def save_comparison_benchmark(results: dict[str, BenchmarkResults], data_generation_name: str):

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.csv"

    data = [r.data for r in results.values()]

    with (COMPARISON_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        file.write("comparison\n")

        writer = csv.writer(file)
        writer.writerows(data)