import json
import questionary
from pathlib import Path
from datetime import datetime
from visualization import visualize_algorithm_test, visualize_scaled_test
from benchmark import BenchmarkResults
from sorts import SORTING_ALGORITHMS

COMPARISON_DIRECTORY = Path(__file__).resolve().parent / "results" / "comparison"
SCALED_DIRECTORY = Path(__file__).resolve().parent / "results" / "scaled"

def prompt_load() -> None:
    """Load the sorting results of a json file."""

    # Get the associated file path desired to be loaded.
    raw_path = questionary.path("Select a file to load: ", default = "./results/").ask()
    if not raw_path:
        return
    file_path = Path(raw_path).resolve()

    # Attempt to load the file.
    try:
        with file_path.open("r", newline = "", encoding = "utf-8") as file:
            data = json.load(file)

            # Determine which type of test is being loaded.
            test_type: str = data["test_type"]
            if test_type == "Comparison":
                # Visualize a comparison test.
                results: dict[str, BenchmarkResults] = {}
                for name in SORTING_ALGORITHMS.keys():
                    times = data[name]
                    results[name] = BenchmarkResults(times)
                visualize_algorithm_test(results)
            elif test_type == "Scaling":
                # Visualize a scaling test.
                lengths = []
                results: dict[str, list[BenchmarkResults]] = {}
                for length, algorithm_data in data["lengths"].items():
                    lengths.append(int(length))
                    for algorithm, times in algorithm_data.items():
                        l = results[algorithm] = results.get(algorithm, [])
                        l.append(BenchmarkResults(times))
                visualize_scaled_test(lengths, results)
            else:
                input(f"{file_path} is an invalid file.")
    except IsADirectoryError:
        input(f"{file_path} is a directory. Please select a valid .json file.")
    except FileNotFoundError:
        input(f"{file_path} does not exist. Please select a valid .json file.")
    except Exception as e:
        input(f"An error was found: {e}")

def save_scaling_benchmark(lengths: list[int], results: dict[str, list[BenchmarkResults]], data_generation_name: str) -> None:
    """Save the results from a scaling test to json.

    Args:
        lengths (list[int]): The data set lengths tested with.
        results (dict[str, list[BenchmarkResults]]): Result data containing:
            - algorithm_name (str): The name of the sorting algorithm.
            - benchmarks (list[BenchmarkResults]): The results from the sorting algorithm, 
                sorted in the same order as the index from lengths.
        data_generation_name (str): The name of the method used to generate the original data.
    """

    # Create the name of the file.
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d")
    file_name = f"{data_generation_name.lower().replace(" ", "_")}_{timestamp}.json"

    # Create data to be saved.
    data = {}

    data["lengths"] = {}
    for i, length in enumerate(lengths):
        l = data["lengths"][length] = {}
        for name, result in results.items():
            l[name] = result[i].data

    data["test_type"] = "Scaling"
    data["data_generation"] = data_generation_name

    # Dump the data to a json file.
    with (SCALED_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        json.dump(data, file, indent = 2)

def save_comparison_benchmark(results: dict[str, BenchmarkResults], length: int, data_generation_name: str):
    """Save the results from a comparison test to json.

    Args:
        results (dict[str, BenchmarkResults]): Result data containing:
            - algorithm_name (str): The name of the sorting algorithm.
            - results (BenchmarkResults): The associated results of the sorting algorithm.
        length (int): The amount of items generated in the original data.
        data_generation_name (str): The name of the method used to generate the original data.
    """

    # Create the name of the file.
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

    # Dump the data to a json file.
    with (COMPARISON_DIRECTORY / file_name).open("w", newline = "", encoding = "utf-8") as file:
        json.dump(data, file, indent = 2)
