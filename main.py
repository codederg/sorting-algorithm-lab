from __future__ import annotations
import random
from typing import Any, Protocol
import os
import subprocess
from generate_data import generate_random, generate_nearly_sorted, generate_sorted, generate_reverse_sorted
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

items_to_sort: list[int] = None
length_of_data: int = 10
data_generation_method_name : str = "Sorted"

additional_generation_arguments: list[any] = None
selected_generation: GenerationMethod = generate_sorted

class GenerationMethod(Protocol):
    def __call__(self, size: int, *args: Any, **kwargs: Any) -> list[int]:
        pass

class NegativeNumberError(Exception):
    pass

def clear_terminal() -> None:
    subprocess.run(["cls" if os.name == "nt" else "clear"])

def data_generation_settings() -> None:
    global length_of_data

    while True:
        clear_terminal()
        prompt_generation_settings()

        choice: str = input("Data Generation: ")
        match choice:
            case "0":  # Return.
                break            
            case "1":  # Choose method for generation.
                choose_generation_method()
            case "2":  # Prompt length of data.
                length_of_data = prompt_for_positive_number("Length of new data: ")
            case "3":  # Generate a new data set.
                generate_and_update_list()
            case _:
                print(f"{choice} is an invalid command.")

def prompt_generation_settings() -> None:
    print("| Data generation |")
    print(f"Current list: {items_to_sort}")
    print(f"(1) Choose method ({data_generation_method_name})")
    print(f"(2) Length of data (n = {length_of_data})")
    print(f"(3) Generate new data set")
    print("(0) Return")

def choose_generation_method() -> None:
    global data_generation_method_name, additional_generation_arguments, selected_generation

    while True:
        clear_terminal()
        prompt_generation_methods()
        choice: str = input("Generate: ")
        
        match choice:
            case "0":  # Return
                break
            case "1":  # Generate random.
                min_value, max_value = prompt_for_range()
                random_instance = prompt_for_random_instance()
                data_generation_method_name = "Random"
                selected_generation = generate_random
                additional_generation_arguments = [random_instance, min_value, max_value]
                break
            case "2":  # Generate sorted.
                data_generation_method_name = "Sorted"
                selected_generation = generate_sorted
                additional_generation_arguments = None
                break
            case "3":  # Generate reverse sorted.
                data_generation_method_name = "Reverse Sorted"
                selected_generation = generate_reverse_sorted
                additional_generation_arguments = None
                break
            case "4":  # Generate nearly sorted.
                swaps: int = prompt_for_positive_number("Amount of random swaps: ")
                random_instance = prompt_for_random_instance()
                data_generation_method_name = "Nearly Sorted"
                additional_generation_arguments = [random_instance, swaps]
                selected_generation = generate_nearly_sorted
                break
            case _:
                print(f"{choice} is an invalid command.")

def prompt_generation_methods() -> None:
    print("Select a way to generate data:")
    print("(1) Random")
    print("(2) Sorted")
    print("(3) Reverse Sorted")
    print("(4) Nearly Sorted")
    print("(0) Return")

def generate_and_update_list() -> None:
    global items_to_sort

    if additional_generation_arguments is None:
        items_to_sort = selected_generation(length_of_data)
    else:
        items_to_sort = selected_generation(length_of_data, *additional_generation_arguments)

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

def display_commands() -> None:
    print("Commands:")
    print("(1) Generate random data.")
    print("(2) ")
    print("(0) Exit")

def main() -> None:
    global items_to_sort

    # Pregenerate a list of random values.
    items_to_sort = generate_random(length_of_data, random.Random())

    while True:
        clear_terminal()
        display_commands()

        choice: str = input("Command: ")
        
        match choice:
            case "0":
                break
            case "1":
                data_generation_settings()
            case "2":
                pass  # TODO: Implement user-chosen sorting algorithm.
            case _:
                print(f"{choice} is an invalid command.")
        

main()
