from collections.abc import Callable
import matplotlib
matplotlib.use("QtAgg")  # Must be called before importing pyplot.
import matplotlib.pyplot as plt
from benchmark import BenchmarkResults

def visualize_scaled_test() -> None:
    pass

def visualize_algorithm_test(results: dict[str, BenchmarkResults]) -> None:

    categories = results.keys()
    values = [i.median for i in results.values()]

    fig, ax = plt.subplots()
    bars = ax.bar(categories, values, color = "steelblue", width = 0.5)

    ax.set_title("Algorithm Lab")
    ax.set_xlabel("Sorting Algorithm")
    ax.set_ylabel("Median Time Taken (ms)")

    ax.bar_label(bars, padding = 3)

    plt.show()
