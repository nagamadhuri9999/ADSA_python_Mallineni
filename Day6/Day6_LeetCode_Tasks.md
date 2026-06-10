# Day 6: LeetCode Practice Tasks (Time and Space Complexity)

These tasks are designed to test your understanding of algorithmic efficiency. Your goal is to not only solve them, but to optimize them from a naive brute-force approach to a faster Big O time complexity.

## Task 1: LeetCode 1. Two Sum
**Difficulty**: Easy
**Description**: Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

**Complexity Goal**: 
- *Brute Force*: O(N^2) using nested loops.
- *Optimized*: O(N) using a dictionary (Hash Map).

## Task 2: LeetCode 204. Count Primes
**Difficulty**: Medium
**Description**: Given an integer `n`, return the number of prime numbers that are strictly less than `n`.

**Complexity Goal**:
- *Brute Force*: O(N * sqrt(N)) checking each number individually.
- *Optimized*: O(N log(log N)) using the Sieve of Eratosthenes (research this!).

## Task 3: LeetCode 367. Valid Perfect Square
**Difficulty**: Easy
**Description**: Given a positive integer `num`, return `true` if `num` is a perfect square or `false` otherwise. Do not use any built-in library function such as `sqrt`.

**Complexity Goal**:
- *Brute Force*: O(N) checking every number up to `num`.
- *Optimized*: O(sqrt(N)) using a while loop ending at `i * i <= num`.
