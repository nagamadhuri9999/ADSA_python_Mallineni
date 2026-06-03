# Day 4: String Methods & Recursion Quiz

Test your knowledge of Day 4 concepts! Choose the best answer for each question.

---

### 1. What is the output of `"  hello  ".strip()`?
A) `"hello  "`
B) `"  hello"`
C) `"hello"`
D) `"  hello  "`

### 2. Which method converts a string into a list of substrings?
A) `join()`
B) `split()`
C) `slice()`
D) `list()`

### 3. If two strings are anagrams, which of the following is true?
A) They must be identical strings.
B) They must have the same length and exactly the same character counts.
C) They must contain only alphabetic characters.
D) They must have the same frequency of vowels.

### 4. What happens when a recursive function lacks a base case?
A) It returns 0 immediately.
B) It runs once and stops.
C) It causes an infinite loop and eventually a RecursionError.
D) It skips the recursive step.

### 5. In a recursion tree for Fibonacci `fib(4)`, does the function calculate `fib(2)` more than once?
A) Yes, multiple times, which is why memoization is useful.
B) No, it only calculates it exactly once.
C) No, `fib(2)` is the base case and is never called.
D) Yes, but Python automatically caches it by default.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **C) `"hello"`** (The `strip()` method removes both leading and trailing whitespace).
2. **B) `split()`** (The `split()` method breaks a string into a list based on a delimiter).
3. **B) They must have the same length and exactly the same character counts.** (This is the definition of an anagram).
4. **C) It causes an infinite loop and eventually a RecursionError.** (Without a base case, the function calls itself until the call stack limit is reached).
5. **A) Yes, multiple times, which is why memoization is useful.** (The naive recursive Fibonacci has overlapping subproblems).

</details>
