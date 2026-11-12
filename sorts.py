
def bubble_sort(array: list[int]) -> list[int]:
    """Sort a list in ascending order using the bubble sort algorithm.

    Args:
        array (list[int]): A list of elements to be sorted.

    Returns:
        list[int]: The sorted list in ascending order.
    """

    # Create a shallow copy to prevent modifying the original list.
    array = array.copy()

    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap elements if the element found is greater than the next.
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    return array

def insertion_sort(array: list[int]) -> list[int]:

    # Create a shallow copy to prevent modifying the original list.
    array = array.copy()

    # Start at the second index
    for i in range(1, len(array)):
        key = array[i]  # Track the value being sorted.
        j = i - 1

        # Iterate through sorted elements in order to find where the sorted key must go.
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # Insert the key in the sorted position.
        array[j + 1] = key
    
    return array