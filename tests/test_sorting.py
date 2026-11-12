from collections.abc import Callable
from sorts import bubble_sort, insertion_sort, selection_sort
import pytest

SORTING_ALGORITHMS = [bubble_sort, insertion_sort, selection_sort]

@pytest.mark.parametrize("sort_function", SORTING_ALGORITHMS)
@pytest.mark.parametrize("unsorted, expected", [
    ([], []),  # Empty list
    ([1], [1]),  # One element
    ([1, 2, 3, 4], [1, 2, 3, 4]),  # Already sorted
    ([4, 3, 2, 1], [1, 2, 3, 4]),  # Reverse sorted
    ([2, 1, 2, 3, 4, 3], [1, 2, 2, 3, 3, 4]),  # Duplicate values
    ([1, 0, 3, 2], [0, 1, 2, 3]),  # Presence of 0
    ([0, 1, -1, 2, -2], [-2, -1, 0, 1, 2]),  # Negative values
])
def test_sorts(sort_function: Callable[[list[int]], int], unsorted: list[int], expected: list[int]) -> None:
    result = sort_function(unsorted)

    assert result == expected