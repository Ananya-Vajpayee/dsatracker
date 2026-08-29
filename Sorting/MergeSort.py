def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    Approach: Divide and Conquer.
    """
    # Base case: an array of 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the two sorted halves into one sorted array
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Merges two already-sorted lists into a single sorted list.
    """
    result = []
    i = j = 0  # pointers for left and right lists

    # Compare elements from both lists and pick the smaller one each time
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One of the two lists may still have leftover elements — append them
    result.extend(left[i:])
    result.extend(right[j:])

    return result


if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before sorting:", arr)
    sorted_arr = merge_sort(arr)
    print("After sorting: ", sorted_arr)