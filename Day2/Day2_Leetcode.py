# Day 2 Leetcode Problems: Control Flow (Conditionals & Loops)
# These problems are specifically chosen to practice 'if/elif/else' and 'for/while' loops.

# ==================================================
# Problem 1: Leetcode 412 - Fizz Buzz
# Difficulty: Easy
# ==================================================
# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

def fizzBuzz(n: int) -> list[str]:
    answer = []
    # Use a for loop to iterate from 1 to n (inclusive)
    for i in range(1, n + 1):
        # The order of conditionals matters! Check the strictest condition first.
        if i % 3 == 0 and i % 5 == 0:
            answer.append("FizzBuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))
    return answer

# Dry Run for n = 3:
# i = 1: 1%3!=0, 1%5!=0 -> answer.append("1")
# i = 2: 2%3!=0, 2%5!=0 -> answer.append("2")
# i = 3: 3%3==0 -> answer.append("Fizz")
# Result: ["1", "2", "Fizz"]


# ==================================================
# Problem 2: Leetcode 9 - Palindrome Number
# Difficulty: Easy
# ==================================================
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example: 121 -> true. -121 -> false. 10 -> false.
# Constraint: Try doing it without converting the integer to a string (use a while loop!)

def isPalindrome(x: int) -> bool:
    # Negative numbers and numbers ending in 0 (except 0 itself) cannot be palindromes.
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    
    reversed_num = 0
    original = x
    
    # Use a while loop to reverse the number mathematically
    while x > 0:
        last_digit = x % 10
        reversed_num = (reversed_num * 10) + last_digit
        x = x // 10  # Floor division to remove the last digit
        
    return original == reversed_num

# Dry Run for x = 121:
# reversed_num = 0, x = 121
# Loop 1: last_digit = 1, reversed_num = 1, x = 12
# Loop 2: last_digit = 2, reversed_num = 12, x = 1
# Loop 3: last_digit = 1, reversed_num = 121, x = 0
# Loop breaks. 121 == 121 -> Returns True.


# ==================================================
# Problem 3: Leetcode 231 - Power of Two
# Difficulty: Easy
# ==================================================
# Given an integer n, return true if it is a power of two. Otherwise, return false.

def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    
    # As long as the number is perfectly divisible by 2, keep dividing it by 2.
    while n % 2 == 0:
        n = n // 2
        
    # If it was a power of two, it will eventually reduce to exactly 1.
    return n == 1

# Dry Run for n = 8:
# 8 % 2 == 0 -> n = 4
# 4 % 2 == 0 -> n = 2
# 2 % 2 == 0 -> n = 1
# 1 % 2 != 0 -> Loop breaks. n == 1 -> Returns True.

if __name__ == "__main__":
    print("Testing FizzBuzz(5):", fizzBuzz(5))
    print("Testing isPalindrome(121):", isPalindrome(121))
    print("Testing isPowerOfTwo(8):", isPowerOfTwo(8))
