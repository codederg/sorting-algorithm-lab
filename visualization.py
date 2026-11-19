from collections.abc import Callable
import matplotlib
matplotlib.use("QtAgg")  # Must be called before importing pyplot.
import matplotlib.pyplot as plt
from benchmark import BenchmarkResults

def visualize_scaled_test(lengths: list[int], data: dict[str, list[BenchmarkResults]]) -> None:

    for algorithm_name, results in data.items():
        y = [i.median for i in results]
        plt.plot(lengths, y, label = algorithm_name)

    plt.title(f"Scaling data set lengths")
    plt.xlabel("Length of data set")
    plt.ylabel("Median Time Taken (ms)")

    plt.legend()
    plt.show()

def visualize_algorithm_test(results: dict[str, BenchmarkResults]) -> None:
    """Display time taken for different sorting algorithms.

    Displays a bar chart to indicate the differences in ms of each sorting algorithm.
    Presents each sorting algorithm across the x-axis and the median time taken (ms) 
    across the y-axis. Displays the median, as it is less affected by outliers.

    Args:
        results (dict[str, BenchmarkResults]): The name of the sorting algorithm and its results.
    """
    categories = results.keys()
    values = [i.median for i in results.values()]

    fig, ax = plt.subplots()
    bars = ax.bar(categories, values, color = "steelblue", width = 0.5)

    ax.set_title("Algorithm Lab")
    ax.set_xlabel("Sorting Algorithm")
    ax.set_ylabel("Median Time Taken (ms)")

    ax.bar_label(bars, padding = 3)

    plt.show()
