# Day 5 Leetcode Problems: List Methods and Frequency Counting
# These problems test your ability to use dictionaries for O(n) lookups and frequency counting.

# ==================================================
# Problem 1: Leetcode 1 - Two Sum
# Difficulty: Easy
# ==================================================
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums: list[int], target: int) -> list[int]:
    # Approach 1: Nested Loops (O(n^2)). This is what we learned today!
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
                
    # Approach 2: Dictionary / Hash Map (O(n)). Faster!
    # We store the numbers we've seen so far, and their indices.
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
    return []

# Dry Run for nums = [2, 7, 11, 15], target = 9:
# i = 0, num = 2. Complement = 7. Is 7 in seen? No. seen = {2: 0}
# i = 1, num = 7. Complement = 2. Is 2 in seen? Yes! (at index 0).
# Return [0, 1].


# ==================================================
# Problem 2: Leetcode 136 - Single Number
# Difficulty: Easy
# ==================================================
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity.

def singleNumber(nums: list[int]) -> int:
    # Approach: Frequency Counting using a Dictionary
    freq = {}
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        
    for num, count in freq.items():
        if count == 1:
            return num

# Dry Run for nums = [4, 1, 2, 1, 2]:
# Build freq: {4: 1, 1: 2, 2: 2}
# Loop through items: 
#   4 has count 1. Return 4!


# ==================================================
# Problem 3: Leetcode 169 - Majority Element
# Difficulty: Easy
# ==================================================
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.

def majorityElement(nums: list[int]) -> int:
    # Approach: Frequency Counting
    freq = {}
    threshold = len(nums) // 2
    
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        # Early exit: If we hit the threshold, we found it!
        if freq[num] > threshold:
            return num

# Dry Run for nums = [2, 2, 1, 1, 1, 2, 2]:
# threshold = 7 // 2 = 3.
# We need a number that appears 4 or more times.
# After looping, freq[2] reaches 4. Returns 2.


if __name__ == "__main__":
    print("Testing Two Sum:", twoSum([2, 7, 11, 15], 9))
    print("Testing Single Number:", singleNumber([4, 1, 2, 1, 2]))
    print("Testing Majority Element:", majorityElement([2, 2, 1, 1, 1, 2, 2]))
