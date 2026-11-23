# Summary

To compile the results of various tests, each sorting algorithm shows widely varied results as consequence to the conditions they are sorting under. For example, while having an average of O(n<sup>2</sup>) execution time, insertion sort can become even quicker than logarithmic sorting algorithm functions when sorting already sorted data.

On average, bubble sort has the longest execution times, indicating that its simplicity comes at the cost of speed. Additionally, algorithms such as mergesort and quicksort boast considerably faster execution times as a result of their "divide-and-conquer" methods of sorting data.

From outside research, the differences in execution times is widely based in the amount of writes these algorithms do, as writing data to memory takes more time and effort compared to pure comparison.

These results serve to show how different algorithms have certain strengths and weaknesses. This knowledge can provide solutions on how to effectively sort data as quickly as possible and explains how various built-in sorting algorithms serve to work (e.g., Python's own list.sort() method).
