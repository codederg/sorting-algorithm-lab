
def bubble_sort(array: list[int]) -> list[int]:
    # Create a shallow copy to prevent modifying the original list.
    array = array.copy()

    n = len(array)

    # Move through all elements.
    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap elements if the element found is greater than the next.
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array
