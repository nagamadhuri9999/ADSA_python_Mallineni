# Dynamic Programming (DP) Notes

## 1. Dynamic Programming Fundamentals
Dynamic Programming is an algorithmic technique for solving an optimization problem by breaking it down into simpler subproblems and utilizing the fact that the optimal solution to the overall problem depends upon the optimal solution to its subproblems.

### Key Properties:
1. **Overlapping Subproblems:** Subproblems are evaluated many times. DP avoids recomputing them by storing their results.
2. **Optimal Substructure:** The optimal solution to a problem can be constructed from optimal solutions of its subproblems.

### Approaches:
DP problems are typically solved using one of two approaches:
1. **Top-Down (Memoization):** Recursive formulation + caching.
2. **Bottom-Up (Tabulation):** Iterative formulation using tables.

---

## 2. Memoization (Top-Down)
- **Concept:** Start with the main problem and recursively break it down into subproblems. Cache (memoize) the result of each subproblem so you only compute it once.
- **Structure:** Uses recursion. Usually implemented with an array or hash map to store results.
- **Pros:** Natural recursive logic, only evaluates required subproblems (on-demand computation).
- **Cons:** Recursion depth overhead, possible stack overflow for very deep recursions.

**Example: Fibonacci with Memoization (Python)**
```python
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
```

---

## 3. Tabulation (Bottom-Up)
- **Concept:** Solve all related subproblems starting from the smallest (base cases) and iteratively build up to the main problem. 
- **Structure:** Uses iteration (loops). Implemented with an array/table.
- **Pros:** No recursion overhead, faster execution in practice. Often allows space optimization (e.g., storing only previous 1-2 values instead of the entire array).
- **Cons:** Computes all subproblems, even if not all of them are strictly required for the final answer.

**Example: Fibonacci with Tabulation (Python)**
```python
def fib(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

---

## 4. Longest Increasing Subsequence (LIS)
- **Problem Statement:** Given an integer array, find the length of the longest strictly increasing subsequence.
- **DP State Definition:** `dp[i]` = length of the longest increasing subsequence ending at index `i`.
- **State Transition:** `dp[i] = 1 + max(dp[j])` for all `0 <= j < i` such that `nums[j] < nums[i]`.
- **Time Complexity:** $O(N^2)$ (An $O(N \log N)$ approach exists using Binary Search).
- **Space Complexity:** $O(N)$

**Tabulation Approach:**
```python
def lengthOfLIS(nums):
    if not nums: return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
```

---

## 5. Longest Common Subsequence (LCS)
- **Problem Statement:** Given two strings `text1` and `text2`, return the length of their longest common subsequence.
- **DP State Definition:** `dp[i][j]` = length of LCS of `text1[0...i-1]` and `text2[0...j-1]`.
- **State Transition:**
  - If `text1[i-1] == text2[j-1]`: `dp[i][j] = 1 + dp[i-1][j-1]`
  - Else: `dp[i][j] = max(dp[i-1][j], dp[i][j-1])`
- **Time Complexity:** $O(N \times M)$
- **Space Complexity:** $O(N \times M)$ (can be optimized to $O(\min(N, M))$).

**Tabulation Approach:**
```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]
```

---

## 6. Knapsack Problem (0/1 Knapsack)
- **Problem Statement:** Given weights and values of `N` items, and a knapsack of capacity `W`, find the maximum total value you can pack without exceeding the weight limit. Each item can be selected only once (0/1).
- **DP State Definition:** `dp[i][w]` = maximum value using the first `i` items with a weight limit of `w`.
- **State Transition:**
  - If weight of current item > current capacity (`wt[i-1] > w`): `dp[i][w] = dp[i-1][w]` (skip item).
  - Else: `dp[i][w] = max(dp[i-1][w], val[i-1] + dp[i-1][w - wt[i-1]])` (max of skipping or taking the item).
- **Time Complexity:** $O(N \times W)$
- **Space Complexity:** $O(N \times W)$ (can be optimized to $O(W)$ using a 1D array).

**Tabulation Approach:**
```python
def knapSack(W, wt, val, n):
    dp = [[0 for w in range(W + 1)] for i in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][W]
```
