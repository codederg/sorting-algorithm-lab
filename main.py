import random
from collections.abc import Callable
from generate_data import generate_random, generate_nearly_sorted, generate_sorted, generate_reverse_sorted
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

items_to_sort: list[int] = None

class NegativeNumberError(Exception):
    pass

def data_generation_settings() -> None:
    print(f"Current list:\n {items_to_sort}\n")

    length_of_data = prompt_for_positive_number("Length of new data: ")

    choose_generation_method(length_of_data)

    print(f"New list:\n {items_to_sort}\n")

def choose_generation_method(length_of_data: int) -> None:
    global items_to_sort

    print("Select a way to generate data:")
    print("(1) Random")
    print("(2) Sorted")
    print("(3) Reverse Sorted")
    print("(4) Nearly Sorted")

    while True:
        choice: str = input("Generate: ")

        match choice:
            case "0":
                break
            case "1":
                min_value, max_value = prompt_for_range()
                random_instance = prompt_for_random_instance()
                items_to_sort = generate_random(length_of_data, random_instance, min_value, max_value)
                break
            case "2":
                items_to_sort = generate_sorted(length_of_data)
                break
            case "3":
                items_to_sort = generate_reverse_sorted(length_of_data)
                break
            case "4":
                swaps: int = prompt_for_positive_number("Amount of random swaps: ")
                random_instance = prompt_for_random_instance()
                items_to_sort = generate_nearly_sorted(length_of_data, random_instance, swaps)
                break

def prompt_for_positive_number(prompt: str) -> int:
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
    items_to_sort = generate_random(10, random.Random(), max_value = 100)

    display_commands()

    while True:
        choice: str = input("Command: ")
        
        match choice:
            case "0":
                break
            case "1":
                data_generation_settings()
            case "2":
                pass  # TODO: Implement user-chosen sorting algorithm.
            case "?":
                display_commands()
            case _:
                print(f"{choice} is an invalid command.")
        

main()
