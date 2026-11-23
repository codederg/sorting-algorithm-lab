# Sorting Algorithm Benchmark Lab

## 1. Overview

A Python application for implementing, benchmarking, and visually analyzing sorting algorithms.

This program investigates and highlights the differences in median sorting times (ms) between different sorting algorithms under certain conditions. The program provides tools for comparing sorting algorithms across different input sizes and dataset distributions.

This program also uses Matplotlib for sorting time visualization and supports saving/loading results to/from JSON.

## 2. Algorithms

| Algorithm | Average Time | Worst Time |
| :--- | ---: | ---: |
| Bubble Sort | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| Selection Sort | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| Insertion Sort | O(n<sup>2</sup>) | O(n<sup>2</sup>) |
| Mergesort | O(n log n) | O(n log n) |
| Quicksort | O(n log n) | O(n<sup>2</sup>) |

## 3. Features

- Multiple sorting algorithm implementations.
- Random, sorted, reverse-sorted, and nearly-sorted dataset generation.
- Scaling experiments across different dataset sizes.
- Comparative experiments using identical datasets.
- Benchmark trials with median execution-time calculations.
- Matplotlib graphing of results.
- JSON import/export of benchmark results.

## 4. Project Structure
```
sorting-algorithm-lab/
├── benchmark.py                      # Benchmark sorting algorithms
├── generate_data.py                  # Data generation module
├── main.py                           # Main application code
├── requirements.txt                  # Project external requirements
├── results/                          # Results directory
│   ├── comparison/                   # Comparison test result JSONs
│   └── scaled/                       # Scaled test result JSONs
├── saving.py                         # Saving and loading JSON files
├── sorts.py                          # Sorting algorithms
├── tests/                            # Program unit tests
├── visualization.py                  # Visualization module
└── README.md                         # Project overview
```

## 5. Installation

### Linux:
```
git clone https://github.com/codederg/sorting-algorithm-lab
cd sorting-algorithm-lab

python -m venv .venv

source ./.venv/bin/activate
pip install -r requirements.txt
```

## 6. Usage
Launch the program via:
```
python main.py
```
Using the CLI, run commands via number-based prompts.
#### Scaling lab:
- ```Command: 1```
- Select amount of data sets
- Select the length of the first data set
- Select the amount each data set's length will increase by
- Select data generation method
- View execution times via line graph
#### Comparison lab:
- ```Command: 2```
- Select the length of the tested data set
- Select data generation method
- View execution times via bar chart
#### Loading:
- ```Command: 3```
- Input file path of appropriate JSON

## 7. Benchmark Methodology
- Timing uses ```time.perf_counter()``` to get execution time, and is converted to milliseconds.
- Multiple trials are conducted per experiment.
- Median execution time is displayed to reduce the influence of outliers.
- Allows the setting of random or fixed seeds.
- The execution times are influenced by several outside factors, such as hardware and memory usage.
