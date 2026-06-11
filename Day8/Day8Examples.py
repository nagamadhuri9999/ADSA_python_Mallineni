# Day 8 Examples: Advanced Sorting Algorithms

print("--- 1. Merge Sort ---")
def merge_sort(arr):
    """
    Divide and Conquer Algorithm.
    Time Complexity: O(N log N)
    Space Complexity: O(N)
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Merging the two halves
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

unsorted_data1 = [38, 27, 43, 3, 9, 82, 10]
print(f"Original List: {unsorted_data1}")
print(f"Merge Sorted:  {merge_sort(unsorted_data1.copy())}\n")


print("--- 2. Quick Sort ---")
def quick_sort(arr):
    """
    Divide and Conquer Algorithm using Partitioning.
    Time Complexity: O(N log N) average, O(N^2) worst case.
    Space Complexity: O(log N)
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

unsorted_data2 = [10, 7, 8, 9, 1, 5]
print(f"Original List: {unsorted_data2}")
print(f"Quick Sorted:  {quick_sort(unsorted_data2)}\n")


print("--- 3. Python's Built-in Sort (Timsort) ---")
unsorted_data3 = [5, 2, 9, 1, 5, 6]
print(f"Original List: {unsorted_data3}")
# sorted() returns a new list
print(f"sorted() func: {sorted(unsorted_data3)}")
# .sort() modifies the list in place
unsorted_data3.sort()
print(f".sort() method:{unsorted_data3}\n")
