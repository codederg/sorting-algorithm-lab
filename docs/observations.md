# Scaling Experiment: Random Datasets

## Experimental Setup

- Distribution: Random
- Datasets: [0, 100, 200, 300, ...., 1900]
- Seed: 1

## Observations

![Scaling dataset lengths with random data](docs/scaling_random.png)

### Bubble Sort, Insertion Sort, and Selection Sort

As predicted, the graph highlights a quadratic growth model as the datasets grow longer, taking considerably more time as the data set gets very large. It should be noted that the algorithms seem to take less time to sort in the order of Bubble Sort > Insertion Sort > Selection Sort.

### Mergesort and Quicksort

The graph shows a much more linear, consistent line for both algorithms as the datasets grow in length. Additionally, these two algorithms are consistently much faster than the quadratic algorithms.

# Scaling Experiment: Sorted Datasets

## Experimental Setup

- Distribution: Sorted
- Datasets: [0, 50, 100, ...., 450]
- Seed: 1

## Observations

![Scaling dataset lengths with sorted data](docs/scaling_sorted.png)

### Bubble Sort and Selection Sort

As predicted, the graph highlights a quadratic growth model as the datasets grow longer, with bubble sort taking more time than selection sort.

### Mergesort and Quicksort

Both of these algorithms show a linear, consistent line as the datasets grow longer.

### Insertion Sort

Unlike random data distribution, this sorting algorithm sorts an already sorted list much faster than the other algorithms. This is likely due to how insertion sort stops its comparisons as soon as it finds that its element is in the right place.

# Comparison Experiment: Reverse-sorted

## Experimental Setup

- Distribution: Reverse-sorted
- Dataset Length: 1000

## Observations

![Different algorithm times with reverse sorted data](docs/comparison_reverse.png)

### Bubble Sort and Insertion Sort

Both algorithms take considerably longer than the others, as expected with a considerably large dataset length.

### Selection Sort

Unlike bubble sort and insertion sort, selection sort takes considerably less time to sort. This is likely a result of how, with reverse sorted data, selection sort only has to swap once per pass, considerably decreasing the amount of writes.

# Mergesort and Quicksort

Both of these algorithms are incredibly fast when compared to the quadratic algorithms. This is expected, as the divide-and-conquer methods these algorithms use considerably less time to actually sort the data.

