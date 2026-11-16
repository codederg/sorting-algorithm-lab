from __future__ import annotations
import time
from collections.abc import Callable
from statistics import mean, median, stdev, variance, quantiles

class BenchmarkResults():
    """Represents the results of a trialed benchmark.

    Attributes:
        data (list[float]): The elapsed times making up the dataset.
        mean (float): The average of the dataset.
        median (float): The middle value of the dataset.
        stdev (float): The sample standard deviation of the dataset.
        variance (float): The sample variation of the dataset.
        iqr (float): The iqr of the dataset.
        min (float): The minimum value of the dataset.
        max (float): The maximum value of the dataset.
    """
    def __init__(self, data: list[float]) -> BenchmarkResults:
        """Initialize the results of the benchmark.

        Args:
            data (list[float]): The elapsed times making up the dataset.
        """
        self.data = data
        self.mean = mean(data)
        self.median = median(data)
        self.stdev = stdev(data)
        self.variance = variance(data)
        self.iqr = self._calculate_iqr(data)
        self.min = min(data)
        self.max = max(data)

    def _calculate_iqr(data: list[float]) -> float:
        """Calculate the iqr of the dataset.

        Args:
            data (list[float]): The dataset.

        Returns:
            float: The iqr of the dataset.
        """

        first, _, third = quantiles(data)
        return third - first


def benchmark(sort_function: Callable[[list[int]], list[int]], items: list[int]) -> tuple[list[int], float]:
    """Benchmark a sorting algorithm function.

    Args:
        sort_function (Callable[[list[int]], list[int]]): The sorting algorithm.
        items (list[int]): The list being sorted.

    Returns:
        tuple[list[int], float]: A tuple containing:
            - The sorted list.
            - The elapsed benchmark time.
    """

    # Create a shallow copy to preserve the original dataset.
    items = items.copy()

    # Benchmark the sorting list.
    start_time = time.perf_counter()
    sorted_list = sort_function(items)
    end_time = time.perf_counter

    elapsed = start_time - end_time

    return sorted_list, elapsed

def benchmark_multiple(sort_function: Callable[[list[int]], list[int]], items: list[int], trials: int = 5) -> BenchmarkResults:
    """Benchmark a sorting algorithm for multiple trials.

    Args:
        sort_function (Callable[[list[int]], list[int]]): The sorting algorithm.
        items (list[int]): The list being sorted.
        trials (int, optional): The amount of trials in the benchmark. Defaults to 5.

    Returns:
        BenchmarkResults: The results gathered from the benchmark.
    """

    times: list[float]

    for _ in range(trials):
        _, elapsed = benchmark(sort_function, items)
        times.append(elapsed)

    return BenchmarkResults(times)