# Day 5 Capstone Task: The Data Analyst

## Objective
Build a program that takes raw string input from a user, converts it into a list of numbers, and then performs two analytical operations: Frequency Counting and Pair Generation. This will test your knowledge of input parsing, dictionary manipulation, and nested loops.

## Requirements

1. **Input Processing:**
   - Prompt the user to enter a list of space-separated numbers (e.g., `"1 2 2 3"`).
   - Read this string, split it, and convert it into a list of integers.

2. **Frequency Analysis:**
   - Create a function `count_frequencies(nums)` that takes the integer list and returns a dictionary showing how many times each number appears.
   - Use the `.get()` method to handle missing keys gracefully.
   - Print the resulting dictionary.

3. **Combination Pairs:**
   - Create a function `print_unique_pairs(nums)` that prints every unique pair of numbers in the list.
   - Use nested loops. The inner loop must start at `i + 1` to prevent duplicate pairs (e.g., (1, 2) and (2, 1)) and self-pairing (e.g., (1, 1)).

4. **Integration:**
   - Combine these steps into a single script that runs sequentially.

## Example Output
```text
Enter space-separated numbers: 1 2 2 3

--- Frequency Analysis ---
Number 1 appears 1 time(s)
Number 2 appears 2 time(s)
Number 3 appears 1 time(s)

--- Unique Pairs ---
(1, 2)
(1, 2)
(1, 3)
(2, 2)
(2, 3)
(2, 3)
```

Good luck!
