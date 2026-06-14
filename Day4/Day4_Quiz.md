# Day 4: String Methods, Anagrams, and Recursion Quiz

Test your knowledge of Day 4 concepts! Choose the best answer for each question.

---

### 1. Are strings mutable or immutable in Python?
A) Mutable
B) Immutable
C) It depends on how they are created.
D) Mutable only inside functions.

### 2. What does `text.lower()` do?
A) Converts the string to all lowercase and modifies the original string.
B) Converts the string to all lowercase and returns a new string.
C) Throws an error if there are no uppercase letters.
D) Converts only the first letter to lowercase.

### 3. Which method removes leading and trailing whitespace from a string?
A) `.clean()`
B) `.trim()`
C) `.strip()`
D) `.remove_spaces()`

### 4. What is the output of `"apple,banana,cherry".split(",")`?
A) `("apple", "banana", "cherry")`
B) `["apple", "banana", "cherry"]`
C) `"apple banana cherry"`
D) `TypeError`

### 5. How would you join a list of strings `["a", "b", "c"]` with a hyphen `-`?
A) `["a", "b", "c"].join("-")`
B) `join("-", ["a", "b", "c"])`
C) `"-".join(["a", "b", "c"])`
D) `["a", "b", "c"].implode("-")`

### 6. What does `text.find("x")` return if "x" is NOT in the string?
A) `0`
B) `False`
C) `-1`
D) It raises a `ValueError`

### 7. What does `text.count("p")` do?
A) Returns the index of the first "p".
B) Returns the total number of characters in the string.
C) Returns the number of times "p" appears in the string.
D) Throws an error.

### 8. What is the output of `"hello".replace("l", "w")`?
A) `"hewlo"`
B) `"hewwo"`
C) `"hello"`
D) `"hwllo"`

### 9. Which method checks if a string consists entirely of digits?
A) `.isnumeric()` or `.isdigit()`
B) `.is_number()`
C) `.contains_digits()`
D) `.check_digits()`

### 10. What is an anagram?
A) A word spelled the same forwards and backwards.
B) A word formed by rearranging the letters of another word.
C) A word that sounds like another word.
D) A string containing only letters.

### 11. If `s1 = "listen"` and `s2 = "silent"`, what does `sorted(s1) == sorted(s2)` evaluate to?
A) `False`
B) `True`
C) `TypeError`
D) `None`

### 12. What is the time complexity of sorting a string of length `n`?
A) O(n)
B) O(1)
C) O(n log n)
D) O(n^2)

### 13. Which data structure is best for counting the frequency of characters in a string for an O(n) anagram check?
A) List
B) Tuple
C) Dictionary (Hash Map)
D) Set

### 14. What happens if two strings have different lengths when checking for anagrams?
A) They can still be anagrams.
B) They cannot possibly be anagrams.
C) You must pad the shorter string with spaces.
D) The program will crash.

### 15. In Python, what does the `.get(key, default)` method do on a dictionary?
A) It deletes the key and returns the default.
B) It returns the value for the key, or the default if the key doesn't exist.
C) It always returns the default value.
D) It throws a KeyError if the key doesn't exist.

### 16. What is the defining characteristic of a recursive function?
A) It uses a `while` loop.
B) It returns multiple values.
C) It calls itself.
D) It takes no arguments.

### 17. What is a "Base Case" in recursion?
A) The first line of the function.
B) The condition that stops the recursion.
C) The part of the function that calls itself.
D) A `try...except` block.

### 18. What happens if a recursive function lacks a base case?
A) It returns `None`.
B) It runs once and stops.
C) It causes an infinite loop and eventually a `RecursionError` (Stack Overflow).
D) It is caught by the compiler and won't run.

### 19. The underlying data structure that manages recursive function calls is a:
A) Queue
B) Tree
C) Linked List
D) Stack

### 20. In a Call Stack, which function call resolves (finishes) first?
A) The first one called (FIFO).
B) The last one called (LIFO).
C) They all resolve simultaneously.
D) The one with the smallest arguments.

### 21. If `def fact(n): return n * fact(n-1)` is called with `n=3` (assuming no base case), what is the next call?
A) `fact(4)`
B) `fact(2)`
C) `fact(3)`
D) It crashes immediately.

### 22. What is the base case for a recursive factorial function?
A) `if n == 0:` or `if n == 1:`
B) `if n < 0:`
C) `if n == 100:`
D) `if n % 2 == 0:`

### 23. What does `fib(n) = fib(n-1) + fib(n-2)` represent?
A) Factorial sequence
B) Fibonacci sequence
C) Anagram generation
D) Sorting algorithm

### 24. Why is naive recursive Fibonacci slow for large numbers?
A) Because addition is slow.
B) Because it uses too much memory.
C) Because it recalculates the same values multiple times (overlapping subproblems).
D) Because Python doesn't support recursion well.

### 25. What is the output of `" Python ".strip().upper()`?
A) `" PYTHON "`
B) `"PYTHON"`
C) `" python "`
D) `"python"`

### 26. Which method checks if a string ends with a specific suffix?
A) `.endswith()`
B) `.ends_with()`
C) `.check_end()`
D) `.suffix()`

### 27. How do you convert `"100"` to an integer?
A) `integer("100")`
B) `int("100")`
C) `str_to_int("100")`
D) `"100".to_int()`

### 28. If `d = {"a": 1}`, what does `d.get("b", 0)` return?
A) `1`
B) `0`
C) `KeyError`
D) `None`

### 29. Can recursion be used to traverse a list?
A) Yes, by passing the rest of the list (e.g., `lst[1:]`) in the recursive call.
B) No, recursion is only for math.
C) No, lists are immutable.
D) Yes, but only for lists of integers.

### 30. What does the string method `.title()` do?
A) Capitalizes every letter.
B) Capitalizes the first letter of the string only.
C) Capitalizes the first letter of every word.
D) Lowercases the string.

### 31. What is the output of `"a b c".split()`?
A) `["a b c"]`
B) `["a", "b", "c"]`
C) `("a", "b", "c")`
D) `TypeError`

### 32. Can a string be modified in-place using indexing (e.g. `s[0] = 'H'`)?
A) Yes
B) No, strings are immutable.

### 33. What is the maximum recursion depth in Python by default (approximately)?
A) 100
B) 1000
C) 10000
D) Infinite

### 34. How can you change the recursion limit in Python?
A) `sys.setrecursionlimit()`
B) `python.set_limit()`
C) `os.recursion_limit()`
D) You cannot change it.

### 35. What is the output of `bool("False")`?
A) `False`
B) `True` (because the string is not empty)
C) `None`
D) `Error`

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) Immutable**
2. **B) Converts the string to all lowercase and returns a new string.**
3. **C) `.strip()`**
4. **B) `["apple", "banana", "cherry"]`**
5. **C) `"-".join(["a", "b", "c"])`**
6. **C) `-1`**
7. **C) Returns the number of times "p" appears in the string.**
8. **B) `"hewwo"`**
9. **A) `.isnumeric()` or `.isdigit()`**
10. **B) A word formed by rearranging the letters of another word.**
11. **B) `True`**
12. **C) O(n log n)**
13. **C) Dictionary (Hash Map)**
14. **B) They cannot possibly be anagrams.**
15. **B) It returns the value for the key, or the default if the key doesn't exist.**
16. **C) It calls itself.**
17. **B) The condition that stops the recursion.**
18. **C) It causes an infinite loop and eventually a `RecursionError` (Stack Overflow).**
19. **D) Stack**
20. **B) The last one called (LIFO).**
21. **B) `fact(2)`**
22. **A) `if n == 0:` or `if n == 1:`**
23. **B) Fibonacci sequence**
24. **C) Because it recalculates the same values multiple times (overlapping subproblems).**
25. **B) `"PYTHON"`**
26. **A) `.endswith()`**
27. **B) `int("100")`**
28. **B) `0`**
29. **A) Yes, by passing the rest of the list (e.g., `lst[1:]`) in the recursive call.**
30. **C) Capitalizes the first letter of every word.**
31. **B) `["a", "b", "c"]`**
32. **B) No, strings are immutable.**
33. **B) 1000**
34. **A) `sys.setrecursionlimit()`**
35. **B) `True` (because the string is not empty)**

</details>
