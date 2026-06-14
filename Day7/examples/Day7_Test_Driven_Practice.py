import unittest

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

class TestDay7Methods(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual(selection_sort([64, 25, 12, 22, 11]), [11, 12, 22, 25, 64])
        self.assertEqual(selection_sort([]), [])
        
    def test_binary_search(self):
        self.assertEqual(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91], 23), 5)
        self.assertEqual(binary_search([1, 2, 3], 4), -1)

if __name__ == '__main__':
    unittest.main()
