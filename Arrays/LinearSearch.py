def linear_search(arr, target):
    """
    Traverse the array and check each element.
    Returns the index if found, otherwise -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # element found, return its index
    return -1  # element not found


# Example usage
if __name__ == "__main__":
    arr = [3, 90, 7, 1, 5, 9, 20, 8, 4, 6]
    target = 8

    result = linear_search(arr, target)

    if result != -1:
        print(f"{target} is present at index {result} of the array.")
    else:
        print(f"{target} is not present in the array.")