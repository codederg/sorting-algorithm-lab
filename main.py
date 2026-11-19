from __future__ import annotations
import random
from typing import Any, Protocol
from collections.abc import Callable
import os
import subprocess
from generate_data import generate_random, generate_nearly_sorted, generate_sorted, generate_reverse_sorted
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort
from benchmark import benchmark_multiple, BenchmarkResults
from visualization import visualize_algorithm_test

DEFAULT_GENERATION_LENGTH: int = 50
AMOUNT_OF_TRIALS = 50
SORTING_ALGORITHMS: dict[str, Callable[[list[int]], list[int]]] = {  # {name: sort_function}
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
}

class GenerationMethod(Protocol):
    def __call__(self, size: int, *args: Any, **kwargs: Any) -> list[int]:
        pass

class NegativeNumberError(Exception):
    pass

def clear_terminal() -> None:
    subprocess.run(["cls" if os.name == "nt" else "clear"])

def choose_generation_method() -> tuple[GenerationMethod, list[any] | None]:

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
                return generate_random, (random_instance, min_value, max_value)
            case "2":  # Generate sorted.
                return generate_sorted, None
            case "3":  # Generate reverse sorted.
                return generate_reverse_sorted, None
            case "4":  # Generate nearly sorted.
                swaps: int = prompt_for_positive_number("Amount of random swaps: ")
                random_instance = prompt_for_random_instance()
                return generate_nearly_sorted, (random_instance, swaps)
            case _:
                print(f"{choice} is an invalid command.")

def generate_data_set(length: int, generation_algorithm: GenerationMethod, additional_arguments: list[any] | None = None) -> list[int]:

    if additional_arguments is None:
        return generation_algorithm(length)
    else:
        return generation_algorithm(length, *additional_arguments)

def display_generation_methods() -> None:
    print("Select a way to generate data:")
    print("(1) Random")
    print("(2) Sorted")
    print("(3) Reverse Sorted")
    print("(4) Nearly Sorted")
    print("(0) Return")

def display_commands() -> None:
    print("Commands:")
    print("(1) Test the same algorithm with different data set lengths.")
    print("(2) Test different algorithms with the same data set.")
    print("(0) Exit")

def prompt_for_positive_number(prompt: str) -> int:
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

    selected_algorithm: Callable[[list[int]], list[int]] = None
    while True:
        clear_terminal()
        display_sorting_options()

        choice: str = input("Command: ")

        match choice:
            case "0":
                break
            case "1":
                selected_algorithm = bubble_sort
            case "2":
                selected_algorithm = selection_sort
            case "3":
                selected_algorithm = insertion_sort
            case "4":
                selected_algorithm = merge_sort
            case "5":
                selected_algorithm = quick_sort
            case _:
                print(f"{choice} is an invalid command.")
        break

    # Exit the test if they choose.
    if selected_algorithm is None:
        return

    amount_of_sets = prompt_for_positive_number("Amount of data sets: ")
    start_length = prompt_for_positive_number("Start length: ")
    delta_length = prompt_for_positive_number("Net length increase for each data set: ")

    # Let the user choose the data generation algorithm.
    generation_method, additional_arguments = choose_generation_method()

    # Create the data sets in the form of {length: data_set}.
    data_sets: dict[int, list[int]] = {}
    for i in range(amount_of_sets):
        length = start_length + delta_length * i
        data_set = generate_data_set(length, generation_method, additional_arguments)
        data_sets[length] = data_set        

    # Sort each data set and gather benchmark results.
    results: dict[int, BenchmarkResults] = {}
    for length, data_set in data_sets.items():
        results[length] = benchmark_multiple(selected_algorithm, data_set, AMOUNT_OF_TRIALS)
    
def algorithm_test() -> None:

    length = prompt_for_positive_number("Length: ")
    generation_method, additional_arguments = choose_generation_method()

    data_set = generate_data_set(length, generation_method, additional_arguments)

    results: dict[str, BenchmarkResults] = {}

    for name, sort in SORTING_ALGORITHMS.items():
        result = benchmark_multiple(sort, data_set, AMOUNT_OF_TRIALS)
        results[name] = result

    visualize_algorithm_test(results)

def display_sorting_options() -> None:
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
            case _:
                print(f"{choice} is an invalid command.")

main()
