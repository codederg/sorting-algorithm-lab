import random

def generate_random(size: int, rng: random.Random, min_value: int = 0, max_value: int = 1000) -> list[int]:
    if size < 0:
        raise ValueError("Size cannot be negative")
    if min_value < max_value:
        raise ValueError("Minimum value must be less than max value")

    return [rng.randint(min_value, max_value) for _ in range(size)]

def generate_sorted(size: int) -> list[int]:
    return [i for i in range(size)]

def generate_reverse_sorted(size: int) -> list[int]:
    return [i for i in range(size - 1, -1, -1)]

def generate_nearly_sorted(size: int, rng: random.Random, min_value: int = 0, max_value: int = 1000, swaps: int = 3) -> list[int]:
    data: list[int] = generate_sorted(size, rng, min_value, max_value)

    for _ in range(swaps):
        i = random.randrange(size)
        j = random.randrange(size)
        data[i], data[j] = data[j], data[i]

    return data

