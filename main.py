import random
from generate_data import generate_random, generate_nearly_sorted, generate_sorted, generate_reverse_sorted
from sorts import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort

def data_generation_settings():
    pass

def display_commands():
    print("Commands:")
    print("(1) ")
    print("(2) ")
    print("(0) Exit")

def main() -> None:

    display_commands()

    while True:
        choice: str = input("Command: #")
        
        match choice:
            case "0":
                break
            case "1":
                data_generation_settings
            case "2":
                pass  # TODO: Implement user-chosen sorting algorithm.
            case "?":
                display_commands()
            case _:
                print(f"{choice} is an invalid command.")
        

main()