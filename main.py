from __future__ import annotations
import random
import os
import subprocess
from generate_data import generate_random, GenerationMethod, GENERATION_FUNCTIONS
from sorts import SORTING_ALGORITHMS
from benchmark import benchmark_multiple, BenchmarkResults, AMOUNT_OF_TRIALS
from visualization import visualize_algorithm_test, visualize_scaled_test
from saving import save_comparison_benchmark, save_scaling_benchmark, prompt_load

DEFAULT_GENERATION_LENGTH: int = 50

class NegativeNumberError(Exception):
    pass

def clear_terminal() -> None:
    """Clears the terminal."""
    subprocess.run(["cls" if os.name == "nt" else "clear"])

def choose_generation_method() -> tuple[str, list[any] | None]:
    """Prompts the user to choose a generation method for a data set.

    Returns:
        tuple[str, list[any] | None]: A tuple containing:
            - data_generation_name (str): The name of the chosen data generation method.
            - additional_arguments (list[any] | None, optional): Additional arguments needed to generate the data set.
    """
    while True:
        clear_terminal()
        display_generation_methods()
        choice: str = input("Generate: ")
        
        match choice:
            case "0":  # Return
                break
            case "1":  # Generate random.
                min_value, max_value = prompt_for_range()
                random_instance = prompt_for_random_instance()
                return "Random", (random_instance, min_value, max_value)
            case "2":  # Generate sorted.
                return "Sorted", None
            case "3":  # Generate reverse sorted.
                return "Reverse Sorted", None
            case "4":  # Generate nearly sorted.
                swaps: int = prompt_for_positive_number("Amount of random swaps: ")
                random_instance = prompt_for_random_instance()
                return "Nearly Sorted", (random_instance, swaps)
            case _:
                print(f"{choice} is an invalid command.")

def generate_data_set(length: int, generation_algorithm: GenerationMethod, additional_arguments: list[any] | None = None) -> list[int]:
    """Generate a data set to be sorted.

    Args:
        length (int): The length of the generated data set.
        generation_algorithm (GenerationMethod): The algorithm used to generate the data set.
        additional_arguments (list[any] | None, optional): Any additional arguments needed to run the algorithm. Defaults to None.

    Returns:
        list[int]: The generated data set.
    """
    if additional_arguments is None:
        return generation_algorithm(length)
    else:
        return generation_algorithm(length, *additional_arguments)

def display_generation_methods() -> None:
    """Display different generation command settings."""
    print("Select a way to generate data:")
    print("(1) Random")
    print("(2) Sorted")
    print("(3) Reverse Sorted")
    print("(4) Nearly Sorted")
    print("(0) Return")

def display_commands() -> None:
    """Display program commands."""
    print("Commands:")
    print("(1) Test the same algorithm with different data set lengths.")
    print("(2) Test different algorithms with the same data set.")
    print("(3) Load json result file.")
    print("(0) Exit")

def prompt_for_positive_number(prompt: str) -> int:
    """Prompt the user for a positive integer.

    Args:
        prompt (str): The text prompt displayed to the user.

    Raises:
        NegativeNumberError: If selected number is negative.

    Returns:
        int: The positive number.
    """
    clear_terminal()
    while True:
        try:
            number: int = int(input(prompt))
            if number < 0:
                raise NegativeNumberError()
            
        except ValueError:
            print("Please input a number.")
        except NegativeNumberError:
            print("Please input a positive number.")
        else:
            break

    return number

def prompt_for_random_instance() -> random.Random:
    """Prompt the user for a seed to create a valid random instance.

    This function prompts the user to create a random.Random instance.
    The user is prompted for a seed in the form of an integer for 
    simplicity. Note that if the user uses a blank seed, they will
    get a random seed.

    Returns:
        random.Random: The random instance used for random generation.
    """
    clear_terminal()
    while True:
        try:
            seed = input("Seed (leave blank for random): ")
            if seed == "":
                random_instance: random.Random = random.Random()
            else:
                random_instance: random.Random = random.Random(int(seed))
            
        except ValueError:
            print("Please input a number.")
        else:
            break

    return random_instance

def prompt_for_range() -> tuple[int, int]:
    """Prompt the user for a minimum and maximum value.

    Returns:
        tuple[int, int]: A tuple containing:
            minimum (int): The selected minimum value.
            maximum (int): The selected maximum value.
    """
    clear_terminal()

    # Prompt user for a valid minimum value.
    while True:
        try:
            min_value = int(input("Minimum value: "))
        except ValueError:
            print("Please input a number.")
        else:
            break

    # Prompt user for a valid maximum value.
    while True:
        try:
            max_value = int(input("Maximum value: "))
        except ValueError:
            print("Please input a number.")
        else:
            if max_value < min_value:
                print("Maximum must be bigger than minimum.")
            else:
                break

    return min_value, max_value

def scaled_test() -> None:
    """Test different algorithms with scaling (increasing) data set lengths."""
    # Let the user determine the characteristics of the data sets.
    amount_of_sets = prompt_for_positive_number("Amount of data sets: ")
    start_length = prompt_for_positive_number("Start length: ")
    delta_length = prompt_for_positive_number("Net length increase for each data set: ")

    # Let the user choose the data generation algorithm.
    generation_name, additional_arguments = choose_generation_method()

    # Generate the data sets.
    data_sets: list[int] = []
    lengths: list[int] = []
    for i in range(amount_of_sets):
        length = start_length + delta_length * i
        data_set = generate_data_set(length, GENERATION_FUNCTIONS[generation_name], additional_arguments)
        lengths.append(length)
        data_sets.append(data_set)

    # Benchmark each algorithm with each data set and gather results.
    results: dict[str, list[BenchmarkResults]] = {}
    for name, algorithm in SORTING_ALGORITHMS.items():
        results[name] = []
        for data_set in data_sets:
            results[name].append(benchmark_multiple(algorithm, data_set, AMOUNT_OF_TRIALS))

    save_scaling_benchmark(lengths, results, generation_name)
    visualize_scaled_test(lengths, results, generation_name)
    
def algorithm_test() -> None:
    """Test different algorithms with the same data set."""
    length = prompt_for_positive_number("Length: ")
    generation_name, additional_arguments = choose_generation_method()

    data_set = generate_data_set(length, GENERATION_FUNCTIONS[generation_name], additional_arguments)

    results: dict[str, BenchmarkResults] = {}

    for name, sort in SORTING_ALGORITHMS.items():
        result = benchmark_multiple(sort, data_set, AMOUNT_OF_TRIALS)
        results[name] = result

    save_comparison_benchmark(results, length, generation_name)
    visualize_algorithm_test(results, generation_name)

def display_sorting_options() -> None:
    """Display sorting algorithm options."""
    print("Algorithms:")
    print("(1) Bubble sort")
    print("(2) Selection sort")
    print("(3) Insertion sort")
    print("(4) Merge sort")
    print("(5) Quicksort")
    print("(0) Return")

def main() -> None:
    global items_to_sort

    # Pregenerate a list of random values.
    items_to_sort = generate_random(DEFAULT_GENERATION_LENGTH, random.Random())

    while True:
        clear_terminal()
        display_commands()

        choice: str = input("Command: ")
        
        match choice:
            case "0":
                break
            case "1":
                scaled_test()
            case "2":
                algorithm_test()
            case "3":
                prompt_load()
            case _:
                print(f"{choice} is an invalid command.")

main()
