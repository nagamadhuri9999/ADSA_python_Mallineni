# Day 4 Leetcode Problems: String Methods, Anagrams, and Recursion
# These problems test your ability to use sorting, frequency maps, and recursion.

# ==================================================
# Problem 1: Leetcode 242 - Valid Anagram
# Difficulty: Easy
# ==================================================
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

def isAnagram(s: str, t: str) -> bool:
    # Approach 1: Sorting. Very clean, but takes O(n log n) time.
    # return sorted(s) == sorted(t)
    
    # Approach 2: Frequency Counting. Takes O(n) time and O(1) space (since alphabet is fixed 26 chars).
    if len(s) != len(t):
        return False
        
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
        
    for char in t:
        if counts.get(char, 0) == 0:
            return False
        counts[char] -= 1
        
    return True

# Dry Run for s = "cat", t = "tac":
# counts becomes {'c': 1, 'a': 1, 't': 1}
# t[0] = 't' -> exists, decrement 't' to 0
# t[1] = 'a' -> exists, decrement 'a' to 0
# t[2] = 'c' -> exists, decrement 'c' to 0
# Loop finishes successfully. Returns True.


# ==================================================
# Problem 2: Leetcode 49 - Group Anagrams
# Difficulty: Medium
# ==================================================
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    # We use a dictionary where the KEY is the sorted version of the word,
    # and the VALUE is a list of the original words that match that sorted version.
    anagram_map = {}
    
    for word in strs:
        # sorted() returns a list of chars ['a', 'e', 't']. We must join them back to a string "aet" to use as a key.
        sorted_word = "".join(sorted(word))
        
        if sorted_word not in anagram_map:
            anagram_map[sorted_word] = []
            
        anagram_map[sorted_word].append(word)
        
    return list(anagram_map.values())

# Dry Run for strs = ["eat", "tea", "bat"]:
# word = "eat" -> sorted = "aet". Map: {"aet": ["eat"]}
# word = "tea" -> sorted = "aet". Map: {"aet": ["eat", "tea"]}
# word = "bat" -> sorted = "abt". Map: {"aet": ["eat", "tea"], "abt": ["bat"]}
# values() returns: [["eat", "tea"], ["bat"]]


# ==================================================
# Problem 3: Leetcode 509 - Fibonacci Number
# Difficulty: Easy
# ==================================================
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
# such that each number is the sum of the two preceding ones, starting from 0 and 1.
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).

def fib(n: int) -> int:
    # Base cases: If n is 0 or 1, just return n.
    if n == 0: return 0
    if n == 1: return 1
    
    # Recursive step
    return fib(n - 1) + fib(n - 2)

# Dry Run for fib(3):
# fib(3) = fib(2) + fib(1)
#   fib(2) = fib(1) + fib(0) = 1 + 0 = 1
#   fib(1) = 1
# fib(3) = 1 + 1 = 2


if __name__ == "__main__":
    print("Testing Valid Anagram:", isAnagram("anagram", "nagaram"))
    print("Testing Group Anagrams:", groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    print("Testing Fibonacci(5):", fib(5))
