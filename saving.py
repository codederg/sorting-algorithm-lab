import json
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
        data = json.load(file)

        test_type: str = data["test_type"]

        if test_type == "Comparison":

            results: dict[str, BenchmarkResults] = {}
            for name in SORTING_ALGORITHMS.keys():
                times = data[name]
                results[name] = BenchmarkResults(times)
            visualize_algorithm_test(results)

def save_scaling_benchmark(lengths: list[int], results: dict[str, list[BenchmarkResults]], data_generation_name: str) -> None:

    print(lengths)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.json"

    # Create data to be saved.
    data = {}
    for name, result in results.items():

        data[name] = {}
        
        for i, length in enumerate(lengths):
            data[name][length] = result[i].data

    data["test_type"] = "Scaling"
    data["data_generation"] = data_generation_name

    with (SCALED_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        json.dump(data, file, indent = 2)

def save_comparison_benchmark(results: dict[str, BenchmarkResults], length: int, data_generation_name: str):

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.json"

    # Create data to be saved
    data = {}
    for name, result in results.items():
        data[name] = result.data

    data["test_type"] = "Comparison"
    data["data_generation"] = data_generation_name
    data["length"] = length

    with (COMPARISON_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        json.dump(data, file, indent = 2)