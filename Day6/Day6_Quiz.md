# Day 6: Big O & Searching Algorithms Quiz

Test your knowledge of Day 6 concepts! Choose the best answer for each question.

---

### 1. What does Big O notation describe?
A) The exact time a program takes to run in seconds.
B) How the runtime or space requirements grow as the input size grows.
C) The size of the compiled program.
D) How many loops are in the code.

### 2. Which of the following represents Constant Time complexity?
A) O(n)
B) O(n^2)
C) O(1)
D) O(log n)

### 3. Which of the following represents Linear Time complexity?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 4. If an algorithm takes O(n^2) time, and the input size doubles, how does the time change?
A) It stays the same.
B) It doubles.
C) It quadruples (increases by 4x).
D) It halves.

### 5. Accessing an element in an array by its index (e.g., `arr[5]`) takes what time complexity?
A) O(1)
B) O(n)
C) O(log n)
D) O(n^2)

### 6. What is the time complexity of a standard Linear Search in the worst case?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 7. What is the best-case time complexity for Linear Search?
A) O(1) (if the target is the first element)
B) O(n)
C) O(log n)
D) O(n/2)

### 8. What is the defining characteristic of Binary Search?
A) It checks every element from left to right.
B) It divides the search interval in half at every step.
C) It uses recursion exclusively.
D) It sorts the array while searching.

### 9. What is the absolute prerequisite for using Binary Search?
A) The array must contain only positive numbers.
B) The array must be sorted.
C) The array must have an even length.
D) The array must not contain duplicates.

### 10. What is the worst-case time complexity of Binary Search?
A) O(1)
B) O(log n)
C) O(n)
D) O(n log n)

### 11. In Binary Search, if `arr[mid] < target`, what should happen next?
A) `right = mid - 1`
B) `left = mid + 1`
C) `left = mid - 1`
D) `right = mid + 1`

### 12. In Binary Search, if `arr[mid] > target`, what should happen next?
A) `right = mid - 1`
B) `left = mid + 1`
C) `left = mid - 1`
D) `right = mid + 1`

### 13. How is the `mid` index usually calculated in Python's binary search?
A) `mid = (left + right) / 2`
B) `mid = (left + right) // 2`
C) `mid = left + right`
D) `mid = len(arr) // 2`

### 14. What happens if Binary Search doesn't find the target?
A) The program crashes.
B) The `while left <= right:` loop terminates and we usually return `-1`.
C) It enters an infinite loop.
D) It returns the closest number.

### 15. If an array has 1,000,000 sorted elements, roughly how many steps does Binary Search take in the worst case?
A) 1,000,000
B) 500,000
C) ~20
D) 1

### 16. Which algorithm would you use to find a target in an unsorted array?
A) Binary Search
B) Linear Search
C) Quick Search
D) Hash Search

### 17. What is the space complexity of an iterative (while-loop) Binary Search?
A) O(1)
B) O(n)
C) O(log n)
D) O(n^2)

### 18. What is the space complexity of a Recursive Binary Search?
A) O(1)
B) O(n)
C) O(log n) (due to the Call Stack)
D) O(n^2)

### 19. If you have two nested loops (like generating all pairs), what is the time complexity?
A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

### 20. Which algorithm is generally faster for a sorted array of 1 million items?
A) Linear Search
B) Binary Search
C) They take the same time.
D) It depends on the programming language.

### 21. What happens if you run Binary Search on an unsorted array?
A) It works perfectly.
B) It throws a Compilation Error.
C) It may return incorrect results (fail to find the target).
D) It automatically sorts the array first.

### 22. What does `arr.index(target)` use under the hood in Python?
A) Binary Search
B) Linear Search
C) Hash Map lookup
D) Magic

### 23. If `left = 0` and `right = 4`, what is `mid` using `(left + right) // 2`?
A) `2`
B) `2.5`
C) `3`
D) `4`

### 24. If you drop the constants in O(2n + 5), what does the Big O notation become?
A) O(2n)
B) O(n + 5)
C) O(n)
D) O(1)

### 25. Why do we drop constants in Big O notation?
A) Because computers are fast.
B) Because Big O only cares about how the runtime scales with massive inputs.
C) Because constants are too hard to calculate.
D) Because Python ignores constants.

### 26. Searching for a key in a Python Dictionary (Hash Map) has an average time complexity of:
A) O(n)
B) O(n^2)
C) O(log n)
D) O(1)

### 27. When finding the first occurrence of a target in a sorted array with duplicates using Binary Search, what do you do when `arr[mid] == target`?
A) Return `mid` immediately.
B) Set `result = mid` and `left = mid + 1`.
C) Set `result = mid` and `right = mid - 1` to keep searching left.
D) Raise an error.

### 28. Which is better/faster: O(n) or O(log n)?
A) O(n)
B) O(log n)
C) They are the same.
D) It depends on the operating system.

### 29. Can Binary Search be applied to a sorted list of strings?
A) Yes, because strings can be compared lexicographically (alphabetically).
B) No, it only works on numbers.
C) Yes, but only if all strings are the same length.
D) No, lists of strings cannot be sorted.

### 30. What does the `in` operator (e.g., `5 in lst`) do on a Python List?
A) Performs a Binary Search.
B) Performs a Linear Search.
C) Performs an O(1) lookup.
D) Throws a syntax error.

### 31. If you must perform 10,000 searches on the same unsorted array of length 1,000,000, what is the best strategy?
A) Do 10,000 linear searches.
B) Sort the array once (O(n log n)), then do 10,000 Binary Searches.
C) Convert it to a set/dictionary once, then do O(1) lookups.
D) Both B and C are much better than A.

### 32. What does `math.log2(1048576)` roughly equal?
A) 10
B) 20
C) 100
D) 1048576

### 33. In the worst case, Linear search examines how many elements?
A) `n/2`
B) `1`
C) `n`
D) `n^2`

### 34. What condition prevents an infinite loop in Binary Search?
A) `while True:`
B) `while left < right:`
C) `while left <= right:`
D) `while mid != target:`

### 35. If you search for `10` in `[1, 3, 5, 7]`, what will `left` and `right` eventually do?
A) `left` will become greater than `right`, terminating the loop.
B) `right` will become greater than `left`.
C) `mid` will become `None`.
D) The array will resize.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) How the runtime or space requirements grow as the input size grows.**
2. **C) O(1)**
3. **C) O(n)**
4. **C) It quadruples (increases by 4x).**
5. **A) O(1)**
6. **C) O(n)**
7. **A) O(1) (if the target is the first element)**
8. **B) It divides the search interval in half at every step.**
9. **B) The array must be sorted.**
10. **B) O(log n)**
11. **B) `left = mid + 1`**
12. **A) `right = mid - 1`**
13. **B) `mid = (left + right) // 2`**
14. **B) The `while left <= right:` loop terminates and we usually return `-1`.**
15. **C) ~20**
16. **B) Linear Search**
17. **A) O(1)**
18. **C) O(log n) (due to the Call Stack)**
19. **D) O(n^2)**
20. **B) Binary Search**
21. **C) It may return incorrect results (fail to find the target).**
22. **B) Linear Search**
23. **A) `2`**
24. **C) O(n)**
25. **B) Because Big O only cares about how the runtime scales with massive inputs.**
26. **D) O(1)**
27. **C) Set `result = mid` and `right = mid - 1` to keep searching left.**
28. **B) O(log n)**
29. **A) Yes, because strings can be compared lexicographically.**
30. **B) Performs a Linear Search.**
31. **D) Both B and C are much better than A.**
32. **B) 20**
33. **C) `n`**
34. **C) `while left <= right:`**
35. **A) `left` will become greater than `right`, terminating the loop.**

</details>
