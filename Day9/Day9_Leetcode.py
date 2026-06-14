# Day 9 Leetcode Problems: Advanced Sorting Mechanics
# These problems test your ability to use QuickSelect and Custom Sorting.

# ==================================================
# Problem 1: Leetcode 215 - Kth Largest Element in an Array
# Difficulty: Medium
# ==================================================
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?

def findKthLargest(nums: list[int], k: int) -> int:
    # We will use QuickSelect to achieve O(n) average time complexity!
    # Note: Kth largest is the (len(nums) - k + 1)-th smallest element.
    target_k = len(nums) - k + 1
    
    def quickselect(arr, k_smallest):
        # We use a random pivot to avoid worst-case O(n^2) on already sorted arrays
        import random
        pivot = random.choice(arr)
        
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        if k_smallest <= len(left):
            return quickselect(left, k_smallest)
        elif k_smallest <= len(left) + len(mid):
            return pivot
        else:
            return quickselect(right, k_smallest - len(left) - len(mid))
            
    return quickselect(nums, target_k)

# Dry Run for nums = [3,2,1,5,6,4], k = 2
# Target is (6 - 2 + 1) = 5th smallest element.
# Say pivot is 4.
# left = [3, 2, 1], mid = [4], right = [5, 6]
# 5 <= len(left)(3) ? No.
# 5 <= len(left)+len(mid)(4) ? No.
# So we search `right`, looking for 5 - 4 = 1st smallest.
# quickselect([5, 6], 1). Pivot say 5. left=[], mid=[5], right=[6].
# 1 <= 0 ? No. 1 <= 1 ? Yes! Return 5.


# ==================================================
# Problem 2: Leetcode 973 - K Closest Points to Origin
# Difficulty: Medium
# ==================================================
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).
# The distance is computed using the Euclidean distance: sqrt(x^2 + y^2).

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    # We can use Python's built-in sort with a custom lambda function!
    # Timsort is incredibly fast (O(n log n)).
    # Distance formula: x^2 + y^2 (We don't need sqrt since it doesn't change the order)
    
    points.sort(key=lambda P: P[0]**2 + P[1]**2)
    return points[:k]

# Dry Run for points = [[3,3],[5,-1],[-2,4]], k = 2
# Distances:
# [3,3] -> 9+9 = 18
# [5,-1] -> 25+1 = 26
# [-2,4] -> 4+16 = 20
# Sorted by distance: [[3,3], [-2,4], [5,-1]]
# Return first k (2) elements: [[3,3], [-2,4]]


if __name__ == "__main__":
    print("Testing Kth Largest:", findKthLargest([3,2,1,5,6,4], 2))
    print("Testing K Closest Points:", kClosest([[3,3],[5,-1],[-2,4]], 2))
