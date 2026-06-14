# Day 3 Leetcode Problems: Strings, Lists, and Functions
# These problems focus on string manipulation, list indexing, and basic algorithms.

# ==================================================
# Problem 1: Leetcode 344 - Reverse String
# Difficulty: Easy
# ==================================================
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

def reverseString(s: list[str]) -> None:
    # Python makes this incredibly easy using slice assignment!
    # [::-1] creates a reversed copy, and s[:] assigns it back to the original list reference.
    s[:] = s[::-1]
    
    # Alternatively, you can use the built-in method:
    # s.reverse()

# Dry Run for s = ["h","e","l","l","o"]:
# s[::-1] generates ["o","l","l","e","h"]
# s[:] = ... assigns those elements back to the original memory address of s.


# ==================================================
# Problem 2: Leetcode 58 - Length of Last Word
# Difficulty: Easy
# ==================================================
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(s: str) -> int:
    # 1. .strip() removes leading and trailing whitespaces.
    # 2. .split() breaks the string into a list of words.
    words = s.strip().split()
    
    # 3. [-1] uses negative indexing to grab the very last word in the list.
    # 4. len() gets the character count of that word.
    return len(words[-1])

# Dry Run for s = "   fly me   to   the moon  ":
# s.strip() -> "fly me   to   the moon"
# .split() -> ["fly", "me", "to", "the", "moon"]
# words[-1] -> "moon"
# len("moon") -> 4


# ==================================================
# Problem 3: Leetcode 26 - Remove Duplicates from Sorted Array
# Difficulty: Easy
# ==================================================
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
# such that each unique element appears only once. The relative order of the elements should be kept the same.
# Return the number of unique elements in nums.

def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0
        
    # 'insert_index' acts as a pointer to where the next unique element should go.
    insert_index = 1
    
    for i in range(1, len(nums)):
        # If the current element is different from the previous element, it's unique!
        if nums[i] != nums[i - 1]:
            # Place it at the insert_index, then increment the index.
            nums[insert_index] = nums[i]
            insert_index += 1
            
    return insert_index

# Dry Run for nums = [1, 1, 2]:
# insert_index = 1
# i = 1: nums[1] (1) == nums[0] (1). Condition fails.
# i = 2: nums[2] (2) != nums[1] (1). Condition passes!
#   nums[1] becomes 2. nums is now [1, 2, 2].
#   insert_index becomes 2.
# Loop ends. Returns 2 (the count of unique elements).


if __name__ == "__main__":
    # Test 1
    s_list = ["h","e","l","l","o"]
    reverseString(s_list)
    print("Reverse String:", s_list)
    
    # Test 2
    print("Length of Last Word:", lengthOfLastWord("   fly me   to   the moon  "))
    
    # Test 3
    nums_list = [1, 1, 2]
    k = removeDuplicates(nums_list)
    print(f"Remove Duplicates: {k}, Array is now: {nums_list[:k]}")
