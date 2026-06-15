# MASTER PRACTICE PROBLEMS COLLECTION
# ======================================


# ==================================================
# --- Day10 : Day10_Practice_Problems.py ---
# ==================================================

# Day 10 Practice Problems: Introduction to Linked Lists
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# ==========================================
# Problems 1-10: Basic Setup & Traversal
# ==========================================

def problem_1_create_node():
    # TODO: Create a Node holding the value 42 and print its data.
    pass

    # --- SOLUTION ---
    # node = Node(42)
    # print(node.data)


def problem_2_link_two_nodes():
    # TODO: Create two nodes (val 10, val 20). Link the first to the second.
    pass

    # --- SOLUTION ---
    # n1 = Node(10)
    # n2 = Node(20)
    # n1.next = n2


def problem_3_create_linked_list():
    # TODO: Initialize an empty LinkedList object. Check if its head is None.
    pass

    # --- SOLUTION ---
    # ll = LinkedList()
    # print(ll.head is None)


def problem_4_manual_list_creation():
    # TODO: Create a LinkedList, set head to Node(1), link head.next to Node(2).
    pass

    # --- SOLUTION ---
    # ll = LinkedList()
    # ll.head = Node(1)
    # ll.head.next = Node(2)


def problem_5_traverse_and_print():
    # TODO: Given a LinkedList `ll`, write a while loop to print all node data.
    pass

    # --- SOLUTION ---
    # current = ll.head
    # while current is not None:
    #     print(current.data)
    #     current = current.next


def problem_6_count_nodes():
    # TODO: Given a LinkedList `ll`, traverse it and return the total number of nodes.
    pass

    # --- SOLUTION ---
    # current = ll.head
    # count = 0
    # while current is not None:
    #     count += 1
    #     current = current.next
    # return count


def problem_7_search_node():
    # TODO: Write a function that returns True if `target` exists in the LinkedList.
    pass

    # --- SOLUTION ---
    # def search(ll, target):
    #     current = ll.head
    #     while current:
    #         if current.data == target: return True
    #         current = current.next
    #     return False


def problem_8_get_tail():
    # TODO: Traverse to the last node of the list and return its data. Return None if empty.
    pass

    # --- SOLUTION ---
    # def get_tail_data(ll):
    #     if not ll.head: return None
    #     current = ll.head
    #     while current.next: # Stop AT the last node
    #         current = current.next
    #     return current.data


def problem_9_sum_nodes():
    # TODO: Return the sum of all node values in a LinkedList of integers.
    pass

    # --- SOLUTION ---
    # def sum_list(ll):
    #     total = 0
    #     current = ll.head
    #     while current:
    #         total += current.data
    #         current = current.next
    #     return total


def problem_10_find_max():
    # TODO: Return the maximum value in a LinkedList.
    pass

    # --- SOLUTION ---
    # def find_max(ll):
    #     if not ll.head: return None
    #     max_val = ll.head.data
    #     current = ll.head.next
    #     while current:
    #         if current.data > max_val: max_val = current.data
    #         current = current.next
    #     return max_val


# ==========================================
# Problems 11-20: Insertions & Modifications
# ==========================================

def problem_11_insert_at_head():
    # TODO: Add a method to LinkedList class: `def insert_head(self, data):`
    pass

    # --- SOLUTION ---
    # def insert_head(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node


def problem_12_insert_at_tail():
    # TODO: Add a method to LinkedList class: `def insert_tail(self, data):`
    pass

    # --- SOLUTION ---
    # def insert_tail(self, data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #     current.next = new_node


def problem_13_insert_after_node():
    # TODO: Given a specific Node object `prev_node` and `data`, insert a new node right after it.
    pass

    # --- SOLUTION ---
    # def insert_after(prev_node, data):
    #     if not prev_node: return
    #     new_node = Node(data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node


def problem_14_delete_head():
    # TODO: Remove the head node from the LinkedList and return its data.
    pass

    # --- SOLUTION ---
    # def delete_head(self):
    #     if not self.head: return None
    #     val = self.head.data
    #     self.head = self.head.next
    #     return val


def problem_15_delete_tail():
    # TODO: Traverse to the end and remove the last node. (Hint: stop at the SECOND to last node).
    pass

    # --- SOLUTION ---
    # def delete_tail(self):
    #     if not self.head: return None
    #     if not self.head.next:
    #         val = self.head.data
    #         self.head = None
    #         return val
    #     current = self.head
    #     while current.next.next: # Stop at second to last
    #         current = current.next
    #     val = current.next.data
    #     current.next = None
    #     return val


def problem_16_build_from_list():
    # TODO: Given a Python list `[1, 2, 3]`, build a LinkedList holding these values in order.
    pass

    # --- SOLUTION ---
    # def build_ll(arr):
    #     ll = LinkedList()
    #     for val in reversed(arr): # Insert at head is O(1)
    #         ll.insert_head(val)
    #     return ll


def problem_17_convert_to_list():
    # TODO: Traverse a LinkedList and append all values into a standard Python list, returning it.
    pass

    # --- SOLUTION ---
    # def to_list(ll):
    #     res = []
    #     current = ll.head
    #     while current:
    #         res.append(current.data)
    #         current = current.next
    #     return res


def problem_18_clear_list():
    # TODO: Remove all nodes from the LinkedList (in Python, just remove the head reference!).
    pass

    # --- SOLUTION ---
    # def clear(self):
    #     self.head = None # Garbage collector handles the rest


def problem_19_replace_value():
    # TODO: Traverse the list and replace all occurrences of `old_val` with `new_val`.
    pass

    # --- SOLUTION ---
    # def replace(ll, old_val, new_val):
    #     current = ll.head
    #     while current:
    #         if current.data == old_val:
    #             current.data = new_val
    #         current = current.next


def problem_20_print_formatted():
    # TODO: Print the list exactly like "1 -> 2 -> 3 -> None".
    pass

    # --- SOLUTION ---
    # def print_ll(ll):
    #     current = ll.head
    #     while current:
    #         print(f"{current.data} -> ", end="")
    #         current = current.next
    #     print("None")


if __name__ == "__main__":
    print("Welcome to Day 10 Practice Problems!")

# ==================================================
# --- Day9 : Day9_Practice_Problems.py ---
# ==================================================

# Day 9 Practice Problems: Advanced Sorting Mechanics
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_quickselect_base():
    # TODO: Implement the partitioning step of QuickSelect for an array and a pivot.
    pass

    # --- SOLUTION ---
    # def partition_lists(arr, pivot):
    #     left = [x for x in arr if x < pivot]
    #     mid = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x > pivot]
    #     return left, mid, right


def problem_2_quickselect_full():
    # TODO: Implement full QuickSelect to find the k-th smallest element. (k is 1-indexed)
    pass

    # --- SOLUTION ---
    # def quickselect(arr, k):
    #     if len(arr) == 1: return arr[0]
    #     pivot = arr[len(arr) // 2]
    #     left = [x for x in arr if x < pivot]
    #     mid = [x for x in arr if x == pivot]
    #     right = [x for x in arr if x > pivot]
    #     if k <= len(left): return quickselect(left, k)
    #     elif k <= len(left) + len(mid): return pivot
    #     else: return quickselect(right, k - len(left) - len(mid))


def problem_3_kth_largest():
    # TODO: Use your quickselect function to find the k-th LARGEST element.
    pass

    # --- SOLUTION ---
    # def kth_largest(arr, k):
    #     # k-th largest is the (len - k + 1)-th smallest!
    #     return quickselect(arr, len(arr) - k + 1)


def problem_4_lomuto_partition():
    # TODO: Implement Lomuto partition scheme in-place (last element is pivot).
    pass

    # --- SOLUTION ---
    # def lomuto(arr, low, high):
    #     pivot = arr[high]
    #     i = low - 1
    #     for j in range(low, high):
    #         if arr[j] <= pivot:
    #             i += 1
    #             arr[i], arr[j] = arr[j], arr[i]
    #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
    #     return i + 1


def problem_5_hoare_partition():
    # TODO: Implement Hoare partition scheme in-place (first element is pivot).
    pass

    # --- SOLUTION ---
    # def hoare(arr, low, high):
    #     pivot = arr[low]
    #     i = low - 1
    #     j = high + 1
    #     while True:
    #         i += 1
    #         while arr[i] < pivot: i += 1
    #         j -= 1
    #         while arr[j] > pivot: j -= 1
    #         if i >= j: return j
    #         arr[i], arr[j] = arr[j], arr[i]


def problem_6_counting_inversions_brute():
    # TODO: Count inversions in an array using an O(n^2) nested loop.
    pass

    # --- SOLUTION ---
    # def inversions_brute(arr):
    #     count = 0
    #     for i in range(len(arr)):
    #         for j in range(i + 1, len(arr)):
    #             if arr[i] > arr[j]: count += 1
    #     return count


def problem_7_merge_sort_inversions():
    # TODO: Modify the merge step of merge sort to also return the number of inversions found.
    pass

    # --- SOLUTION ---
    # def merge_inversions(left, right):
    #     res = []; i = j = inv = 0
    #     while i < len(left) and j < len(right):
    #         if left[i] <= right[j]:
    #             res.append(left[i])
    #             i += 1
    #         else:
    #             res.append(right[j])
    #             j += 1
    #             inv += (len(left) - i) # KEY LOGIC!
    #     res.extend(left[i:]); res.extend(right[j:])
    #     return res, inv


def problem_8_sort_with_timsort():
    # TODO: Demonstrate Timsort by sorting an array of dicts in-place by a specific key.
    pass

    # --- SOLUTION ---
    # def python_sort(arr):
    #     arr.sort(key=lambda x: x['key'])
    #     # Python's .sort() uses Timsort internally!


def problem_9_quickselect_strings():
    # TODO: Use quickselect to find the shortest string in a list.
    pass

    # --- SOLUTION ---
    # # Modify quickselect to compare len(x) instead of x, and search for k=1.


def problem_10_find_median_quickselect():
    # TODO: Find the exact median of an unsorted list using QuickSelect.
    pass

    # --- SOLUTION ---
    # def median(arr):
    #     n = len(arr)
    #     if n % 2 == 1:
    #         return quickselect(arr, n // 2 + 1)
    #     else:
    #         return 0.5 * (quickselect(arr, n // 2) + quickselect(arr, n // 2 + 1))


def problem_11_check_anagram_sorting():
    # TODO: Determine if two strings are anagrams by sorting them.
    pass

    # --- SOLUTION ---
    # def is_anagram(s1, s2):
    #     return sorted(s1) == sorted(s2)


def problem_12_sort_tuples_multiple_keys():
    # TODO: Sort a list of tuples `(name, age)` primarily by age, and secondarily by name.
    pass

    # --- SOLUTION ---
    # def sort_tuples(arr):
    #     return sorted(arr, key=lambda x: (x[1], x[0]))


def problem_13_insertion_sort_for_timsort():
    # TODO: Implement insertion sort designed for a small subarray (used as the base of Timsort).
    pass

    # --- SOLUTION ---
    # def insertion_sort_sub(arr, left, right):
    #     for i in range(left + 1, right + 1):
    #         key = arr[i]
    #         j = i - 1
    #         while j >= left and arr[j] > key:
    #             arr[j + 1] = arr[j]
    #             j -= 1
    #         arr[j + 1] = key


def problem_14_custom_comparator():
    # TODO: Write a custom comparison function to sort numbers by their absolute value.
    pass

    # --- SOLUTION ---
    # def sort_abs(arr):
    #     return sorted(arr, key=abs)


def problem_15_find_peak_element():
    # TODO: A peak is greater than its neighbors. Use a divide and conquer strategy (Binary Search) to find a peak.
    pass

    # --- SOLUTION ---
    # def find_peak(arr):
    #     left, right = 0, len(arr) - 1
    #     while left < right:
    #         mid = (left + right) // 2
    #         if arr[mid] < arr[mid + 1]: left = mid + 1
    #         else: right = mid
    #     return left


def problem_16_merge_intervals():
    # TODO: Given [[1,3],[2,6],[8,10]], sort by start time and merge overlapping intervals.
    pass

    # --- SOLUTION ---
    # def merge_intervals(intervals):
    #     intervals.sort(key=lambda x: x[0])
    #     merged = []
    #     for interval in intervals:
    #         if not merged or merged[-1][1] < interval[0]:
    #             merged.append(interval)
    #         else:
    #             merged[-1][1] = max(merged[-1][1], interval[1])
    #     return merged


def problem_17_sort_colors_dutch_flag():
    # TODO: Sort an array of 0s, 1s, and 2s in-place in O(n) time (Dutch National Flag problem).
    pass

    # --- SOLUTION ---
    # def sort_colors(arr):
    #     low, mid, high = 0, 0, len(arr) - 1
    #     while mid <= high:
    #         if arr[mid] == 0:
    #             arr[low], arr[mid] = arr[mid], arr[low]
    #             low += 1; mid += 1
    #         elif arr[mid] == 1:
    #             mid += 1
    #         else:
    #             arr[high], arr[mid] = arr[mid], arr[high]
    #             high -= 1


def problem_18_sort_by_frequency():
    # TODO: Sort an array based on the frequency of its elements (highest frequency first).
    pass

    # --- SOLUTION ---
    # from collections import Counter
    # def frequency_sort(arr):
    #     counts = Counter(arr)
    #     # Sort primarily by count (desc), secondarily by value (asc)
    #     return sorted(arr, key=lambda x: (-counts[x], x))


def problem_19_largest_number():
    # TODO: Given [10, 2], arrange them to form the largest number "210". (Hint: custom string comparison).
    pass

    # --- SOLUTION ---
    # from functools import cmp_to_key
    # def largest_number(nums):
    #     def compare(x, y):
    #         if x + y > y + x: return -1
    #         elif x + y < y + x: return 1
    #         else: return 0
    #     strs = [str(n) for n in nums]
    #     strs.sort(key=cmp_to_key(compare))
    #     return str(int("".join(strs)))


def problem_20_pancake_sort_flip():
    # TODO: Write a helper function that reverses the first `k` elements of an array in-place.
    pass

    # --- SOLUTION ---
    # def flip(arr, k):
    #     left = 0
    #     while left < k:
    #         arr[left], arr[k] = arr[k], arr[left]
    #         left += 1; k -= 1


if __name__ == "__main__":
    print("Welcome to Day 9 Practice Problems!")

# ==================================================
# --- Day8 : Day8_Practice_Problems.py ---
# ==================================================

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

# ==================================================
# --- Day7 : Day7_Practice_Problems.py ---
# ==================================================

# Day 7 Practice Problems: Space Complexity & Sorting Algorithms
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_find_max():
    # TODO: Find the maximum element in [3, 1, 8, 2] without using max().
    pass

    # --- SOLUTION ---
    # def find_max(arr):
    #     if not arr: return None
    #     maximum = arr[0]
    #     for n in arr:
    #         if n > maximum: maximum = n
    #     return maximum


def problem_2_find_min():
    # TODO: Find the minimum element in [3, 1, 8, 2] without using min().
    pass

    # --- SOLUTION ---
    # def find_min(arr):
    #     if not arr: return None
    #     minimum = arr[0]
    #     for n in arr:
    #         if n < minimum: minimum = n
    #     return minimum


def problem_3_find_second_max():
    # TODO: Find the second largest distinct element in an array.
    pass

    # --- SOLUTION ---
    # def second_max(arr):
    #     first = second = float('-inf')
    #     for n in arr:
    #         if n > first:
    #             second = first
    #             first = n
    #         elif n > second and n != first:
    #             second = n
    #     return second


def problem_4_find_second_min():
    # TODO: Find the second smallest distinct element in an array.
    pass

    # --- SOLUTION ---
    # def second_min(arr):
    #     first = second = float('inf')
    #     for n in arr:
    #         if n < first:
    #             second = first
    #             first = n
    #         elif n < second and n != first:
    #             second = n
    #     return second


def problem_5_print_even_indices():
    # TODO: Print elements located at even indices (0, 2, 4...).
    pass

    # --- SOLUTION ---
    # def even_indices(arr):
    #     for i in range(0, len(arr), 2):
    #         print(arr[i])


def problem_6_print_odd_indices():
    # TODO: Print elements located at odd indices (1, 3, 5...).
    pass

    # --- SOLUTION ---
    # def odd_indices(arr):
    #     for i in range(1, len(arr), 2):
    #         print(arr[i])


def problem_7_find_even_index_max():
    # TODO: Find the maximum value among elements at EVEN indices.
    pass

    # --- SOLUTION ---
    # def even_index_max(arr):
    #     if not arr: return None
    #     maximum = arr[0]
    #     for i in range(0, len(arr), 2):
    #         if arr[i] > maximum: maximum = arr[i]
    #     return maximum


def problem_8_find_odd_index_max():
    # TODO: Find the maximum value among elements at ODD indices.
    pass

    # --- SOLUTION ---
    # def odd_index_max(arr):
    #     if len(arr) < 2: return None
    #     maximum = arr[1]
    #     for i in range(1, len(arr), 2):
    #         if arr[i] > maximum: maximum = arr[i]
    #     return maximum


def problem_9_print_square_indices():
    # TODO: Print elements at indices that are perfect squares (0, 1, 4, 9...).
    pass

    # --- SOLUTION ---
    # def square_indices(arr):
    #     i = 0
    #     while i * i < len(arr):
    #         print(arr[i * i])
    #         i += 1


def problem_10_print_cube_indices():
    # TODO: Print elements at indices that are perfect cubes (0, 1, 8, 27...).
    pass

    # --- SOLUTION ---
    # def cube_indices(arr):
    #     i = 0
    #     while i * i * i < len(arr):
    #         print(arr[i * i * i])
    #         i += 1


def problem_11_check_sorted():
    # TODO: Write a function to check if an array is sorted in ascending order.
    pass

    # --- SOLUTION ---
    # def is_sorted(arr):
    #     for i in range(1, len(arr)):
    #         if arr[i] < arr[i - 1]: return False
    #     return True


def problem_12_bubble_sort_one_pass():
    # TODO: Perform just ONE pass of bubble sort. What does the array look like?
    pass

    # --- SOLUTION ---
    # def bubble_one_pass(arr):
    #     for j in range(len(arr) - 1):
    #         if arr[j] > arr[j + 1]:
    #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #     return arr


def problem_13_bubble_sort_full():
    # TODO: Implement the full Bubble Sort algorithm.
    pass

    # --- SOLUTION ---
    # def bubble_sort(arr):
    #     n = len(arr)
    #     for i in range(n):
    #         swapped = False
    #         for j in range(0, n - i - 1):
    #             if arr[j] > arr[j + 1]:
    #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
    #                 swapped = True
    #         if not swapped: break


def problem_14_selection_sort_find_min_idx():
    # TODO: Find the INDEX of the minimum element in the sub-array arr[start:].
    pass

    # --- SOLUTION ---
    # def find_min_idx(arr, start):
    #     min_idx = start
    #     for i in range(start + 1, len(arr)):
    #         if arr[i] < arr[min_idx]:
    #             min_idx = i
    #     return min_idx


def problem_15_selection_sort_full():
    # TODO: Implement the full Selection Sort algorithm.
    pass

    # --- SOLUTION ---
    # def selection_sort(arr):
    #     n = len(arr)
    #     for i in range(n):
    #         min_idx = i
    #         for j in range(i + 1, n):
    #             if arr[j] < arr[min_idx]:
    #                 min_idx = j
    #         arr[i], arr[min_idx] = arr[min_idx], arr[i]


def problem_16_insertion_sort_shift():
    # TODO: Given a sorted array and a new key, shift elements right to make room for the key.
    pass

    # --- SOLUTION ---
    # def shift_for_key(arr, key):
    #     arr.append(0) # Make room
    #     j = len(arr) - 2
    #     while j >= 0 and key < arr[j]:
    #         arr[j + 1] = arr[j]
    #         j -= 1
    #     arr[j + 1] = key
    #     return arr


def problem_17_insertion_sort_full():
    # TODO: Implement the full Insertion Sort algorithm.
    pass

    # --- SOLUTION ---
    # def insertion_sort(arr):
    #     for i in range(1, len(arr)):
    #         key = arr[i]
    #         j = i - 1
    #         while j >= 0 and key < arr[j]:
    #             arr[j + 1] = arr[j]
    #             j -= 1
    #         arr[j + 1] = key


def problem_18_sort_descending():
    # TODO: Modify Bubble Sort to sort in DESCENDING order.
    pass

    # --- SOLUTION ---
    # def bubble_sort_desc(arr):
    #     n = len(arr)
    #     for i in range(n):
    #         for j in range(0, n - i - 1):
    #             if arr[j] < arr[j + 1]: # Flipped the sign!
    #                 arr[j], arr[j + 1] = arr[j + 1], arr[j]


def problem_19_find_3_max():
    # TODO: Find the 3 largest elements in an array. (Hint: Sorting is easiest).
    pass

    # --- SOLUTION ---
    # def top_3(arr):
    #     if len(arr) < 3: return None
    #     # Sort descending and slice
    #     return sorted(arr, reverse=True)[:3]


def problem_20_in_place_swap():
    # TODO: Swap elements at index `i` and `j` in an array in-place.
    pass

    # --- SOLUTION ---
    # def swap(arr, i, j):
    #     arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    print("Welcome to Day 7 Practice Problems!")

# ==================================================
# --- Day6 : Day6_Practice_Problems.py ---
# ==================================================

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

# ==================================================
# --- Day5 : Day5_Practice_Problems.py ---
# ==================================================

# Day 5 Practice Problems: List Methods and Problem Solving
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_list_append():
    # TODO: Create an empty list 'nums'. Append 10, then append 20. Print the list.
    pass

    # --- SOLUTION ---
    # nums = []
    # nums.append(10)
    # nums.append(20)
    # print(nums)


def problem_2_list_extend():
    # TODO: You have lst1 = [1, 2] and lst2 = [3, 4]. Use .extend() to add lst2 to lst1.
    pass

    # --- SOLUTION ---
    # lst1 = [1, 2]
    # lst2 = [3, 4]
    # lst1.extend(lst2)
    # print(lst1)


def problem_3_list_insert():
    # TODO: You have fruits = ["apple", "cherry"]. Insert "banana" at index 1.
    pass

    # --- SOLUTION ---
    # fruits = ["apple", "cherry"]
    # fruits.insert(1, "banana")
    # print(fruits)


def problem_4_list_remove():
    # TODO: You have items = [1, 5, 1, 9]. Remove the FIRST occurrence of 1 using .remove().
    pass

    # --- SOLUTION ---
    # items = [1, 5, 1, 9]
    # items.remove(1)
    # print(items)


def problem_5_list_pop():
    # TODO: You have nums = [10, 20, 30]. Use .pop() to remove and print the last element.
    pass

    # --- SOLUTION ---
    # nums = [10, 20, 30]
    # last = nums.pop()
    # print(last, nums)


def problem_6_list_index():
    # TODO: Find the index of "cat" in animals = ["dog", "cat", "bird"].
    pass

    # --- SOLUTION ---
    # animals = ["dog", "cat", "bird"]
    # print(animals.index("cat"))


def problem_7_list_count():
    # TODO: Count how many times 5 appears in [5, 2, 5, 5, 1].
    pass

    # --- SOLUTION ---
    # nums = [5, 2, 5, 5, 1]
    # print(nums.count(5))


def problem_8_list_sort():
    # TODO: Sort the list [4, 1, 8, 3] in ascending order in-place.
    pass

    # --- SOLUTION ---
    # nums = [4, 1, 8, 3]
    # nums.sort()
    # print(nums)


def problem_9_list_reverse():
    # TODO: Reverse the list [1, 2, 3] in-place using .reverse().
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # nums.reverse()
    # print(nums)


def problem_10_map_input():
    # TODO: Assume user types "1 2 3". Write code to parse this into a list of integers [1, 2, 3].
    pass

    # --- SOLUTION ---
    # # raw = input()
    # raw = "1 2 3" # Simulated input
    # nums = list(map(int, raw.split()))
    # print(nums)


def problem_11_sum_list():
    # TODO: Write a loop to calculate the sum of [10, 20, 30] without using the built-in sum().
    pass

    # --- SOLUTION ---
    # nums = [10, 20, 30]
    # total = 0
    # for n in nums: total += n
    # print(total)


def problem_12_product_list():
    # TODO: Write a loop to calculate the product (multiplication) of [2, 3, 4].
    pass

    # --- SOLUTION ---
    # nums = [2, 3, 4]
    # prod = 1
    # for n in nums: prod *= n
    # print(prod)


def problem_13_sum_of_squares():
    # TODO: Calculate the sum of the squares of [1, 2, 3] -> (1^2 + 2^2 + 3^2)
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # total = 0
    # for n in nums: total += (n ** 2)
    # print(total)


def problem_14_frequency_count():
    # TODO: Write a loop to create a frequency dictionary for [1, 1, 2, 3, 3, 3].
    pass

    # --- SOLUTION ---
    # nums = [1, 1, 2, 3, 3, 3]
    # freq = {}
    # for n in nums:
    #     freq[n] = freq.get(n, 0) + 1
    # print(freq)


def problem_15_all_pairs():
    # TODO: Print all unique pairs from [1, 2, 3] using nested loops.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         print((nums[i], nums[j]))


def problem_16_list_clear():
    # TODO: You have lst = [1, 2, 3]. Empty it completely using a list method.
    pass

    # --- SOLUTION ---
    # lst = [1, 2, 3]
    # lst.clear()
    # print(lst)


def problem_17_min_max_loops():
    # TODO: Find the maximum value in [4, 9, 2, 7] using a loop, not the max() function.
    pass

    # --- SOLUTION ---
    # nums = [4, 9, 2, 7]
    # current_max = nums[0]
    # for n in nums:
    #     if n > current_max: current_max = n
    # print(current_max)


def problem_18_copy_list():
    # TODO: Create a shallow copy of lst1 = [1, 2, 3] into lst2. Append 4 to lst2. lst1 should NOT change.
    pass

    # --- SOLUTION ---
    # lst1 = [1, 2, 3]
    # lst2 = lst1.copy() # or lst1[:]
    # lst2.append(4)
    # print(lst1, lst2)


def problem_19_filter_evens():
    # TODO: Given nums = [1, 2, 3, 4, 5, 6], create a new list containing only the even numbers.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3, 4, 5, 6]
    # evens = []
    # for n in nums:
    #     if n % 2 == 0: evens.append(n)
    # print(evens)


def problem_20_list_membership():
    # TODO: Check if 10 is inside the list [5, 10, 15] and print True or False.
    pass

    # --- SOLUTION ---
    # nums = [5, 10, 15]
    # print(10 in nums)


if __name__ == "__main__":
    print("Welcome to Day 5 Practice Problems!")
    # problem_1_list_append()

# ==================================================
# --- Day4 : Day4_Practice_Problems.py ---
# ==================================================

# Day 4 Practice Problems: String Methods, Anagrams, and Recursion
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_string_lower():
    # TODO: Convert the string "PyThOn" to fully lowercase.
    pass

    # --- SOLUTION ---
    # text = "PyThOn"
    # print(text.lower())


def problem_2_string_upper():
    # TODO: Convert the string "hello" to fully uppercase.
    pass

    # --- SOLUTION ---
    # text = "hello"
    # print(text.upper())


def problem_3_string_strip():
    # TODO: Remove the extra spaces from "   data   ".
    pass

    # --- SOLUTION ---
    # text = "   data   "
    # print(text.strip())


def problem_4_string_replace():
    # TODO: Replace "bad" with "good" in "This is a bad idea".
    pass

    # --- SOLUTION ---
    # text = "This is a bad idea"
    # print(text.replace("bad", "good"))


def problem_5_string_split():
    # TODO: Split "apple,banana,cherry" into a list using the comma as a delimiter.
    pass

    # --- SOLUTION ---
    # text = "apple,banana,cherry"
    # print(text.split(","))


def problem_6_string_join():
    # TODO: Join the list ["A", "B", "C"] into a single string separated by dashes ("-").
    pass

    # --- SOLUTION ---
    # items = ["A", "B", "C"]
    # print("-".join(items))


def problem_7_string_find():
    # TODO: Find the index of the word "fox" in "The quick brown fox".
    pass

    # --- SOLUTION ---
    # text = "The quick brown fox"
    # print(text.find("fox"))


def problem_8_string_count():
    # TODO: Count how many times the letter "p" appears in "apple".
    pass

    # --- SOLUTION ---
    # text = "apple"
    # print(text.count("p"))


def problem_9_is_digit():
    # TODO: Check if the string "12345" consists only of digits using .isdigit().
    pass

    # --- SOLUTION ---
    # text = "12345"
    # print(text.isdigit())


def problem_10_anagram_sorting():
    # TODO: Write a function that takes two strings and returns True if they are anagrams using sorted().
    pass

    # --- SOLUTION ---
    # def is_anagram(s1, s2):
    #     return sorted(s1) == sorted(s2)
    # print(is_anagram("listen", "silent"))


def problem_11_anagram_frequency():
    # TODO: Write an anagram checker using a dictionary to count frequencies instead of sorting.
    pass

    # --- SOLUTION ---
    # def is_anagram_freq(s1, s2):
    #     if len(s1) != len(s2): return False
    #     counts = {}
    #     for char in s1:
    #         counts[char] = counts.get(char, 0) + 1
    #     for char in s2:
    #         if counts.get(char, 0) == 0: return False
    #         counts[char] -= 1
    #     return True


def problem_12_basic_recursion():
    # TODO: Write a recursive function 'print_down(n)' that prints from n down to 1.
    pass

    # --- SOLUTION ---
    # def print_down(n):
    #     if n <= 0: return
    #     print(n)
    #     print_down(n - 1)
    # print_down(3)


def problem_13_recursive_sum():
    # TODO: Write a recursive function to find the sum of numbers from 1 to n.
    pass

    # --- SOLUTION ---
    # def recursive_sum(n):
    #     if n <= 1: return 1
    #     return n + recursive_sum(n - 1)


def problem_14_recursive_factorial():
    # TODO: Write a recursive function to find the factorial of n (n!).
    pass

    # --- SOLUTION ---
    # def factorial(n):
    #     if n == 1: return 1
    #     return n * factorial(n - 1)


def problem_15_recursive_fibonacci():
    # TODO: Write a recursive function to find the nth Fibonacci number. (fib(0)=0, fib(1)=1)
    pass

    # --- SOLUTION ---
    # def fibonacci(n):
    #     if n <= 1: return n
    #     return fibonacci(n - 1) + fibonacci(n - 2)


def problem_16_recursive_power():
    # TODO: Write a recursive function to calculate base^exp (e.g., power(2, 3) = 8).
    pass

    # --- SOLUTION ---
    # def power(base, exp):
    #     if exp == 0: return 1
    #     return base * power(base, exp - 1)


def problem_17_palindrome_checker():
    # TODO: Write a function to check if a string is a palindrome. Use string methods to clean it first.
    pass

    # --- SOLUTION ---
    # def is_palindrome(s):
    #     cleaned = s.replace(" ", "").lower()
    #     return cleaned == cleaned[::-1]


def problem_18_vowel_counter():
    # TODO: Write a function that counts how many vowels are in a string using a loop and string methods.
    pass

    # --- SOLUTION ---
    # def count_vowels(s):
    #     count = 0
    #     for char in s.lower():
    #         if char in "aeiou": count += 1
    #     return count


def problem_19_title_case():
    # TODO: Convert "python is fun" to "Python Is Fun" using .title().
    pass

    # --- SOLUTION ---
    # text = "python is fun"
    # print(text.title())


def problem_20_starts_with():
    # TODO: Check if "Data Science" starts with "Data" using .startswith().
    pass

    # --- SOLUTION ---
    # text = "Data Science"
    # print(text.startswith("Data"))


if __name__ == "__main__":
    print("Welcome to Day 4 Practice Problems!")
    # problem_1_string_lower()

# ==================================================
# --- Day3 : Day3_Practice_Problems.py ---
# ==================================================

# Day 3 Practice Problems: Strings, Lists, and Functions
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_string_indexing():
    # TODO: Create a string 'word' = "Developer".
    # TODO: Print the first and last characters using positive and negative indexing.
    pass

    # --- SOLUTION ---
    # word = "Developer"
    # print(word[0], word[-1])


def problem_2_list_indexing():
    # TODO: Create a list 'nums' = [10, 20, 30, 40, 50].
    # TODO: Print the third item (30) using indexing.
    pass

    # --- SOLUTION ---
    # nums = [10, 20, 30, 40, 50]
    # print(nums[2])


def problem_3_string_slicing():
    # TODO: You have text = "PythonProgramming".
    # TODO: Extract and print the word "Python" using slicing.
    pass

    # --- SOLUTION ---
    # text = "PythonProgramming"
    # print(text[0:6])


def problem_4_list_slicing():
    # TODO: You have items = ["apple", "banana", "cherry", "date", "elderberry"].
    # TODO: Extract and print ["banana", "cherry", "date"] using slicing.
    pass

    # --- SOLUTION ---
    # items = ["apple", "banana", "cherry", "date", "elderberry"]
    # print(items[1:4])


def problem_5_slicing_steps():
    # TODO: You have numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
    # TODO: Use slicing with a step to print all odd numbers: [1, 3, 5, 7, 9].
    pass

    # --- SOLUTION ---
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(numbers[1::2])


def problem_6_reverse_string():
    # TODO: Use negative step slicing to print the reverse of "hello".
    pass

    # --- SOLUTION ---
    # word = "hello"
    # print(word[::-1])


def problem_7_basic_function():
    # TODO: Define a function 'say_hello' that takes no parameters and prints "Hello, World!".
    # TODO: Call the function.
    pass

    # --- SOLUTION ---
    # def say_hello():
    #     print("Hello, World!")
    # say_hello()


def problem_8_function_with_parameters():
    # TODO: Define a function 'multiply' that takes two parameters 'a' and 'b'.
    # TODO: It should return the product of a and b. Call it with 5 and 4 and print the result.
    pass

    # --- SOLUTION ---
    # def multiply(a, b):
    #     return a * b
    # print(multiply(5, 4))


def problem_9_default_arguments():
    # TODO: Define a function 'greet' with parameter 'name' and 'msg' which defaults to "Welcome".
    # TODO: Print f"{msg}, {name}!". Call it once with only a name, and once with both.
    pass

    # --- SOLUTION ---
    # def greet(name, msg="Welcome"):
    #     print(f"{msg}, {name}!")
    # greet("Alice")
    # greet("Bob", "Good morning")


def problem_10_args():
    # TODO: Define a function 'sum_all' that takes *args.
    # TODO: Use the built-in sum() function to return the sum of all passed numbers.
    # TODO: Print sum_all(1, 2, 3, 4, 5).
    pass

    # --- SOLUTION ---
    # def sum_all(*args):
    #     return sum(args)
    # print(sum_all(1, 2, 3, 4, 5))


def problem_11_kwargs():
    # TODO: Define a function 'print_info' that takes **kwargs.
    # TODO: Iterate through kwargs.items() and print the key and value.
    # TODO: Call it with name="John", age=30.
    pass

    # --- SOLUTION ---
    # def print_info(**kwargs):
    #     for key, value in kwargs.items():
    #         print(f"{key}: {value}")
    # print_info(name="John", age=30)


def problem_12_global_scope():
    # TODO: Create a global variable 'counter' = 0.
    # TODO: Define a function that uses the 'global' keyword to increment 'counter' by 1.
    pass

    # --- SOLUTION ---
    # counter = 0
    # def increment():
    #     global counter
    #     counter += 1
    # increment()


def problem_13_list_concatenation():
    # TODO: You have list1 = [1, 2] and list2 = [3, 4].
    # TODO: Combine them into list3 without using the append method (use +).
    pass

    # --- SOLUTION ---
    # list1 = [1, 2]
    # list2 = [3, 4]
    # list3 = list1 + list2
    # print(list3)


def problem_14_string_repetition():
    # TODO: Use the '*' operator to print "Ha" 5 times consecutively.
    pass

    # --- SOLUTION ---
    # print("Ha" * 5)


def problem_15_function_calling_function():
    # TODO: Define 'square(x)' that returns x*x.
    # TODO: Define 'sum_of_squares(x, y)' that returns square(x) + square(y).
    pass

    # --- SOLUTION ---
    # def square(x):
    #     return x * x
    # def sum_of_squares(x, y):
    #     return square(x) + square(y)
    # print(sum_of_squares(3, 4))


def problem_16_return_vs_print():
    # TODO: Define 'add_print(a, b)' that prints a+b but returns None.
    # TODO: Define 'add_return(a, b)' that returns a+b.
    # Note the difference when you try to assign their results to a variable!
    pass

    # --- SOLUTION ---
    # def add_print(a, b):
    #     print(a + b)
    # def add_return(a, b):
    #     return a + b
    # res1 = add_print(2, 2)   # res1 is None
    # res2 = add_return(2, 2)  # res2 is 4


def problem_17_recursive_countdown():
    # TODO: Define a recursive function 'countdown(n)'.
    # TODO: Base case: if n <= 0, print "Blastoff!".
    # TODO: Recursive step: print n, then call countdown(n - 1).
    pass

    # --- SOLUTION ---
    # def countdown(n):
    #     if n <= 0:
    #         print("Blastoff!")
    #     else:
    #         print(n)
    #         countdown(n - 1)
    # countdown(3)


def problem_18_string_immutability():
    # TODO: Strings are immutable. Try to change text = "Cat" to "Bat" using indexing (text[0] = "B").
    # Watch it throw a TypeError. Then do it the right way using string concatenation or slicing.
    pass

    # --- SOLUTION ---
    # text = "Cat"
    # # text[0] = "B"  # Throws TypeError
    # text = "B" + text[1:]
    # print(text)


def problem_19_list_mutability():
    # TODO: Lists ARE mutable. Create nums = [1, 2, 3].
    # TODO: Change the first element to 99 using indexing. Print nums.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # nums[0] = 99
    # print(nums)


def problem_20_slice_assignment():
    # TODO: You have nums = [1, 2, 3, 4, 5].
    # TODO: Replace the sublist [2, 3] with [8, 9] using slice assignment.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3, 4, 5]
    # nums[1:3] = [8, 9]
    # print(nums)


if __name__ == "__main__":
    print("Welcome to Day 3 Practice Problems!")
    # problem_1_string_indexing()

# ==================================================
# --- Day2 : Day2_Practice_Problems.py ---
# ==================================================

# Day 2 Practice Problems: Control Flow (Conditionals & Loops)
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_if():
    # TODO: Create a variable 'temperature' = 35.
    # TODO: Write an if statement that prints "It's a hot day!" if temperature is greater than 30.
    pass

    # --- SOLUTION ---
    # temperature = 35
    # if temperature > 30:
    #     print("It's a hot day!")


def problem_2_if_else():
    # TODO: Create a variable 'is_raining' = True.
    # TODO: If it's raining, print "Take an umbrella", else print "Enjoy the sun".
    pass

    # --- SOLUTION ---
    # is_raining = True
    # if is_raining:
    #     print("Take an umbrella")
    # else:
    #     print("Enjoy the sun")


def problem_3_elif():
    # TODO: Create a variable 'score' = 85.
    # TODO: if score >= 90 print "A", elif score >= 80 print "B", else print "C".
    pass

    # --- SOLUTION ---
    # score = 85
    # if score >= 90:
    #     print("A")
    # elif score >= 80:
    #     print("B")
    # else:
    #     print("C")


def problem_4_nested_if():
    # TODO: Create variables 'is_weekend' = True and 'has_money' = False.
    # TODO: If it's the weekend, check if you have money. If yes, print "Go to movies", else print "Stay home".
    # If not the weekend, print "Go to work".
    pass

    # --- SOLUTION ---
    # is_weekend = True
    # has_money = False
    # if is_weekend:
    #     if has_money:
    #         print("Go to movies")
    #     else:
    #         print("Stay home")
    # else:
    #     print("Go to work")


def problem_5_multiple_conditions():
    # TODO: Create 'age' = 25 and 'has_license' = True.
    # TODO: Print "Can drive" ONLY IF age is >= 18 AND has_license is True.
    pass

    # --- SOLUTION ---
    # age = 25
    # has_license = True
    # if age >= 18 and has_license:
    #     print("Can drive")


def problem_6_for_loop_range():
    # TODO: Use a for loop and range() to print numbers from 1 to 5 (inclusive).
    pass

    # --- SOLUTION ---
    # for i in range(1, 6):
    #     print(i)


def problem_7_for_loop_list():
    # TODO: Create a list 'fruits' = ["apple", "banana", "cherry"].
    # TODO: Use a for loop to print each fruit.
    pass

    # --- SOLUTION ---
    # fruits = ["apple", "banana", "cherry"]
    # for fruit in fruits:
    #     print(fruit)


def problem_8_for_loop_string():
    # TODO: Use a for loop to iterate over the string "Python" and print each letter on a new line.
    pass

    # --- SOLUTION ---
    # for letter in "Python":
    #     print(letter)


def problem_9_while_loop():
    # TODO: Create a variable 'count' = 3.
    # TODO: Use a while loop to print 'count' and decrement it by 1 as long as it is > 0.
    pass

    # --- SOLUTION ---
    # count = 3
    # while count > 0:
    #     print(count)
    #     count -= 1


def problem_10_break_statement():
    # TODO: Loop from 1 to 10 using for i in range(1, 11).
    # TODO: If i equals 5, break out of the loop immediately. Print 'i' in each iteration.
    pass

    # --- SOLUTION ---
    # for i in range(1, 11):
    #     if i == 5:
    #         break
    #     print(i)


def problem_11_continue_statement():
    # TODO: Loop from 1 to 5.
    # TODO: If the number is 3, use 'continue' to skip printing it. Print all other numbers.
    pass

    # --- SOLUTION ---
    # for i in range(1, 6):
    #     if i == 3:
    #         continue
    #     print(i)


def problem_12_nested_loops():
    # TODO: Create two lists: colors = ["red", "blue"] and items = ["car", "bike"].
    # TODO: Use a nested loop to print every combination (e.g., "red car").
    pass

    # --- SOLUTION ---
    # colors = ["red", "blue"]
    # items = ["car", "bike"]
    # for color in colors:
    #     for item in items:
    #         print(color, item)


def problem_13_sum_with_loop():
    # TODO: Create a variable 'total' = 0.
    # TODO: Use a for loop to add all numbers from 1 to 10 to 'total'. Print the final 'total'.
    pass

    # --- SOLUTION ---
    # total = 0
    # for i in range(1, 11):
    #     total += i
    # print(total)


def problem_14_even_numbers_range():
    # TODO: Use a for loop with a step size in range() to print all even numbers from 2 to 10.
    pass

    # --- SOLUTION ---
    # for i in range(2, 11, 2):
    #     print(i)


def problem_15_while_true():
    # TODO: Use a 'while True:' loop and a variable 'x' starting at 1.
    # TODO: Break out of the loop when 'x' reaches 4. Print 'x' and increment it each time.
    pass

    # --- SOLUTION ---
    # x = 1
    # while True:
    #     print(x)
    #     if x == 4:
    #         break
    #     x += 1


def problem_16_pattern_square():
    # TODO: Use a nested loop to print a 3x3 square of asterisks (*).
    pass

    # --- SOLUTION ---
    # for i in range(3):
    #     for j in range(3):
    #         print("*", end=" ")
    #     print()


def problem_17_pattern_triangle():
    # TODO: Use a loop to print a right-angle triangle of asterisks with 4 rows.
    # Row 1: 1 star. Row 4: 4 stars.
    pass

    # --- SOLUTION ---
    # for i in range(1, 5):
    #     print("*" * i)


def problem_18_loop_else():
    # TODO: Loop from 1 to 3. 
    # TODO: Add an 'else' block to the 'for' loop that prints "Loop finished without breaking".
    pass

    # --- SOLUTION ---
    # for i in range(1, 4):
    #     print(i)
    # else:
    #     print("Loop finished without breaking")


def problem_19_list_filtering():
    # TODO: You have nums = [1, 5, 8, 10, 15].
    # TODO: Use a for loop and an if statement to print ONLY numbers greater than 9.
    pass

    # --- SOLUTION ---
    # nums = [1, 5, 8, 10, 15]
    # for n in nums:
    #     if n > 9:
    #         print(n)


def problem_20_counting_vowels():
    # TODO: You have a string 'word' = "education".
    # TODO: Use a for loop to count how many vowels (a,e,i,o,u) are in the word. Print the final count.
    pass

    # --- SOLUTION ---
    # word = "education"
    # count = 0
    # for char in word:
    #     if char in "aeiou":
    #         count += 1
    # print(count)


if __name__ == "__main__":
    print("Welcome to Day 2 Practice Problems!")
    print("Fill in the code for each function and call them here to test your answers.")
    # problem_1_if()

# ==================================================
# --- Day1 : fix_me_day1.py ---
# ==================================================

# Debugging Exercise: Day 1
# This file contains several intentional errors. 
# Your task is to find them, fix them, and make the script run successfully!

print("Welcome to the Day 1 Debugging Challenge!)

# 1. Variable Assignment Errors
1st_name = "Alice"
last-name = "Smith"
print(f"User: {1st_name} {last-name}")

# 2. Data Type Errors
age = 25
message = "I am " + age + " years old."
print(message)

# 3. List Errors
favorite_colors = ["Red", "Blue", "Green"
print(favorite_colors)

# 4. Math and Operator Errors
# We want to calculate the average of 3 test scores
score1 = 80
score2 = 90
score3 = 100
average_score = score1 + score2 + score3 / 3
print(f"The average score is: {average_score}")

# 5. Logic error
# Check if the user is an adult
is_adult = Age >= 18
print("Is adult?", is_adult)

print("If you see this, you fixed all the errors! Great job!")


# ==================================================
# --- Day1 : Day1_Practice_Problems.py ---
# ==================================================

# Day 1 Practice Problems: Python Fundamentals, Variables, Data Types & Operators
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_basics():
    # TODO: Print "Hello, Python!" to the console
    pass

    # --- SOLUTION ---
    # print("Hello, Python!")


def problem_2_variables():
    # TODO: Create a variable called 'user_age' and set it to 25.
    # TODO: Create a variable called 'user_name' and set it to "Alice".
    # TODO: Print a message saying "Alice is 25 years old."
    pass

    # --- SOLUTION ---
    # user_age = 25
    # user_name = "Alice"
    # print(user_name, "is", user_age, "years old.")


def problem_3_datatypes():
    # TODO: Create a variable 'price' with the value 19.99
    # TODO: Use the built-in type() function to print the data type of 'price'
    pass

    # --- SOLUTION ---
    # price = 19.99
    # print(type(price))


def problem_4_type_casting():
    # TODO: You have a string variable: str_num = "50"
    # TODO: Convert it into an integer, add 10 to it, and print the result.
    str_num = "50"
    pass

    # --- SOLUTION ---
    # num = int(str_num)
    # result = num + 10
    # print(result)


def problem_5_arithmetic():
    # TODO: Calculate the total bill for 3 coffees.
    # Each coffee is $4.50. The tax is a flat $1.50.
    # Store the result in 'total_bill' and print it.
    pass

    # --- SOLUTION ---
    # coffee_price = 4.50
    # num_coffees = 3
    # tax = 1.50
    # total_bill = (coffee_price * num_coffees) + tax
    # print(total_bill)


def problem_6_modulo():
    # TODO: Create a variable 'number' and set it to 15.
    # TODO: Use the modulo operator (%) to find the remainder when 'number' is divided by 2.
    # Print the remainder.
    pass

    # --- SOLUTION ---
    # number = 15
    # remainder = number % 2
    # print(remainder)


def problem_7_lists():
    # TODO: Create a list named 'fruits' containing "apple", "banana", and "cherry".
    # TODO: Print the second item in the list ("banana").
    pass

    # --- SOLUTION ---
    # fruits = ["apple", "banana", "cherry"]
    # print(fruits[1])


def problem_8_dictionaries():
    # TODO: Create a dictionary named 'student' with keys "name" and "grade".
    # Set "name" to "John" and "grade" to "A".
    # TODO: Print the student's grade.
    pass

    # --- SOLUTION ---
    # student = {"name": "John", "grade": "A"}
    # print(student["grade"])


def problem_9_comparison():
    # TODO: You have a saved password "secret123" and an input password "secret123".
    # TODO: Create a variable 'is_match' that uses the equality operator (==) to compare them.
    # Print 'is_match'.
    saved_pwd = "secret123"
    input_pwd = "secret123"
    pass

    # --- SOLUTION ---
    # is_match = (saved_pwd == input_pwd)
    # print(is_match)


def problem_10_logical():
    # TODO: To get a discount, a customer must be a member (is_member = True)
    # AND must have spent over $50 (spent = 60).
    # TODO: Create a boolean variable 'gets_discount' using logical operators and print it.
    is_member = True
    spent = 60
    pass

    # --- SOLUTION ---
    # gets_discount = is_member and (spent > 50)
    # print(gets_discount)

def problem_11_string_formatting():
    # TODO: Use an f-string to print "My favorite language is Python." 
    # Use the variable provided below inside the f-string.
    language = "Python"
    pass

    # --- SOLUTION ---
    # print(f"My favorite language is {language}.")


def problem_12_string_methods():
    # TODO: Convert the string 'shout' to uppercase using a string method and print it.
    shout = "hello"
    pass

    # --- SOLUTION ---
    # print(shout.upper())


def problem_13_length():
    # TODO: Use a built-in function to print the number of characters in the word "Supercalifragilisticexpialidocious".
    word = "Supercalifragilisticexpialidocious"
    pass

    # --- SOLUTION ---
    # print(len(word))


def problem_14_tuples():
    # TODO: Create a tuple named 'coordinates' containing the numbers 10 and 20.
    # TODO: Try to assign the value 30 to the first element (index 0). Watch it fail! (Tuples are immutable)
    pass

    # --- SOLUTION ---
    # coordinates = (10, 20)
    # # coordinates[0] = 30 # This will raise a TypeError!


def problem_15_sets():
    # TODO: Create a set named 'unique_numbers' with the values: 1, 1, 2, 3, 3, 4.
    # Print the set. Notice how duplicates are automatically removed!
    pass

    # --- SOLUTION ---
    # unique_numbers = {1, 1, 2, 3, 3, 4}
    # print(unique_numbers)


def problem_16_swap():
    # TODO: Swap the values of 'a' and 'b' without using a third temporary variable.
    # Print 'a' and 'b' to verify they swapped.
    a = 100
    b = 200
    pass

    # --- SOLUTION ---
    # a, b = b, a
    # print(a, b)


def problem_17_assignment_operator():
    # TODO: Use the '+=' assignment operator to add 50 to 'score'. Print 'score'.
    score = 10
    pass

    # --- SOLUTION ---
    # score += 50
    # print(score)


def problem_18_membership_operator():
    # TODO: Check if the letter "z" is in the string "alphabet" using the 'in' operator.
    # Print the boolean result.
    word = "alphabet"
    pass

    # --- SOLUTION ---
    # print("z" in word)


def problem_19_identity_operator():
    # TODO: Create two variables: list1 = [1, 2] and list2 = [1, 2].
    # TODO: Use the 'is' operator to check if they are the exact same object in memory. Print the result.
    pass

    # --- SOLUTION ---
    # list1 = [1, 2]
    # list2 = [1, 2]
    # print(list1 is list2) # Returns False because they are two distinct lists in memory!


def problem_20_precedence():
    # TODO: Calculate the result of 10 + 5 * 2. 
    # TODO: Now use parentheses to force the addition to happen first. Print both results.
    pass

    # --- SOLUTION ---
    # print(10 + 5 * 2)       # Output: 20
    # print((10 + 5) * 2)     # Output: 30

def problem_21_string_slicing():
    # TODO: Create a variable 'text' = "Python Programming".
    # TODO: Slice the string to extract just the word "Python" and print it.
    pass

    # --- SOLUTION ---
    # text = "Python Programming"
    # print(text[0:6])


def problem_22_dict_keys():
    # TODO: You have a dictionary: car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # TODO: Print only the keys of the dictionary.
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    pass

    # --- SOLUTION ---
    # print(car.keys())


def problem_23_dict_values():
    # TODO: Using the same 'car' dictionary, print only the values.
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    pass

    # --- SOLUTION ---
    # print(car.values())


def problem_24_list_append():
    # TODO: Create a list 'colors' = ["red", "green"].
    # TODO: Add "blue" to the end of the list and print the list.
    pass

    # --- SOLUTION ---
    # colors = ["red", "green"]
    # colors.append("blue")
    # print(colors)


def problem_25_type_error():
    # TODO: Try to concatenate a string "Age: " and an integer 25 using the '+' operator.
    # TODO: Watch it fail! Fix it by converting the integer to a string first, then print it.
    pass

    # --- SOLUTION ---
    # # print("Age: " + 25) # This raises a TypeError!
    # print("Age: " + str(25))


def problem_26_boolean_math():
    # TODO: In Python, True is 1 and False is 0. 
    # TODO: Print the result of True + True.
    pass

    # --- SOLUTION ---
    # print(True + True) # Outputs 2


def problem_27_floor_division():
    # TODO: Calculate 10 divided by 3 using standard division (/) and print it.
    # TODO: Calculate 10 divided by 3 using floor division (//) and print it. Notice the difference!
    pass

    # --- SOLUTION ---
    # print(10 / 3)   # Outputs 3.3333333333333335
    # print(10 // 3)  # Outputs 3


def problem_28_exponentiation():
    # TODO: Calculate 2 to the power of 5 using the exponentiation operator (**) and print it.
    pass

    # --- SOLUTION ---
    # print(2 ** 5)   # Outputs 32


def problem_29_dynamic_typing():
    # TODO: Create a variable 'x' and assign it the integer 100.
    # TODO: Reassign 'x' to the string "Now I'm a string!" and print 'x'. This demonstrates dynamic typing.
    pass

    # --- SOLUTION ---
    # x = 100
    # x = "Now I'm a string!"
    # print(x)


def problem_30_string_repetition():
    # TODO: Use the multiplication operator (*) to print a string of 20 dashes ("-").
    pass

    # --- SOLUTION ---
    # print("-" * 20)

def problem_31_negative_indexing():
    # TODO: Create a list 'letters' = ["a", "b", "c", "d", "e"].
    # TODO: Use negative indexing to print the last element ("e") of the list.
    pass

    # --- SOLUTION ---
    # letters = ["a", "b", "c", "d", "e"]
    # print(letters[-1])


def problem_32_list_membership():
    # TODO: Create a list 'vowels' = ["a", "e", "i", "o", "u"].
    # TODO: Check if the letter "x" is in the 'vowels' list using 'in' and print the boolean result.
    pass

    # --- SOLUTION ---
    # vowels = ["a", "e", "i", "o", "u"]
    # print("x" in vowels)


def problem_33_delete_variable():
    # TODO: Create a variable 'temp_data' = 500.
    # TODO: Delete the variable using the 'del' keyword. 
    # Try printing it afterwards to see the NameError (comment out the print so the script runs).
    pass

    # --- SOLUTION ---
    # temp_data = 500
    # del temp_data
    # # print(temp_data) # This would raise a NameError


def problem_34_multiline_strings():
    # TODO: Create a multiline string using triple quotes (""") containing a short poem or message.
    # Print the multiline string.
    pass

    # --- SOLUTION ---
    # message = """This is a
    # multiline string
    # in Python!"""
    # print(message)


def problem_35_boolean_casting():
    # TODO: Use bool() to cast an empty string "" to a boolean and print it.
    # TODO: Use bool() to cast a non-empty string "Python" to a boolean and print it.
    pass

    # --- SOLUTION ---
    # print(bool(""))       # Outputs False
    # print(bool("Python")) # Outputs True


def problem_36_multiple_assignment():
    # TODO: Assign the values 10, 20, and 30 to variables x, y, and z in a single line of code.
    # Print x, y, and z.
    pass

    # --- SOLUTION ---
    # x, y, z = 10, 20, 30
    # print(x, y, z)


def problem_37_update_dictionary():
    # TODO: Create a dictionary 'user' = {"name": "Bob", "age": 30}.
    # TODO: Update the "age" key to 31 and print the updated dictionary.
    pass

    # --- SOLUTION ---
    # user = {"name": "Bob", "age": 30}
    # user["age"] = 31
    # print(user)


def problem_38_modify_list():
    # TODO: Create a list 'scores' = [80, 90, 100].
    # TODO: Modify the first element (index 0) to be 85 instead of 80. Print the list.
    pass

    # --- SOLUTION ---
    # scores = [80, 90, 100]
    # scores[0] = 85
    # print(scores)


def problem_39_id_function():
    # TODO: Create variables 'a' = 10 and 'b' = 10.
    # TODO: Print the memory identity of both variables using the id() function. They should be the same!
    pass

    # --- SOLUTION ---
    # a = 10
    # b = 10
    # print(id(a), id(b))


def problem_40_comparison_chaining():
    # TODO: Create a variable 'age' = 25.
    # TODO: Check if 'age' is between 18 and 30 (inclusive) by chaining comparison operators (e.g., 18 <= age <= 30).
    # Print the boolean result.
    pass

    # --- SOLUTION ---
    # age = 25
    # print(18 <= age <= 30)

def problem_41_none_type():
    # TODO: Create a variable 'empty_val' and assign it the special 'None' value.
    # Print the type of 'empty_val'.
    pass

    # --- SOLUTION ---
    # empty_val = None
    # print(type(empty_val))


def problem_42_list_length():
    # TODO: Create a list 'guests' = ["Alice", "Bob", "Charlie", "David"].
    # TODO: Use the len() function to print how many guests are in the list.
    pass

    # --- SOLUTION ---
    # guests = ["Alice", "Bob", "Charlie", "David"]
    # print(len(guests))


def problem_43_dict_get():
    # TODO: You have a dictionary 'config' = {"theme": "dark"}.
    # TODO: Use the .get() method to safely fetch the "font_size". It shouldn't crash if it doesn't exist!
    # Print the result.
    pass

    # --- SOLUTION ---
    # config = {"theme": "dark"}
    # print(config.get("font_size")) # Outputs None


def problem_44_string_replace_chaining():
    # TODO: You have string 'text' = "I like apples and apples".
    # TODO: Chain the .replace() method to replace "apples" with "bananas", and then "like" with "love".
    # Print the final string.
    pass

    # --- SOLUTION ---
    # text = "I like apples and apples"
    # final_text = text.replace("apples", "bananas").replace("like", "love")
    # print(final_text)


def problem_45_modulo_last_digit():
    # TODO: You have a number 'num' = 12345.
    # TODO: Use the modulo operator (%) to extract and print the very last digit of the number.
    pass

    # --- SOLUTION ---
    # num = 12345
    # print(num % 10) # Outputs 5


def problem_46_exponentiation_sqrt():
    # TODO: Calculate the square root of 64 using ONLY the exponentiation operator (**) and print it.
    pass

    # --- SOLUTION ---
    # print(64 ** 0.5) # Outputs 8.0


def problem_47_fstring_math():
    # TODO: Use an f-string to print the result of 5 + 7 directly inside the string.
    # Expected output: "5 + 7 is 12"
    pass

    # --- SOLUTION ---
    # print(f"5 + 7 is {5 + 7}")


def problem_48_list_slicing_reverse():
    # TODO: You have a list 'nums' = [1, 2, 3, 4, 5].
    # TODO: Use list slicing with a negative step to print the list in reverse order.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3, 4, 5]
    # print(nums[::-1])


def problem_49_single_element_tuple():
    # TODO: Create a tuple named 'single' containing just the number 99.
    # Hint: Without a comma, Python thinks it's just a number in parentheses!
    # Print the type of 'single' to verify it is a tuple.
    pass

    # --- SOLUTION ---
    # single = (99,)
    # print(type(single))


def problem_50_set_operations():
    # TODO: Create two sets: set_a = {1, 2, 3} and set_b = {3, 4, 5}.
    # TODO: Find the intersection (common items) using the '&' operator and print it.
    pass

    # --- SOLUTION ---
    # set_a = {1, 2, 3}
    # set_b = {3, 4, 5}
    # print(set_a & set_b)


def problem_51_isalnum():
    # TODO: Check if the string "Python3" contains only letters and numbers using .isalnum()
    # Print the boolean result.
    pass

    # --- SOLUTION ---
    # print("Python3".isalnum())


def problem_52_not_in_operator():
    # TODO: Check if the word "error" is NOT IN the string "All systems nominal."
    # Print the boolean result.
    pass

    # --- SOLUTION ---
    # print("error" not in "All systems nominal.")


def problem_53_inequality_operator():
    # TODO: You have 'a' = 10 and 'b' = 20.
    # TODO: Use the inequality operator (!=) to check if they are different and print the result.
    pass

    # --- SOLUTION ---
    # a = 10
    # b = 20
    # print(a != b)


def problem_54_floor_div_negative():
    # TODO: Calculate -10 divided by 3 using floor division (//) and print it.
    # Note how floor division rounds DOWN to the nearest integer!
    pass

    # --- SOLUTION ---
    # print(-10 // 3) # Outputs -4, not -3!


def problem_55_string_join():
    # TODO: You have a list of words: words = ["Python", "is", "awesome"]
    # TODO: Use the .join() method to combine them into a single string separated by spaces. Print it.
    pass

    # --- SOLUTION ---
    # words = ["Python", "is", "awesome"]
    # print(" ".join(words))


def problem_56_string_split():
    # TODO: You have a CSV string: data = "apple,banana,cherry"
    # TODO: Use the .split() method to break it into a list of fruits and print the list.
    pass

    # --- SOLUTION ---
    # data = "apple,banana,cherry"
    # print(data.split(","))


def problem_57_empty_list_bool():
    # TODO: Cast an empty list [] to a boolean using bool() and print it.
    # Empty sequences evaluate to False in Python!
    pass

    # --- SOLUTION ---
    # print(bool([])) # Outputs False


def problem_58_type_comparison():
    # TODO: Create a variable 'x' = 50.
    # TODO: Check if the type of 'x' is exactly equal to 'int' and print the result.
    pass

    # --- SOLUTION ---
    # x = 50
    # print(type(x) == int)


def problem_59_multi_variable_same_value():
    # TODO: Assign the value 0 to variables 'a', 'b', and 'c' in a single line of code.
    # Print 'a', 'b', and 'c'.
    pass

    # --- SOLUTION ---
    # a = b = c = 0
    # print(a, b, c)


def problem_60_short_circuit_logic():
    # TODO: Python stops evaluating 'and' / 'or' as soon as the result is known.
    # TODO: Print the result of (False and (10 / 0 == 0)). It won't crash!
    pass

    # --- SOLUTION ---
    # print(False and (10 / 0 == 0)) # Outputs False without raising ZeroDivisionError

if __name__ == "__main__":
    print("Welcome to Day 1 Practice Problems!")
    print("Fill in the code for each function and call them here to test your answers.")
    # problem_1_basics()

# ==================================================
# --- Day2 : Day2_StarPatterns.py ---
# ==================================================

# Day 2 Star Patterns: common star pattern codes

# 1. Solid square pattern
size = 5
for i in range(size):
    print("* " * size)

print()

# 2. Left-aligned right-angle triangle (increasing)
for i in range(1, 6):
    print("* " * i)

print()

# 3. Left-aligned inverted right-angle triangle
for i in range(5, 0, -1):
    print("* " * i)

print()

# 4. Right-aligned right-angle triangle
n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print()

# 5. Right-aligned inverted right-angle triangle
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print()

# 6. Centered pyramid pattern
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 7. Inverted centered pyramid pattern
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 8. Diamond pattern
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 9. Hollow square pattern
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "* ")

print()

# 10. Hollow left-aligned triangle
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "* ")

print()

# 11. Hollow centered pyramid
for i in range(1, n + 1):
    if i == 1:
        print("  " * (n - 1) + "*")
    elif i == n:
        print("* " * (2 * n - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")

print()

# 12. Hourglass / diamond outline
for i in range(n, 0, -1):
    if i == n:
        print("* " * (2 * i - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")
for i in range(2, n + 1):
    if i == n:
        print("* " * (2 * i - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")


# ==================================================
# --- Day2 : fix_me_day2.py ---
# ==================================================

# Debugging Exercise: Day 2
# This file contains intentional logic and syntax errors involving loops and conditionals.
# Find them and fix them!

print("Welcome to the Day 2 Debugging Challenge!")

# 1. Syntax error in if statement
temperature = 30
if temperature > 25
    print("It's a hot day!")
else:
    print("It's not too hot.")

# 2. Infinite Loop Error
# Warning: If you run this without fixing it, press Ctrl+C in your terminal to stop it!
count = 5
while count > 0:
    print("Countdown:", count)
    # Hint: Something is missing here that causes the loop to never end

# 3. Logic Error in loop range
# We want to print numbers from 1 to 5 (inclusive)
print("Numbers 1 to 5:")
for i in range(1, 5):
    print(i)

# 4. Indentation Error
# We want to print the multiplication table for 3
for j in range(1, 6):
result = 3 * j
print(f"3 x {j} = {result}")

# 5. Logic error in condition order
# We want to print "Fizz" for multiples of 3, "Buzz" for 5, and "FizzBuzz" for both (like 15).
# Right now, 15 is printing "Fizz". Fix the logic!
num = 15
if num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)

print("If you see this and the outputs look correct, you fixed all the errors! Great job!")


# ==================================================
# --- Day3 : Day3_Practice_Problems.py ---
# ==================================================

# Day 3: 50 Basic Practice Problems and Solutions
# Topics: Strings, Lists, Loop Control, Functions, Scope, and Recursion

# ==========================================
# SECTION 1: STRING OPERATIONS (1 - 10)
# ==========================================

# 1. Print the first character of the string "Python".
s1 = "Python"
print("1.", s1[0])

# 2. Print the last character of the string "Data" using negative indexing.
s2 = "Data"
print("2.", s2[-1])

# 3. Slice the first 3 characters from "Programming".
s3 = "Programming"
print("3.", s3[0:3])

# 4. Reverse the string "Hello" using slicing.
s4 = "Hello"
print("4.", s4[::-1])

# 5. Concatenate "Good" and "Morning" with a space in between.
print("5.", "Good" + " " + "Morning")

# 6. Repeat the string "Hi" 4 times.
print("6.", "Hi" * 4)

# 7. Print the characters from index 2 to 5 in "Developer".
s7 = "Developer"
print("7.", s7[2:6])

# 8. Use negative slicing to get the last two characters of "World".
s8 = "World"
print("8.", s8[-2:])

# 9. Extract every second character from "abcdefgh".
s9 = "abcdefgh"
print("9.", s9[::2])

# 10. Check the length of the string "OpenAI" using len().
s10 = "OpenAI"
print("10.", len(s10))

# ==========================================
# SECTION 2: LIST OPERATIONS (11 - 20)
# ==========================================

# 11. Create a list of 3 colors and print the second color.
colors = ["Red", "Green", "Blue"]
print("11.", colors[1])

# 12. Print the last element of [10, 20, 30, 40] using negative indexing.
nums12 = [10, 20, 30, 40]
print("12.", nums12[-1])

# 13. Slice the middle two elements from [1, 2, 3, 4].
nums13 = [1, 2, 3, 4]
print("13.", nums13[1:3])

# 14. Reverse the list [1, 2, 3, 4, 5] using slicing.
nums14 = [1, 2, 3, 4, 5]
print("14.", nums14[::-1])

# 15. Concatenate two lists: [1, 2] and [3, 4].
print("15.", [1, 2] + [3, 4])

# 16. Extract the first 3 elements of [10, 20, 30, 40, 50].
nums16 = [10, 20, 30, 40, 50]
print("16.", nums16[:3])

# 17. Extract all elements except the first and last in [10, 20, 30, 40].
nums17 = [10, 20, 30, 40]
print("17.", nums17[1:-1])

# 18. Repeat the list [0] 5 times.
print("18.", [0] * 5)

# 19. Find the length of the list [5, 10, 15, 20, 25].
nums19 = [5, 10, 15, 20, 25]
print("19.", len(nums19))

# 20. Slice the last three elements of [1, 2, 3, 4, 5, 6].
nums20 = [1, 2, 3, 4, 5, 6]
print("20.", nums20[-3:])


# ==========================================
# SECTION 3: LOOP CONTROL & EXCEPTIONS (21 - 30)
# ==========================================

# 21. Write a for loop from 1 to 5, but break when reaching 3.
print("21.")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 22. Write a for loop from 1 to 4, and skip 2 using continue.
print("22.")
for i in range(1, 5):
    if i == 2:
        continue
    print(i)

# 23. Create an empty for loop using pass.
for i in range(3):
    pass
print("23. Empty loop executed with pass.")

# 24. Write a while loop from 1 to 5, breaking if the number is 4.
print("24.")
w24 = 1
while w24 <= 5:
    if w24 == 4:
        break
    print(w24)
    w24 += 1

# 25. Use a while loop to print 1 to 4, but skip 3.
print("25.")
w25 = 0
while w25 < 4:
    w25 += 1
    if w25 == 3:
        continue
    print(w25)

# 26. Write an if-statement that uses pass.
if True:
    pass
print("26. If-statement executed with pass.")

# 27. Intentionally cause an IndexError and catch it with try/except.
print("27.")
try:
    print([1, 2][5])
except IndexError as e:
    print("Caught:", e)

# 28. Print characters in "Cat", break if 'a' is found.
print("28.")
for char in "Cat":
    if char == 'a':
        break
    print(char)

# 29. Print characters in "Dog", continue if 'o' is found.
print("29.")
for char in "Dog":
    if char == 'o':
        continue
    print(char)

# 30. Access a string out of bounds and catch IndexError.
print("30.")
try:
    print("Hi"[10])
except IndexError:
    print("String index out of range!")


# ==========================================
# SECTION 4: FUNCTIONS (31 - 40)
# ==========================================

# 31. Write a function that prints "Hello, World!" and call it.
print("31.")
def say_hello():
    print("Hello, World!")
say_hello()

# 32. Write a function that takes a name and prints a greeting.
print("32.")
def greet(name):
    print(f"Hi, {name}!")
greet("Venkatesh")

# 33. Write a function that returns the sum of two numbers.
print("33.")
def add(a, b):
    return a + b
print(add(5, 7))

# 34. Write a function with a default parameter for message.
print("34.")
def show_msg(msg="Default message"):
    print(msg)
show_msg()
show_msg("Custom message")

# 35. Write a function that returns the square of a number.
print("35.")
def square(n):
    return n * n
print(square(4))

# 36. Write a function that accepts *args and returns their sum.
print("36.")
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))

# 37. Write a function that accepts **kwargs and prints them.
print("37.")
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Alice", age=25)

# 38. Write a function with both positional and *args.
print("38.")
def show_first_and_rest(first, *rest):
    print("First:", first, "Rest:", rest)
show_first_and_rest(10, 20, 30, 40)

# 39. Write a function that returns the first character of a string.
print("39.")
def first_char(s):
    return s[0]
print(first_char("Python"))

# 40. Write a function that checks if a list is empty.
print("40.")
def is_empty(lst):
    return len(lst) == 0
print(is_empty([]))


# ==========================================
# SECTION 5: VARIABLE SCOPE (41 - 45)
# ==========================================

# 41. Define a global variable and access it inside a function.
print("41.")
g_var = 100
def access_global():
    print(g_var)
access_global()

# 42. Define a local variable and print it inside the function.
print("42.")
def access_local():
    l_var = 50
    print(l_var)
access_local()

# 43. Modify a global variable inside a function using the 'global' keyword.
print("43.")
count = 0
def increment():
    global count
    count += 1
increment()
print(count)

# 44. Create a local variable with the same name as a global variable.
print("44.")
x = "Global"
def shadow_var():
    x = "Local"
    print("Inside:", x)
shadow_var()
print("Outside:", x)

# 45. Demonstrate that a local variable is destroyed after function exits.
print("45.")
def temp_func():
    temp_var = 99
# temp_var is not accessible here
print("temp_var is only accessible inside temp_func")


# ==========================================
# SECTION 6: RECURSION (46 - 50)
# ==========================================

# 46. Write a recursive function to print numbers from N down to 1.
print("46.")
def countdown(n):
    if n <= 0:
        return
    print(n, end=" ")
    countdown(n - 1)
countdown(3)
print()

# 47. Write a recursive function to calculate the factorial of N.
print("47.")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(4))

# 48. Write a recursive function to find the sum of numbers from 1 to N.
print("48.")
def sum_n(n):
    if n <= 1:
        return 1
    return n + sum_n(n - 1)
print(sum_n(5))

# 49. Write a recursive function to find the Nth Fibonacci number.
print("49.")
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fib(5) =", fibonacci(5))

# 50. Write a recursive function to reverse a string.
print("50.")
def reverse_str(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_str(s[:-1])
print(reverse_str("hello"))

# --- End of Practice Problems ---


# ==================================================
# --- Day3 : Day3_Test_Driven_Practice.py ---
# ==================================================

# Day 3: Test-Driven Practice
# Complete the functions below so that all assert statements pass!

def find_max_in_list(lst):
    """
    Return the maximum number in the list without using the built-in max() function.
    """
    # YOUR CODE HERE
    pass

def remove_duplicates(lst):
    """
    Return a new list with duplicates removed, preserving the original order.
    """
    # YOUR CODE HERE
    pass

def sum_even_numbers(lst):
    """
    Return the sum of all even numbers in the list.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
if __name__ == "__main__":
    print("Running tests...")
    
    # Test find_max_in_list
    try:
        assert find_max_in_list([1, 5, 3, 9, 2]) == 9
        assert find_max_in_list([-10, -5, -20]) == -5
        print("✅ find_max_in_list tests passed!")
    except AssertionError:
        print("❌ find_max_in_list tests failed!")

    # Test remove_duplicates
    try:
        assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
        assert remove_duplicates(["a", "b", "a"]) == ["a", "b"]
        print("✅ remove_duplicates tests passed!")
    except AssertionError:
        print("❌ remove_duplicates tests failed!")

    # Test sum_even_numbers
    try:
        assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
        assert sum_even_numbers([1, 3, 5]) == 0
        print("✅ sum_even_numbers tests passed!")
    except AssertionError:
        print("❌ sum_even_numbers tests failed!")

    print("Test run complete.")


# ==================================================
# --- Day4 : Day4_Practice_Problems.py ---
# ==================================================

# Day 4: 50 Basic Practice Problems and Solutions
# Topics: String Methods, Anagrams, Recursion

# ==========================================
# SECTION 1: STRING METHODS (1 - 20)
# ==========================================

# 1. Convert the string "hello" to uppercase.
print("1.", "hello".upper())

# 2. Convert the string "WORLD" to lowercase.
print("2.", "WORLD".lower())

# 3. Remove the leading and trailing spaces from "  python  ".
print("3.", "  python  ".strip())

# 4. Remove the trailing spaces from "data   ".
print("4.", "data   ".rstrip())

# 5. Replace "cat" with "dog" in the string "The cat sat".
print("5.", "The cat sat".replace("cat", "dog"))

# 6. Split the string "a,b,c,d" by comma.
print("6.", "a,b,c,d".split(","))

# 7. Split the string "Hello World" by space.
print("7.", "Hello World".split())

# 8. Join the list ["a", "b", "c"] with a dash "-".
print("8.", "-".join(["a", "b", "c"]))

# 9. Find the index of "y" in "Python".
print("9.", "Python".find("y"))

# 10. Check if the string "12345" consists only of digits.
print("10.", "12345".isdigit())

# 11. Check if the string "hello" consists only of alphabetic characters.
print("11.", "hello".isalpha())

# 12. Count the number of 'a's in "banana".
print("12.", "banana".count("a"))

# 13. Convert "this is a title" to title case.
print("13.", "this is a title".title())

# 14. Check if "Hello World" starts with "Hello".
print("14.", "Hello World".startswith("Hello"))

# 15. Check if "report.pdf" ends with ".pdf".
print("15.", "report.pdf".endswith(".pdf"))

# 16. Replace all spaces in "a b c" with underscores.
print("16.", "a b c".replace(" ", "_"))

# 17. Find the index of 'z' in "hello". (Should return -1).
print("17.", "hello".find("z"))

# 18. Split the string "apple-orange-grape" by "-".
print("18.", "apple-orange-grape".split("-"))

# 19. Join ["I", "love", "Python"] with spaces.
print("19.", " ".join(["I", "love", "Python"]))

# 20. Count how many times "in" appears in "interesting".
print("20.", "interesting".count("in"))

# ==========================================
# SECTION 2: ANAGRAM LOGIC (21 - 30)
# ==========================================

# 21. Check if "cat" and "act" are anagrams using sorting.
print("21.", sorted("cat") == sorted("act"))

# 22. Check if "hello" and "olleh" are anagrams.
print("22.", sorted("hello") == sorted("olleh"))

# 23. Do "test" and "tast" match using sorting?
print("23.", sorted("test") == sorted("tast"))

# 24. Write a snippet to sort characters in the string "python".
print("24.", sorted("python"))

# 25. Check anagram ignoring spaces: "dormitory" and "dirty room".
s1 = "dormitory".replace(" ", "")
s2 = "dirty room".replace(" ", "")
print("25.", sorted(s1) == sorted(s2))

# 26. Count the frequency of characters in "apple" using a dictionary.
freq = {}
for char in "apple":
    freq[char] = freq.get(char, 0) + 1
print("26.", freq)

# 27. Compare character frequencies of "tea" and "eat".
freq1 = {'t':1, 'e':1, 'a':1}
freq2 = {'e':1, 'a':1, 't':1}
print("27.", freq1 == freq2)

# 28. If len(s1) != len(s2), can they be anagrams?
print("28.", "False, they must be the same length.")

# 29. Check anagram ignoring case: "Tea" and "Eat".
print("29.", sorted("Tea".lower()) == sorted("Eat".lower()))

# 30. How do you convert a sorted list of characters back to a string?
print("30.", "".join(sorted("apple")))

# ==========================================
# SECTION 3: RECURSION (31 - 50)
# ==========================================

# 31. Write a recursive function to print "Hello" N times.
print("31.")
def print_hello(n):
    if n == 0: return
    print("Hello", end=" ")
    print_hello(n-1)
print_hello(3); print()

# 32. Recursive function to find the sum of numbers from 1 to 5.
print("32.")
def sum_n(n):
    if n == 1: return 1
    return n + sum_n(n-1)
print(sum_n(5))

# 33. Factorial of 5 using recursion.
print("33.")
def fact(n):
    if n == 0 or n == 1: return 1
    return n * fact(n-1)
print(fact(5))

# 34. Fibonacci number at position 6 using recursion.
print("34.")
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
print(fib(6))

# 35. Recursive function to count down from 3 to 1.
print("35.")
def count_down(n):
    if n == 0: return
    print(n, end=" ")
    count_down(n-1)
count_down(3); print()

# 36. Recursive function to reverse a string "abc".
print("36.")
def rev_str(s):
    if len(s) == 0: return s
    return s[-1] + rev_str(s[:-1])
print(rev_str("abc"))

# 37. Recursive function to find the length of a string.
print("37.")
def str_len(s):
    if s == "": return 0
    return 1 + str_len(s[1:])
print(str_len("python"))

# 38. Recursive function to check if a string is a palindrome.
print("38.")
def is_pal(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_pal(s[1:-1])
print(is_pal("radar"))

# 39. Count occurrences of a character in a string recursively.
print("39.")
def count_char(s, char):
    if not s: return 0
    return (1 if s[0] == char else 0) + count_char(s[1:], char)
print(count_char("apple", "p"))

# 40. Calculate 2^3 using recursion.
print("40.")
def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp-1)
print(power(2, 3))

# 41. Sum of elements in a list recursively.
print("41.")
def sum_list(lst):
    if not lst: return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4]))

# 42. Find the max element in a list recursively.
print("42.")
def max_list(lst):
    if len(lst) == 1: return lst[0]
    m = max_list(lst[1:])
    return lst[0] if lst[0] > m else m
print(max_list([1, 5, 3, 9, 2]))

# 43. Print elements of a list recursively.
print("43.")
def print_list(lst):
    if not lst: return
    print(lst[0], end=" ")
    print_list(lst[1:])
print_list([1,2,3]); print()

# 44. Print elements of a list in reverse order recursively.
print("44.")
def print_rev_list(lst):
    if not lst: return
    print_rev_list(lst[1:])
    print(lst[0], end=" ")
print_rev_list([1,2,3]); print()

# 45. Find GCD of two numbers using Euclidean algorithm recursively.
print("45.")
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
print(gcd(48, 18))

# 46. Check if an array is sorted recursively.
print("46.")
def is_sorted(lst):
    if len(lst) <= 1: return True
    if lst[0] > lst[1]: return False
    return is_sorted(lst[1:])
print(is_sorted([1, 2, 3, 4]))

# 47. Recursive function to multiply two numbers without using '*'.
print("47.")
def mult(a, b):
    if b == 0: return 0
    return a + mult(a, b-1)
print(mult(5, 4))

# 48. Print the binary representation of a number recursively.
print("48.")
def dec_to_bin(n):
    if n == 0: return
    dec_to_bin(n // 2)
    print(n % 2, end="")
dec_to_bin(10); print()

# 49. Check if a number is even recursively.
print("49.")
def is_even(n):
    if n == 0: return True
    if n == 1: return False
    return is_even(n - 2)
print(is_even(10))

# 50. Remove all vowels from a string recursively.
print("50.")
def rem_vowels(s):
    if not s: return ""
    first = "" if s[0].lower() in "aeiou" else s[0]
    return first + rem_vowels(s[1:])
print(rem_vowels("hello world"))

# --- End of Practice Problems ---


# ==================================================
# --- Day4 : Day4_Test_Driven_Practice.py ---
# ==================================================

# Day 4: Test-Driven Practice
# Complete the functions below so that all assert statements pass without errors!

def is_anagram(s1, s2):
    """
    Return True if s1 and s2 are anagrams, ignoring case and spaces.
    Otherwise return False.
    """
    # YOUR CODE HERE
    pass

def count_vowels_recursive(s):
    """
    Return the number of vowels (a, e, i, o, u) in the string s using RECURSION.
    """
    # YOUR CODE HERE
    pass

def reverse_string_recursive(s):
    """
    Return the reversed version of string s using RECURSION.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
if __name__ == "__main__":
    print("Running tests...")
    
    # Test is_anagram
    try:
        assert is_anagram("Listen", "Silent") == True
        assert is_anagram("hello", "world") == False
        assert is_anagram("Astronomer", "Moon starer") == True
        print("✅ is_anagram tests passed!")
    except AssertionError:
        print("❌ is_anagram tests failed!")

    # Test count_vowels_recursive
    try:
        assert count_vowels_recursive("hello") == 2
        assert count_vowels_recursive("xyz") == 0
        assert count_vowels_recursive("education") == 5
        print("✅ count_vowels_recursive tests passed!")
    except AssertionError:
        print("❌ count_vowels_recursive tests failed!")

    # Test reverse_string_recursive
    try:
        assert reverse_string_recursive("hello") == "olleh"
        assert reverse_string_recursive("Python") == "nohtyP"
        assert reverse_string_recursive("") == ""
        print("✅ reverse_string_recursive tests passed!")
    except AssertionError:
        print("❌ reverse_string_recursive tests failed!")

    print("Test run complete.")


# ==================================================
# --- Day5 : Day5_Practice_Problems.py ---
# ==================================================

# Day 5 Practice Problems

# Problem 1: Sum all numbers in a list
def sum_list(nums):
    total = 0
    for num in nums:
        total += num
    return total

# Problem 2: Product of all numbers in a list
def product_list(nums):
    if not nums:
        return 0
    product = 1
    for num in nums:
        product *= num
    return product

# Problem 3: Frequencies count of values
def count_frequencies(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    return freq

# Problem 4: Sum of squares
def sum_of_squares(nums):
    total = 0
    for num in nums:
        total += num * num
    return total

# Problem 5: Printing squares
def print_squares(nums):
    squares = [num * num for num in nums]
    print("Squares:", squares)
    return squares

# Problem 6: Printing all combination pairs in a given list
def print_combination_pairs(nums):
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            pairs.append((nums[i], nums[j]))
    return pairs

if __name__ == "__main__":
    test_list = [1, 2, 3, 4]
    print("Sum:", sum_list(test_list))
    print("Product:", product_list(test_list))
    print("Frequencies:", count_frequencies([1, 2, 2, 3, 1, 4]))
    print("Sum of Squares:", sum_of_squares(test_list))
    print_squares(test_list)
    print("Combination Pairs:", print_combination_pairs(test_list))


# ==================================================
# --- Day5 : Day5_Test_Driven_Practice.py ---
# ==================================================

import unittest

def sum_all_numbers(nums):
    return sum(nums)

def product_all_numbers(nums):
    if not nums: return 0
    res = 1
    for n in nums: res *= n
    return res

def count_frequencies(nums):
    freq = {}
    for n in nums:
        freq[n] = freq.get(n, 0) + 1
    return freq

class TestDay5Methods(unittest.TestCase):

    def test_sum_all_numbers(self):
        self.assertEqual(sum_all_numbers([1, 2, 3]), 6)
        self.assertEqual(sum_all_numbers([10, -10, 5]), 5)

    def test_product_all_numbers(self):
        self.assertEqual(product_all_numbers([1, 2, 3, 4]), 24)
        self.assertEqual(product_all_numbers([]), 0)
        self.assertEqual(product_all_numbers([5, 0, 2]), 0)

    def test_count_frequencies(self):
        self.assertEqual(count_frequencies([1, 1, 2]), {1: 2, 2: 1})
        self.assertEqual(count_frequencies(["a", "b", "a"]), {"a": 2, "b": 1})

if __name__ == '__main__':
    unittest.main()

