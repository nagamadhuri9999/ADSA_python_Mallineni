# Day 8: Practice Problems on Advanced Sorting Algorithms
# --------------------------------------------------------
import time
import random

# ==========================================
# PROBLEM 1: Merge Sort Implementation
# ==========================================
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merging phase
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr


# ==========================================
# PROBLEM 2: Quick Sort Implementation
# ==========================================
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)


# ==========================================
# PROBLEM 3: Sort Colors (LeetCode 75)
# ==========================================
# Given an array with n objects colored red, white, or blue (represented as 0, 1, 2)
# Sort them in-place so that objects of the same color are adjacent.
# Hint: Dutch National Flag algorithm (O(N) time).
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


# ==========================================
# PROBLEM 4: Merge Intervals (LeetCode 56)
# ==========================================
# Given an array of intervals where intervals[i] = [start_i, end_i],
# merge all overlapping intervals.
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals by their start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    for current in intervals[1:]:
        previous = merged[-1]
        
        # If the current interval overlaps with the previous one, merge them
        if current[0] <= previous[1]:
            previous[1] = max(previous[1], current[1])
        else:
            merged.append(current)
            
    return merged


# ==========================================
# PROBLEM 5: Kth Largest Element (LeetCode 215)
# ==========================================
# Find the kth largest element in an unsorted array.
def find_kth_largest(nums, k):
    # Easiest way in Python is to sort and return the element at -k index.
    # Advanced approach uses a Min-Heap or Quickselect.
    nums.sort()
    return nums[-k]


# ==========================================
# PROBLEM 6: Factorial using Recursion
# ==========================================
def factorial(n):
    # Base Case
    if n == 0 or n == 1:
        return 1
    # Recursive Case
    return n * factorial(n - 1)


# ==========================================
# PROBLEM 7: Fibonacci using Recursion
# ==========================================
def fibonacci(n):
    # Base Cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive Case
    return fibonacci(n - 1) + fibonacci(n - 2)


# ==========================================
# PROBLEM 8: Sum of Array using Recursion
# ==========================================
def sum_array(arr):
    # Base Case
    if len(arr) == 0:
        return 0
    # Recursive Case: First element + sum of the rest
    return arr[0] + sum_array(arr[1:])


if __name__ == "__main__":
    print("Testing Merge Sort:")
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print(merge_sort(arr1))
    
    print("\nTesting Quick Sort:")
    arr2 = [10, 7, 8, 9, 1, 5]
    print(quick_sort(arr2))
    
    print("\nTesting Sort Colors (0, 1, 2):")
    colors = [2, 0, 2, 1, 1, 0]
    print(sort_colors(colors))
    
    print("\nTesting Merge Intervals:")
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(intervals))
    
    print("\nTesting Kth Largest Element (k=2):")
    nums = [3,2,1,5,6,4]
    print(find_kth_largest(nums, 2))

    print("\nTesting Factorial (5!):")
    print(factorial(5))

    print("\nTesting Fibonacci (7th number):")
    print(fibonacci(7))

    print("\nTesting Sum of Array ([1, 2, 3, 4, 5]):")
    print(sum_array([1, 2, 3, 4, 5]))
