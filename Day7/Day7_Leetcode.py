# Day 7 Leetcode Problems: Space Complexity & Sorting
# These problems test your ability to sort arrays and utilize O(1) auxiliary space.

# ==================================================
# Problem 1: Leetcode 75 - Sort Colors
# Difficulty: Medium
# ==================================================
# Given an array nums with n objects colored red, white, or blue, sort them in-place 
# so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

def sortColors(nums: list[int]) -> None:
    # Since N is very small (1 <= n <= 300), an O(n^2) algorithm like Bubble Sort or Insertion Sort works perfectly!
    # Let's use Insertion Sort to do it in-place.
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

# Dry Run for nums = [2, 0, 2, 1, 1, 0]:
# i = 1, key = 0. 0 < 2, so swap. nums becomes [0, 2, 2, 1, 1, 0]
# i = 2, key = 2. 2 is not < 2. No movement.
# i = 3, key = 1. 1 < 2, swap down to right place. nums becomes [0, 1, 2, 2, 1, 0]
# ... and so on until sorted!


# ==================================================
# Problem 2: Leetcode 169 - Majority Element (Sorting Approach)
# Difficulty: Easy
# ==================================================
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.

def majorityElement(nums: list[int]) -> int:
    # We solved this with Frequency Counting in Day 5.
    # Today, we solve it using Sorting!
    # If an element appears more than n/2 times, then if we sort the array, 
    # that element MUST occupy the exact middle index of the array!
    
    # We use Python's built-in sort here which is O(n log n).
    nums.sort()
    return nums[len(nums) // 2]

# Dry Run for nums = [2, 2, 1, 1, 1, 2, 2]:
# After sorting: [1, 1, 1, 2, 2, 2, 2]
# Length is 7. Middle index is 7 // 2 = 3.
# nums[3] is 2!


# ==================================================
# Problem 3: Leetcode 268 - Missing Number (Sorting Approach)
# Difficulty: Easy
# ==================================================
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.

def missingNumber(nums: list[int]) -> int:
    # Approach: Sort the array. The index `i` should match the value `nums[i]`.
    # The first index where they don't match is the missing number!
    
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i:
            return i
            
    # If loop finishes, the missing number is the very last one (n).
    return len(nums)

# Dry Run for nums = [3, 0, 1]:
# After sorting: [0, 1, 3]
# i=0: nums[0] == 0. Match!
# i=1: nums[1] == 1. Match!
# i=2: nums[2] == 3. DOES NOT MATCH 2!
# Missing number is 2.


if __name__ == "__main__":
    colors = [2, 0, 2, 1, 1, 0]
    sortColors(colors)
    print("Testing Sort Colors:", colors)
    
    print("Testing Majority Element:", majorityElement([2, 2, 1, 1, 1, 2, 2]))
    print("Testing Missing Number:", missingNumber([3, 0, 1]))
