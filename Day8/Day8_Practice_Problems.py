# Day 8 Practice Problems: Advanced Sorting & Recursion
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_recursion_base_case():
    # TODO: Write a recursive function print_num(n) that prints n down to 1. Don't forget the base case!
    pass

    # --- SOLUTION ---
    # def print_num(n):
    #     if n <= 0: return
    #     print(n)
    #     print_num(n - 1)


def problem_2_recursive_sum_array():
    # TODO: Write a recursive function to sum elements in an array. Base case: empty array -> 0.
    pass

    # --- SOLUTION ---
    # def sum_array(arr):
    #     if len(arr) == 0: return 0
    #     return arr[0] + sum_array(arr[1:])


def problem_3_merge_two_sorted_lists():
    # TODO: Given lst1 = [1, 3] and lst2 = [2, 4], use a two-pointer approach to merge them into [1, 2, 3, 4].
    pass

    # --- SOLUTION ---
    # def merge(lst1, lst2):
    #     res = []
    #     i = j = 0
    #     while i < len(lst1) and j < len(lst2):
    #         if lst1[i] < lst2[j]:
    #             res.append(lst1[i])
    #             i += 1
    #         else:
    #             res.append(lst2[j])
    #             j += 1
    #     res.extend(lst1[i:])
    #     res.extend(lst2[j:])
    #     return res


def problem_4_merge_sort_split():
    # TODO: Write just the 'Divide' part of Merge Sort. Return the left_half and right_half.
    pass

    # --- SOLUTION ---
    # def split_list(arr):
    #     mid = len(arr) // 2
    #     return arr[:mid], arr[mid:]


def problem_5_merge_sort_full():
    # TODO: Combine your logic from problem 3 and 4 to implement full Merge Sort.
    pass

    # --- SOLUTION ---
    # def merge_sort(arr):
    #     if len(arr) <= 1: return arr
    #     mid = len(arr) // 2
    #     left = merge_sort(arr[:mid])
    #     right = merge_sort(arr[mid:])
    #     return merge(left, right) # Using merge from problem 3


def problem_6_quick_sort_partition():
    # TODO: Given arr and a pivot, create lists for elements < pivot, == pivot, and > pivot.
    pass

    # --- SOLUTION ---
    # def simple_partition(arr, pivot):
    #     left = [x for x in arr if x < pivot]
    #     middle = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x > pivot]
    #     return left, middle, right


def problem_7_quick_sort_full():
    # TODO: Implement full Quick Sort using list comprehensions for the partitioning step.
    pass

    # --- SOLUTION ---
    # def quick_sort(arr):
    #     if len(arr) <= 1: return arr
    #     pivot = arr[len(arr) // 2]
    #     left = [x for x in arr if x < pivot]
    #     mid = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x > pivot]
    #     return quick_sort(left) + mid + quick_sort(right)


def problem_8_sort_tuples():
    # TODO: Use Python's built-in sorted() to sort a list of tuples by their SECOND element.
    # Ex: [(1, 3), (2, 1), (4, 2)] -> [(2, 1), (4, 2), (1, 3)]
    pass

    # --- SOLUTION ---
    # def sort_by_second(tuples_list):
    #     return sorted(tuples_list, key=lambda x: x[1])


def problem_9_sort_strings_by_length():
    # TODO: Sort ["apple", "bat", "cherry"] by length, shortest first.
    pass

    # --- SOLUTION ---
    # def sort_by_len(words):
    #     return sorted(words, key=len)


def problem_10_recursive_string_reverse():
    # TODO: Reverse a string using recursion.
    pass

    # --- SOLUTION ---
    # def reverse_string(s):
    #     if len(s) == 0: return ""
    #     return s[-1] + reverse_string(s[:-1])


def problem_11_recursive_power():
    # TODO: Write a recursive function to calculate base^exp.
    pass

    # --- SOLUTION ---
    # def power(base, exp):
    #     if exp == 0: return 1
    #     return base * power(base, exp - 1)


def problem_12_quick_sort_descending():
    # TODO: Modify Quick Sort to sort in descending order.
    pass

    # --- SOLUTION ---
    # def quick_sort_desc(arr):
    #     if len(arr) <= 1: return arr
    #     pivot = arr[len(arr) // 2]
    #     left = [x for x in arr if x > pivot] # Flipped to >
    #     mid = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x < pivot] # Flipped to <
    #     return quick_sort_desc(left) + mid + quick_sort_desc(right)


def problem_13_check_stability_concept():
    # TODO: Will the dictionary method for grouping anagrams (Day 4) maintain the original order of words?
    pass
    # Hint: Prior to Python 3.7 dictionaries didn't guarantee order. Now they do, but the concept of stability usually applies to sorting.


def problem_14_merge_three_arrays():
    # TODO: You have 3 sorted arrays. How would you merge them using your merge() function from Problem 3?
    pass

    # --- SOLUTION ---
    # def merge_three(l1, l2, l3):
    #     # Merge l1 and l2, then merge the result with l3
    #     return merge(merge(l1, l2), l3)


def problem_15_recursive_fib_memoization():
    # TODO: Implement recursive Fibonacci, but use a dictionary to "remember" calculated values (memoization).
    pass

    # --- SOLUTION ---
    # memo = {}
    # def fib(n):
    #     if n in memo: return memo[n]
    #     if n <= 1: return n
    #     memo[n] = fib(n - 1) + fib(n - 2)
    #     return memo[n]


def problem_16_find_median_unsorted():
    # TODO: Find the median of an unsorted list of integers (hint: sort it first).
    pass

    # --- SOLUTION ---
    # def find_median(arr):
    #     arr = sorted(arr)
    #     mid = len(arr) // 2
    #     if len(arr) % 2 == 0:
    #         return (arr[mid - 1] + arr[mid]) / 2.0
    #     else:
    #         return arr[mid]


def problem_17_sort_ignoring_case():
    # TODO: Sort ["Banana", "apple", "Cherry"] ignoring case.
    pass

    # --- SOLUTION ---
    # def sort_ignore_case(words):
    #     return sorted(words, key=str.lower)


def problem_18_sort_dictionaries_by_value():
    # TODO: Given data = [{'name': 'A', 'age': 30}, {'name': 'B', 'age': 20}], sort by 'age'.
    pass

    # --- SOLUTION ---
    # def sort_dicts(data):
    #     return sorted(data, key=lambda x: x['age'])


def problem_19_in_place_partition():
    # TODO: Challenge: Do the Quick Sort partition step in-place by swapping elements without creating new lists.
    pass

    # --- SOLUTION ---
    # def in_place_partition(arr, low, high):
    #     pivot = arr[high]
    #     i = low - 1
    #     for j in range(low, high):
    #         if arr[j] <= pivot:
    #             i = i + 1
    #             arr[i], arr[j] = arr[j], arr[i]
    #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #     return i + 1


def problem_20_in_place_quicksort_full():
    # TODO: Challenge: Implement the full Quick Sort recursively using the in-place partition.
    pass

    # --- SOLUTION ---
    # def in_place_quicksort(arr, low, high):
    #     if low < high:
    #         pi = in_place_partition(arr, low, high)
    #         in_place_quicksort(arr, low, pi - 1)
    #         in_place_quicksort(arr, pi + 1, high)


if __name__ == "__main__":
    print("Welcome to Day 8 Practice Problems!")
