# Day 6 Practice Problems: Searching Algorithms and Big O
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_linear_search_basic():
    # TODO: Write a function to find the index of `target` in `arr`. If not found, return -1.
    pass

    # --- SOLUTION ---
    # def linear_search(arr, target):
    #     for i in range(len(arr)):
    #         if arr[i] == target: return i
    #     return -1


def problem_2_linear_search_count():
    # TODO: Write a function that returns how many times `target` appears in `arr`.
    pass

    # --- SOLUTION ---
    # def linear_search_count(arr, target):
    #     count = 0
    #     for item in arr:
    #         if item == target: count += 1
    #     return count


def problem_3_linear_search_all_indices():
    # TODO: Write a function that returns a list of all indices where `target` appears in `arr`.
    pass

    # --- SOLUTION ---
    # def linear_search_all(arr, target):
    #     indices = []
    #     for i in range(len(arr)):
    #         if arr[i] == target: indices.append(i)
    #     return indices


def problem_4_binary_search_basic():
    # TODO: Implement basic binary search. Return the index of `target` in SORTED `arr`, or -1.
    pass

    # --- SOLUTION ---
    # def binary_search(arr, target):
    #     left, right = 0, len(arr) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target: return mid
    #         elif arr[mid] < target: left = mid + 1
    #         else: right = mid - 1
    #     return -1


def problem_5_binary_search_recursive():
    # TODO: Implement binary search using recursion instead of a while loop.
    pass

    # --- SOLUTION ---
    # def binary_search_rec(arr, target, left, right):
    #     if left > right: return -1
    #     mid = (left + right) // 2
    #     if arr[mid] == target: return mid
    #     elif arr[mid] < target: return binary_search_rec(arr, target, mid + 1, right)
    #     else: return binary_search_rec(arr, target, left, mid - 1)


def problem_6_find_first_occurrence():
    # TODO: In a sorted array with duplicates, find the FIRST index of `target` using binary search.
    pass

    # --- SOLUTION ---
    # def first_occurrence(arr, target):
    #     left, right = 0, len(arr) - 1
    #     result = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target:
    #             result = mid
    #             right = mid - 1  # Keep searching left
    #         elif arr[mid] < target: left = mid + 1
    #         else: right = mid - 1
    #     return result


def problem_7_find_last_occurrence():
    # TODO: In a sorted array with duplicates, find the LAST index of `target` using binary search.
    pass

    # --- SOLUTION ---
    # def last_occurrence(arr, target):
    #     left, right = 0, len(arr) - 1
    #     result = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target:
    #             result = mid
    #             left = mid + 1  # Keep searching right
    #         elif arr[mid] < target: left = mid + 1
    #         else: right = mid - 1
    #     return result


def problem_8_is_sorted():
    # TODO: Write a function to check if a list is sorted in ascending order (return True/False).
    pass

    # --- SOLUTION ---
    # def is_sorted(arr):
    #     for i in range(1, len(arr)):
    #         if arr[i] < arr[i - 1]: return False
    #     return True


def problem_9_search_insert_position():
    # TODO: Find index where target should be inserted in a sorted array to maintain order.
    pass

    # --- SOLUTION ---
    # def search_insert(arr, target):
    #     left, right = 0, len(arr) - 1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid] == target: return mid
    #         elif arr[mid] < target: left = mid + 1
    #         else: right = mid - 1
    #     return left


def problem_10_linear_search_max():
    # TODO: Find the maximum element in an unsorted array using linear search.
    pass

    # --- SOLUTION ---
    # def find_max(arr):
    #     if not arr: return None
    #     maximum = arr[0]
    #     for item in arr:
    #         if item > maximum: maximum = item
    #     return maximum


def problem_11_linear_search_min():
    # TODO: Find the minimum element in an unsorted array using linear search.
    pass

    # --- SOLUTION ---
    # def find_min(arr):
    #     if not arr: return None
    #     minimum = arr[0]
    #     for item in arr:
    #         if item < minimum: minimum = item
    #     return minimum


def problem_12_count_even_numbers():
    # TODO: Use a linear scan to count how many even numbers are in `arr`.
    pass

    # --- SOLUTION ---
    # def count_evens(arr):
    #     count = 0
    #     for n in arr:
    #         if n % 2 == 0: count += 1
    #     return count


def problem_13_contains_vowel():
    # TODO: Use linear search to check if a string contains any vowels.
    pass

    # --- SOLUTION ---
    # def has_vowel(s):
    #     vowels = "aeiouAEIOU"
    #     for char in s:
    #         if char in vowels: return True
    #     return False


def problem_14_find_prefix():
    # TODO: Return a list of all strings in `arr` that start with `prefix`.
    pass

    # --- SOLUTION ---
    # def find_prefix(arr, prefix):
    #     result = []
    #     for s in arr:
    #         if s.startswith(prefix): result.append(s)
    #     return result


def problem_15_find_peak_linear():
    # TODO: A peak element is greater than its neighbors. Find the first peak using linear search.
    pass

    # --- SOLUTION ---
    # def find_peak(arr):
    #     n = len(arr)
    #     if n == 1: return 0
    #     if arr[0] >= arr[1]: return 0
    #     for i in range(1, n - 1):
    #         if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]: return i
    #     if arr[n - 1] >= arr[n - 2]: return n - 1
    #     return -1


def problem_16_find_boolean_transition():
    # TODO: Given an array like [False, False, True, True], find the index of the first True using binary search.
    pass

    # --- SOLUTION ---
    # def first_true(arr):
    #     left, right = 0, len(arr) - 1
    #     result = -1
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if arr[mid]:
    #             result = mid
    #             right = mid - 1
    #         else:
    #             left = mid + 1
    #     return result


def problem_17_search_2d_linear():
    # TODO: Find target in a 2D matrix (list of lists) using nested linear search. Return (row, col) or (-1, -1).
    pass

    # --- SOLUTION ---
    # def search_2d(matrix, target):
    #     for r in range(len(matrix)):
    #         for c in range(len(matrix[0])):
    #             if matrix[r][c] == target: return (r, c)
    #     return (-1, -1)


def problem_18_square_root_binary_search():
    # TODO: Use binary search to find the integer square root of x (e.g., int_sqrt(8) = 2).
    pass

    # --- SOLUTION ---
    # def int_sqrt(x):
    #     if x < 2: return x
    #     left, right = 1, x // 2
    #     while left <= right:
    #         mid = (left + right) // 2
    #         if mid * mid == x: return mid
    #         elif mid * mid < x: left = mid + 1
    #         else: right = mid - 1
    #     return right


def problem_19_guess_number_game():
    # TODO: Imagine a hidden number. Implement the binary search strategy to guess it given a `guess(num)` API.
    pass

    # --- SOLUTION ---
    # def guessNumber(n):
    #     left, right = 1, n
    #     while left <= right:
    #         mid = (left + right) // 2
    #         res = guess(mid)  # assume guess() is provided by the problem
    #         if res == 0: return mid
    #         elif res == 1: left = mid + 1
    #         else: right = mid - 1


def problem_20_count_rotations():
    # TODO: Find how many times a sorted array has been rotated (index of minimum element) using linear search.
    pass

    # --- SOLUTION ---
    # def count_rotations(arr):
    #     for i in range(1, len(arr)):
    #         if arr[i] < arr[i - 1]: return i
    #     return 0


if __name__ == "__main__":
    print("Welcome to Day 6 Practice Problems!")
