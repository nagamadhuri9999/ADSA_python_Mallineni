# Day 7: Practice Problems on Space Complexity, Searching, and Sorting
# --------------------------------------------------------

def day7_problem_1(arr):
    # Practice: Implement Iterative Binary Search
    # --- SOLUTION ---
    # Assuming array is sorted and target is 10
    target = 10
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

def day7_problem_2(arr):
    # Practice: Implement Bubble Sort
    # --- SOLUTION ---
    n = len(arr)
    for j in range(n):
        for k in range(0, n-j-1):
            if arr[k] > arr[k+1]:
                arr[k], arr[k+1] = arr[k+1], arr[k]
    return arr

def day7_problem_3(arr):
    # Practice: Implement Selection Sort
    # --- SOLUTION ---
    n = len(arr)
    for j in range(n):
        min_idx = j
        for k in range(j+1, n):
            if arr[k] < arr[min_idx]:
                min_idx = k
        arr[j], arr[min_idx] = arr[min_idx], arr[j]
    return arr

def day7_problem_4(arr):
    # Practice: Implement Insertion Sort
    # --- SOLUTION ---
    for j in range(1, len(arr)):
        key = arr[j]
        k = j - 1
        while k >= 0 and key < arr[k]:
            arr[k+1] = arr[k]
            k -= 1
        arr[k+1] = key
    return arr

def day7_problem_5(arr):
    # Practice: Analyze Space Complexity for an array duplication
    # --- SOLUTION ---
    # Duplicating an array requires O(N) space.
    arr_copy = arr.copy()
    return arr_copy
