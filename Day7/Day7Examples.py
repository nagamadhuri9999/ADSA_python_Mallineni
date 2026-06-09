# Day 7 Examples: Searching Algorithms

print("--- 1. Linear Search Implementation ---")
def linear_search(arr, target):
    """
    Checks every element one by one.
    Time Complexity: O(N)
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

unsorted_data = [42, 15, 8, 99, 23, 4]
target1 = 23
print(f"List: {unsorted_data}")
print(f"Searching for {target1} using Linear Search...")
index1 = linear_search(unsorted_data, target1)
print(f"Found at index: {index1}\n")

input("Press Enter to see Binary Search...")

print("--- 2. Iterative Binary Search ---")
def binary_search_iterative(arr, target):
    """
    Requires a sorted array. Divides search space in half.
    Time Complexity: O(log N)
    """
    low = 0
    high = len(arr) - 1
    steps = 0
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        print(f"Step {steps}: low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1 # Discard left half
        else:
            high = mid - 1 # Discard right half
            
    return -1

sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target2 = 23
print(f"Sorted List: {sorted_data}")
print(f"Searching for {target2} using Binary Search...")
index2 = binary_search_iterative(sorted_data, target2)
print(f"Found at index: {index2}\n")

input("Press Enter to see Recursive Binary Search...")

print("--- 3. Recursive Binary Search ---")
def binary_search_recursive(arr, target, low, high):
    """
    Same O(log N) complexity, but uses the call stack.
    """
    # Base Case 1: Target not found
    if low > high:
        return -1
        
    mid = (low + high) // 2
    
    # Base Case 2: Target found
    if arr[mid] == target:
        return mid
    # Recursive step: Right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    # Recursive step: Left half
    else:
        return binary_search_recursive(arr, target, low, mid - 1)

target3 = 72
print(f"Searching for {target3} using Recursive Binary Search...")
index3 = binary_search_recursive(sorted_data, target3, 0, len(sorted_data)-1)
print(f"Found at index: {index3}\n")
