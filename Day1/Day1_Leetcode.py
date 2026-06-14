# Day 1 Leetcode Problems: Fundamentals, Variables, & Operators
# These problems are chosen to practice basic arithmetic operators, variables, and list basics.

# ==================================================
# Problem 1: Leetcode 2235 - Add Two Integers
# Difficulty: Easy
# ==================================================
# Given two integers num1 and num2, return the sum of the two integers.

def sum(num1: int, num2: int) -> int:
    # This is the most fundamental use of the arithmetic '+' operator.
    return num1 + num2

# Dry Run:
# num1 = 12, num2 = 5
# return 12 + 5 -> 17


# ==================================================
# Problem 2: Leetcode 2469 - Convert the Temperature
# Difficulty: Easy
# ==================================================
# You are given a non-negative floating point number rounded to two decimal places celsius, that denotes the temperature in Celsius.
# You should convert Celsius into Kelvin and Fahrenheit and return it as an array [kelvin, fahrenheit].
# Formulas: 
# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00

def convertTemperature(celsius: float) -> list[float]:
    # Using arithmetic operators to calculate new floating point variables
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 1.80) + 32.00
    
    # Returning them as a Python List
    return [kelvin, fahrenheit]

# Dry Run for celsius = 36.50:
# kelvin = 36.50 + 273.15 -> 309.65
# fahrenheit = (36.50 * 1.8) + 32.00 -> 97.7
# return [309.65, 97.7]


# ==================================================
# Problem 3: Leetcode 1929 - Concatenation of Array
# Difficulty: Easy
# ==================================================
# Given an integer array nums of length n, you want to create an array ans of length 2n where 
# ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
# Specifically, ans is the concatenation of two nums arrays. Return the array ans.

def getConcatenation(nums: list[int]) -> list[int]:
    # In Python, the '+' operator is overloaded. 
    # For numbers, it adds. For lists, it concatenates!
    return nums + nums

    # Alternative using the '*' multiplication operator for lists:
    # return nums * 2

# Dry Run for nums = [1, 2, 1]:
# nums + nums -> [1, 2, 1] + [1, 2, 1] -> [1, 2, 1, 1, 2, 1]

if __name__ == "__main__":
    print("Testing Add Two Integers:", sum(12, 5))
    print("Testing Convert Temperature:", convertTemperature(36.50))
    print("Testing Array Concatenation:", getConcatenation([1, 2, 1]))
