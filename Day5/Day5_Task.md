# Day 5 Tasks: Data Analyzer & Two Sum

## Task 1: The Data Analyzer

### Objective
Combine your knowledge of lists, iteration, built-in methods, and frequency counting to build a miniature data analysis script.

### Instructions
1. **Data Ingestion**: Prompt the user for a space-separated list of numbers and convert it to a list of integers.
2. **Basic Analytics**: Calculate and print the **Sum**, **Product**, and **Average**.
3. **Advanced Insights**: Use a dictionary to count how many times each number appears in the list (Frequency Count) and print the results.
4. **Pair Generation**: Write a nested loop that generates all unique *pairs* of numbers from the list.

---

## Task 2: Two Sum (LeetCode Classic)

### Objective
Apply nested loops and dictionaries to solve one of the most famous algorithmic interview questions.

### Instructions
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
- You may assume that each input would have exactly one solution.
- You may not use the same element twice.
- You can return the answer in any order.

**Example 1:**
```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

**Example 2:**
```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

**Challenge:** 
1. Solve it using a nested loop (Brute Force - O(N^2)).
2. **Bonus:** Solve it using a frequency/hash map in a single pass (O(N)).
