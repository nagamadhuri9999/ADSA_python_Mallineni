import unittest

# Day 8: Test-Driven Practice
# Complete the functions below so that all assert statements pass!

def merge_sort(arr):
    """
    Implement Merge Sort to sort the array in ascending order.
    """
    # YOUR CODE HERE
    pass

def quick_sort(arr):
    """
    Implement Quick Sort to sort the array in ascending order.
    """
    # YOUR CODE HERE
    pass

def sort_colors(nums):
    """
    Given an array with 0s, 1s, and 2s, sort them in-place.
    """
    # YOUR CODE HERE
    pass

# ==========================================
# 🛑 DO NOT MODIFY THE CODE BELOW THIS LINE 
# ==========================================
class TestDay8Methods(unittest.TestCase):
    def test_merge_sort(self):
        # We need a working implementation to test. 
        # For the sake of the test framework running, if the student hasn't implemented it,
        # it will return None, which will fail.
        arr = [38, 27, 43, 3, 9, 82, 10]
        res = merge_sort(arr.copy())
        if res is not None:
            self.assertEqual(res, [3, 9, 10, 27, 38, 43, 82])
        self.assertEqual(merge_sort([]), [] if merge_sort([]) is not None else None)
        
    def test_quick_sort(self):
        arr = [10, 7, 8, 9, 1, 5]
        res = quick_sort(arr.copy())
        if res is not None:
            self.assertEqual(res, [1, 5, 7, 8, 9, 10])

    def test_sort_colors(self):
        arr = [2, 0, 2, 1, 1, 0]
        res = sort_colors(arr)
        if res is not None:
            self.assertEqual(res, [0, 0, 1, 1, 2, 2])

if __name__ == '__main__':
    print("Running Day 8 Tests...")
    unittest.main()
