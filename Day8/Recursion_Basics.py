# Day 8: Introduction to Recursion - Basic Problems
# --------------------------------------------------------
# Recursion occurs when a function calls itself.
# Every recursive function MUST have:
# 1. Base Case: The condition to stop the recursion.
# 2. Recursive Case: The logic to break the problem into a smaller subproblem.

# ==========================================
# PROBLEM 1: Print Numbers from N down to 1
# ==========================================
def print_n_to_1(n):
    # Base Case
    if n <= 0:
        return
    
    # Process current node first, then recurse
    print(n, end=" ")
    print_n_to_1(n - 1)


# ==========================================
# PROBLEM 2: Print Numbers from 1 up to N
# ==========================================
def print_1_to_n(n):
    # Base Case
    if n <= 0:
        return
    
    # Recurse first (this builds the call stack), then print on the way back down
    print_1_to_n(n - 1)
    print(n, end=" ")


# ==========================================
# PROBLEM 3: Sum of First N Natural Numbers
# ==========================================
def sum_n(n):
    if n <= 0:
        return 0
    return n + sum_n(n - 1)


# ==========================================
# PROBLEM 4: Power of a Number (x^n)
# ==========================================
def power(x, n):
    # Base case: anything to the power of 0 is 1
    if n == 0:
        return 1
    return x * power(x, n - 1)


# ==========================================
# PROBLEM 5: Count Digits in a Number
# ==========================================
def count_digits(n):
    # Handle negative numbers
    n = abs(n)
    
    # Base case: if n is a single digit
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


# ==========================================
# PROBLEM 6: Reverse a String
# ==========================================
def reverse_string(s):
    # Base Case: Empty string or single character
    if len(s) <= 1:
        return s
    
    # Take the first character and put it at the end of the reversed remaining string
    return reverse_string(s[1:]) + s[0]


# ==========================================
# PROBLEM 7: Check if a String is a Palindrome
# ==========================================
def is_palindrome(s):
    # Base Case: If string is 0 or 1 character long, it's a palindrome
    if len(s) <= 1:
        return True
    
    # If the first and last characters match, check the substring inside them
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


if __name__ == "__main__":
    print("1. Print N to 1 (N=5):")
    print_n_to_1(5)
    print("\n")
    
    print("2. Print 1 to N (N=5):")
    print_1_to_n(5)
    print("\n")
    
    print(f"3. Sum of first 5 natural numbers: {sum_n(5)}")
    
    print(f"4. Power (2^3): {power(2, 3)}")
    
    print(f"5. Count digits in 12345: {count_digits(12345)}")
    
    print(f"6. Reverse string 'recursion': {reverse_string('recursion')}")
    
    print(f"7. Is 'racecar' a palindrome?: {is_palindrome('racecar')}")
    print(f"   Is 'hello' a palindrome?: {is_palindrome('hello')}")
