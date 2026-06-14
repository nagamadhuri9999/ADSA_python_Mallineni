# Day 7 Examples: Space Complexity, Searching, and Sorting Algorithms

print("--- 1. Iterative Binary Search ---")
def binary_search_iterative(arr, target):
    """
    Requires a sorted array. Divides search space in half.
    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target2 = 23
print(f"Sorted List: {sorted_data}")
print(f"Searching for {target2} using Binary Search...")
print(f"Found at index: {binary_search_iterative(sorted_data, target2)}\n")

print("--- 2. Bubble Sort ---")
def bubble_sort(arr):
    """
    Swaps adjacent elements if they are out of order.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    return arr

unsorted_data1 = [64, 34, 25, 12, 22, 11, 90]
print(f"Original List: {unsorted_data1}")
print(f"Bubble Sorted: {bubble_sort(unsorted_data1.copy())}\n")

print("--- 3. Selection Sort ---")
def selection_sort(arr):
    """
    Selects the smallest element and places it at the beginning.
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        # Swap the found minimum element with the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

unsorted_data2 = [64, 25, 12, 22, 11]
print(f"Original List: {unsorted_data2}")
print(f"Selection Sorted: {selection_sort(unsorted_data2.copy())}\n")

print("--- 4. Insertion Sort ---")
def insertion_sort(arr):
    """
    Builds the final sorted array one item at a time.
    Time Complexity: O(N^2) worst case, O(N) best case (nearly sorted)
    Space Complexity: O(1)
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

unsorted_data3 = [12, 11, 13, 5, 6]
print(f"Original List: {unsorted_data3}")
print(f"Insertion Sorted: {insertion_sort(unsorted_data3.copy())}\n")
