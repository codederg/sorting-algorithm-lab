from __future__ import annotations
import random
from typing import Any, Protocol

class GenerationMethod(Protocol):
    def __call__(self, size: int, *args: Any, **kwargs: Any) -> list[int]:
        pass

def generate_random(size: int, rng: random.Random, min_value: int = 0, max_value: int = 10000) -> list[int]:
    """Generates a list of randomized values.

    Args:
        size (int): The length of the generated list.
        rng (random.Random): The random number generator.
        min_value (int, optional): The minimum value for each item. Defaults to 0.
        max_value (int, optional): The maximum value for each item. Defaults to 1000.

    Raises:
        ValueError: If size is negative.
        ValueError: If the minimum value is greater than the max value.

    Returns:
        list[int]: The generated list of random values.
    """

    if size < 0:
        raise ValueError("Size cannot be negative")
    if min_value > max_value:
        raise ValueError("Minimum value must be less than max value")

    return [rng.randint(min_value, max_value) for _ in range(size)]

def generate_sorted(size: int) -> list[int]:
    """Generates a list of sorted values starting from 0 and incrementing by 1.

    Args:
        size (int): The length of the generated list.

    Raises:
        ValueError: If size is negative.

    Returns:
        list[int]: The generated list of values.
    """

    if size < 0:
        raise ValueError("Size cannot be negative")

    return [i for i in range(size)]

def generate_reverse_sorted(size: int) -> list[int]:
    """Generates a list of reverse sorted values starting from n and decrementing by 1 until reaching 0.

    Args:
        size (int): The length (n) of the generated list.

    Raises:
        ValueError: If size is negative.

    Returns:
        list[int]: The generated list of values.
    """

    if size < 0:
        raise ValueError("Size cannot be negative")

    return [i for i in range(size - 1, -1, -1)]

def generate_nearly_sorted(size: int, rng: random.Random, swaps: int = 3) -> list[int]:
    """Generates a list of nearly sorted values through random swapping.

    Args:
        size (int): The length of the generated list.
        rng (random.Random): The random number generator.
        swaps (int, optional): The amount of random swaps made to the sorted list. Defaults to 3.

    Raises:
        ValueError: If size is negative.
        ValueError: If swaps is negative.

    Returns:
        list[int]: The generated list of values.
    """

    if size < 0:
        raise ValueError("Size cannot be negative")
    if swaps < 0:
        raise ValueError("Swaps cannot be negative")

    data: list[int] = generate_sorted(size)

    # If no dataset is generated, return an empty one without swaps.
    if not data:
        return []

    for _ in range(swaps):
        i = rng.randrange(size)
        j = rng.randrange(size)
        data[i], data[j] = data[j], data[i]

    return data

GENERATION_FUNCTIONS: dict[str, GenerationMethod] = {
    "Random": generate_random,
    "Nearly Sorted": generate_nearly_sorted,
    "Sorted": generate_sorted,
    "Reverse Sorted": generate_reverse_sorted
}
