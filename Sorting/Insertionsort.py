def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    Approach: Build the sorted array one element at a time.
    """
    n = len(arr)

    # Start from the second element (index 1); index 0 is
    # trivially "sorted" on its own
    for i in range(1, n):
        key = arr[i]        # the element we're currently placing
        j = i - 1            # start comparing with the element just before it

        # Shift elements of the sorted part that are greater than 'key'
        # one position to the right, to make room for 'key'
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place 'key' in its correct position
        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before sorting:", arr)
    sorted_arr = insertion_sort(arr)
    print("After sorting: ", sorted_arr)