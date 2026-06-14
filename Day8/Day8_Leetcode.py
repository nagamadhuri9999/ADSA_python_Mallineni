# Day 8 Leetcode Problems: Advanced Sorting & Divide and Conquer
# These problems test your ability to implement O(n log n) sorting and merging.

# ==================================================
# Problem 1: Leetcode 912 - Sort an Array
# Difficulty: Medium
# ==================================================
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity 
# and with the smallest space complexity possible.

def sortArray(nums: list[int]) -> list[int]:
    # We will use Merge Sort to guarantee O(n log n) worst-case time complexity.
    # Quick Sort might TLE (Time Limit Exceeded) on Leetcode due to worst-case O(n^2) 
    # if not randomized properly.
    
    if len(nums) <= 1:
        return nums
        
    mid = len(nums) // 2
    left = sortArray(nums[:mid])
    right = sortArray(nums[mid:])
    
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Dry Run for nums = [5, 2, 3, 1]:
# Split into [5, 2] and [3, 1]
# Split into [5], [2] -> Merge to [2, 5]
# Split into [3], [1] -> Merge to [1, 3]
# Merge [2, 5] and [1, 3]:
# 1 < 2? Yes -> result=[1]. j=1
# 2 < 3? Yes -> result=[1, 2]. i=1
# 5 < 3? No -> result=[1, 2, 3]. j=2. Right empty.
# Extend left -> result=[1, 2, 3, 5].


# ==================================================
# Problem 2: Leetcode 88 - Merge Sorted Array
# Difficulty: Easy
# ==================================================
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
# To accommodate this, nums1 has a length of m + n.

def mergeInPlace(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    # We must do this in-place in nums1!
    # Trick: Start merging from the BACK so we don't overwrite elements in nums1 we still need.
    p1 = m - 1        # Pointer for valid elements in nums1
    p2 = n - 1        # Pointer for nums2
    p = m + n - 1     # Pointer for placing at the very end of nums1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
        
    # If there are leftovers in nums2, copy them over.
    # (If leftovers are in nums1, they are already in the right place!)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Dry Run for nums1=[1,2,3,0,0,0], m=3, nums2=[2,5,6], n=3
# p1=2 (val 3), p2=2 (val 6), p=5
# nums2[2] (6) > nums1[2] (3), so nums1[5] = 6. p2=1, p=4
# nums2[1] (5) > nums1[2] (3), so nums1[4] = 5. p2=0, p=3
# ... and so on until sorted in-place!


if __name__ == "__main__":
    print("Testing Sort Array:", sortArray([5, 1, 1, 2, 0, 0]))
    
    nums1 = [1,2,3,0,0,0]
    mergeInPlace(nums1, 3, [2,5,6], 3)
    print("Testing Merge Sorted Array In-Place:", nums1)
