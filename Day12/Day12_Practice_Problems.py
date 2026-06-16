"""
Day 12 Practice Problems: Circular Queues and Deques
"""
from collections import deque

def check_palindrome_using_deque(s: str) -> bool:
    """
    Checks if a string is a palindrome using a Deque.
    Ignores non-alphanumeric characters and case.
    """
    char_deque = deque()
    
    for char in s:
        if char.isalnum():
            char_deque.append(char.lower())
            
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

def sliding_window_maximum(nums: list[int], k: int) -> list[int]:
    """
    Finds the maximum element in each sliding window of size k using a Deque.
    """
    if not nums or k == 0:
        return []
    if k == 1:
        return nums

    result = []
    d = deque() # Stores indices

    for i in range(len(nums)):
        # Remove elements out of the current window
        while d and d[0] < i - k + 1:
            d.popleft()
        
        # Remove smaller elements from the back
        while d and nums[d[-1]] < nums[i]:
            d.pop()
            
        d.append(i)
        
        # Append the max element to the result
        if i >= k - 1:
            result.append(nums[d[0]])
            
    return result

if __name__ == "__main__":
    print("Testing check_palindrome_using_deque:")
    print("racecar ->", check_palindrome_using_deque("racecar"))
    print("hello ->", check_palindrome_using_deque("hello"))
    print("A man, a plan, a canal: Panama ->", check_palindrome_using_deque("A man, a plan, a canal: Panama"))
    
    print("\nTesting sliding_window_maximum:")
    print("nums = [1,3,-1,-3,5,3,6,7], k = 3 ->", sliding_window_maximum([1,3,-1,-3,5,3,6,7], 3))
