
def bubble_sort(items: list[int]) -> list[int]:
    """Sort a list in ascending order using the bubble sort algorithm.

    Args:
        items (list[int]): A list of elements to be sorted.

    Returns:
        list[int]: The sorted list in ascending order.
    """

    # Create a shallow copy to prevent modifying the original list.
    items = items.copy()

    n = len(items)

    for i in range(n):
        for j in range(0, n - i - 1):
            # Swap elements if the element found is greater than the next.
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
    
    return items

def insertion_sort(items: list[int]) -> list[int]:
    """Sort a list in ascending order using the insertion sort algorithm.

    Args:
        items (list[int]): A list of elements to be sorted.

    Returns:
        list[int]: The sorted list in ascending order.
    """
    # Create a shallow copy to prevent modifying the original list.
    items = items.copy()

    # Start at the second index
    for i in range(1, len(items)):
        key = items[i]  # Track the value being sorted.
        j = i - 1

        # Iterate through sorted elements in order to find where the sorted key must go.
        while j >= 0 and items[j] > key:
            items[j + 1] = items[j]
            j -= 1

        # Insert the key in the sorted position.
        items[j + 1] = key
    
    return items

def selection_sort(items: list[int]) -> list[int]:
    """Sort a list in ascending order using the selection sort algorithm.
    
    Args:
        items (list[int]): A list of elements to be sorted.
    
    Returns:
        list[int]: The sorted list in ascending order.
    """
    
    # Create a shallow copy to prevent modifying the original list.
    items = items.copy()

    n = len(items)

    # Move through the unsorted portion of the list.
    # Do not loop through the last index, as it is 
    # expected to already be the greatest/sorted value.
    for i in range(n - 1):
        min_index = i

        # Iterate through the unsorted elements to find the smallest value.
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j

        # Swap the minimum element with the first 
        # unsorted element to effectively sort the minimum value
        if min_index != i:
            items[i], items[min_index] = items[min_index], items[i]

    return items