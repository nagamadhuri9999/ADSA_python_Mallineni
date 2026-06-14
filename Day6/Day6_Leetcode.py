# Day 6 Leetcode Problems: Binary Search
# These problems test your ability to implement O(log n) searching algorithms.

# ==================================================
# Problem 1: Leetcode 704 - Binary Search
# Difficulty: Easy
# ==================================================
# Given an array of integers nums which is sorted in ascending order, and an integer target, 
# write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

def search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1

# Dry Run for nums = [-1,0,3,5,9,12], target = 9:
# left=0, right=5. mid=2 (val=3). 3 < 9. left becomes 3.
# left=3, right=5. mid=4 (val=9). 9 == 9. Return 4.


# ==================================================
# Problem 2: Leetcode 35 - Search Insert Position
# Difficulty: Easy
# ==================================================
# Given a sorted array of distinct integers and a target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    # If we don't find it, 'left' points exactly to where it should be inserted!
    return left

# Dry Run for nums = [1,3,5,6], target = 2:
# left=0, right=3. mid=1 (val=3). 3 > 2. right becomes 0.
# left=0, right=0. mid=0 (val=1). 1 < 2. left becomes 1.
# Loop ends. Return left (1). Correct!


# ==================================================
# Problem 3: Leetcode 34 - Find First and Last Position of Element in Sorted Array
# Difficulty: Medium
# ==================================================
# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

def searchRange(nums: list[int], target: int) -> list[int]:
    
    # Helper to find the FIRST occurrence
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1  # Keep searching to the left!
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    # Helper to find the LAST occurrence
    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1  # Keep searching to the right!
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    return [findFirst(nums, target), findLast(nums, target)]

# Dry Run for nums = [5,7,7,8,8,10], target = 8:
# findFirst will lock onto index 4, but since we do `right = mid - 1`, it searches left and finds index 3.
# findLast will lock onto index 3, but does `left = mid + 1`, searches right and finds index 4.
# Returns [3, 4]


if __name__ == "__main__":
    print("Testing Binary Search:", search([-1,0,3,5,9,12], 9))
    print("Testing Search Insert:", searchInsert([1,3,5,6], 2))
    print("Testing Search Range:", searchRange([5,7,7,8,8,10], 8))
