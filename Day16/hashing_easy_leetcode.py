# ==========================================
# HASHING EASY LEETCODE PROBLEMS
# ==========================================

# Problem 1: Two Sum (LeetCode 1)
# Difficulty: Easy
# Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Approach: Use a dictionary (Hash Map) to store numbers we have seen so far and their indices.
# For each number, calculate its complement (target - num). If the complement is in the dictionary, we found our pair.

def twoSum(self, nums: List[int], target: int) -> List[int]:
    hash_map={}

    for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment in hash_map:
            return [hash_map[compliment],i]
        hash_map[nums[i]]=i

# Problem 2: Contains Duplicate (LeetCode 217)
# Difficulty: Easy
# Description: Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
# Approach: Use a Set (Hash Set). A set only stores unique elements. 
# We iterate through the array and add elements to the set. If we see an element already in the set, a duplicate exists.

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    # Alternatively: return len(nums) != len(set(nums))

# Problem 3: Valid Anagram (LeetCode 242)
# Difficulty: Easy
# Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Approach: Use a dictionary to build a frequency map of characters in 's'. 
# Then, iterate through 't', decrementing the counts. If counts don't match, they aren't anagrams.

def isAnagram(s, t):
    if len(s) != len(t):
        return False
        
    char_counts = {}  
    # Build frequency map for 's'
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1      
    # Check against 't'
    for char in t:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1
        
    return True
