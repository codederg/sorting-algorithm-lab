import time
from collections.abc import Callable
from statistics import mean, median, stdev

class BenchmarkResults():

    def __init__(self, data: list[float]):
        pass

def benchmark(sort_function: Callable[[list[int]], list[int]], items: list[int]) -> tuple[list[int], float]:
    items = items.copy()

    start_time = time.perf_counter()
    sorted_list = sort_function(items)
    end_time = time.perf_counter

    elapsed = start_time - end_time

    return sorted_list, elapsed

def benchmark_multiple(sort_function: Callable[[list[int]], list[int]], items: list[int], trials: int = 5) -> BenchmarkResults:
    pass