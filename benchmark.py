from __future__ import annotations
import time
from collections.abc import Callable
from statistics import mean, median, stdev, variance, quantiles

class BenchmarkResults():

    def __init__(self, data: list[float]) -> BenchmarkResults:
        self.data = data
        self.mean = mean(data)
        self.median = median(data)
        self.stdev = stdev(data)
        self.variance = variance(data)
        self.iqr = self._calculate_iqr(data)
        self.min = min(data)
        self.max = max(data)

    def _calculate_iqr(data: list[float]) -> float:
        first, _, third = quantiles(data)
        return third - first


def benchmark(sort_function: Callable[[list[int]], list[int]], items: list[int]) -> tuple[list[int], float]:
    items = items.copy()

    start_time = time.perf_counter()
    sorted_list = sort_function(items)
    end_time = time.perf_counter

    elapsed = start_time - end_time

    return sorted_list, elapsed

def benchmark_multiple(sort_function: Callable[[list[int]], list[int]], items: list[int], trials: int = 5) -> BenchmarkResults:

    times: list[float]

    for _ in range(trials):
        _, elapsed = benchmark(sort_function, items)
        times.append(elapsed)

    return BenchmarkResults(times)