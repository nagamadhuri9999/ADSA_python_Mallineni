# Day 8: Advanced Sorting & Divide and Conquer Quiz

Test your knowledge of Day 8 concepts! Choose the best answer for each question.

---

### 1. What is the fundamental concept behind the Divide and Conquer paradigm?
A) Solving the entire problem at once.
B) Breaking a problem into smaller subproblems, solving them, and combining the results.
C) Iterating through an array multiple times.
D) Using a hash map to store intermediate results.

### 2. Which of the following algorithms uses the Divide and Conquer approach?
A) Bubble Sort
B) Selection Sort
C) Merge Sort
D) Insertion Sort

### 3. What is a "Base Case" in recursion?
A) The condition that causes the function to stop calling itself.
B) The very first time the function is called.
C) The part of the function that runs fastest.
D) An error state.

### 4. What happens if a recursive function does NOT have a base case?
A) It runs perfectly but is slower.
B) It triggers a `RecursionError` (Stack Overflow).
C) It automatically guesses when to stop.
D) It returns `None`.

### 5. In Merge Sort, how small do we divide the array before we start merging?
A) Until it is size 1.
B) Until it is size 2.
C) Until it is divided exactly in half.
D) We don't divide it, we just merge it.

### 6. What is the Time Complexity of Merge Sort in the worst case?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(log n)

### 7. What is the Time Complexity of Merge Sort in the BEST case?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

### 8. What is the Space Complexity of Merge Sort?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 9. Why does Merge Sort require O(n) space?
A) Because of the recursive call stack.
B) Because it requires creating new temporary arrays during the merge step.
C) Because it uses a hash map.
D) It doesn't; Merge Sort is O(1) space.

### 10. Is Merge Sort considered a Stable sorting algorithm?
A) Yes, equal elements retain their original relative order.
B) No, it scrambles equal elements.

### 11. In Quick Sort, what is a "Pivot"?
A) The array being sorted.
B) An element chosen to divide the array into elements smaller than it and larger than it.
C) The final merged array.
D) The middle index of the array.

### 12. What is the BEST/AVERAGE Time Complexity of Quick Sort?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

### 13. What is the WORST-CASE Time Complexity of Quick Sort?
A) O(n log n)
B) O(n^2)
C) O(n^3)
D) O(2^n)

### 14. When does the WORST-CASE scenario occur in Quick Sort (if using the first or last element as pivot)?
A) When the array is filled with random numbers.
B) When the array is already perfectly sorted or reverse-sorted.
C) When the array has an odd number of elements.
D) When the array contains negative numbers.

### 15. How can you avoid the worst-case scenario in Quick Sort?
A) Always pick the first element as the pivot.
B) Pick a random element as the pivot, or pick the median.
C) Use Bubble Sort instead.
D) You cannot avoid it.

### 16. What is the Space Complexity of Quick Sort (excluding the output array, just the call stack)?
A) O(1)
B) O(log n) on average.
C) O(n)
D) O(n^2)

### 17. Which is generally faster in practice for sorting arrays in memory: Merge Sort or Quick Sort?
A) Merge Sort
B) Quick Sort (despite its worst-case scenario).
C) They are identical in speed.
D) Bubble Sort.

### 18. Is Quick Sort typically stable?
A) Yes
B) No

### 19. If you are sorting a massive dataset that cannot fit into RAM (external sorting), which algorithm is preferred?
A) Quick Sort
B) Merge Sort
C) Bubble Sort
D) Selection Sort

### 20. What data structure does the computer use behind the scenes to manage recursive function calls?
A) Queue
B) Heap
C) Stack
D) Tree

### 21. If you have an array `arr = [5, 2, 9, 1, 5, 6]` and pivot is `5`, what elements go into the `left` array (elements < pivot)?
A) `[5, 5]`
B) `[2, 1]`
C) `[9, 6]`
D) `[5, 2, 1, 5]`

### 22. In the `merge(left, right)` step of Merge Sort, how many pointers are typically used?
A) 1
B) 2 (one for the `left` array, one for the `right` array).
C) 3
D) None

### 23. What does `arr.extend(left[i:])` do at the end of a merge function?
A) It crashes if `left` is empty.
B) It adds any remaining unmerged elements from `left` to the result list.
C) It deletes the elements.
D) It sorts the remaining elements.

### 24. Which Python built-in function sorts an array?
A) `arr.order()`
B) `arr.sort()` or `sorted(arr)`
C) `arr.organize()`
D) `sort(arr)`

### 25. Python's built-in `sort()` uses Timsort. What two algorithms is Timsort derived from?
A) Quick Sort and Bubble Sort
B) Merge Sort and Insertion Sort
C) Selection Sort and Quick Sort
D) Heap Sort and Merge Sort

### 26. Which of these algorithms is recursive by nature?
A) Bubble Sort
B) Selection Sort
C) Insertion Sort
D) Merge Sort

### 27. How does the call stack grow during a recursive function?
A) Linearly, proportional to the depth of the recursion.
B) Exponentially.
C) It doesn't grow.
D) It shrinks.

### 28. If an algorithm is O(n log n), what does the "log n" part usually represent?
A) The number of loops.
B) The number of times the data set can be halved (depth of a tree).
C) A constant multiplier.
D) The number of swaps.

### 29. Can Quick Sort be implemented to sort an array in-place (O(1) auxiliary space excluding the call stack)?
A) Yes, by swapping elements around the pivot.
B) No, it always requires O(n) new arrays.
C) Yes, but only for strings.
D) No, it requires O(n^2) space.

### 30. Which algorithm is best if you want a guaranteed worst-case time of O(n log n) and a stable sort?
A) Quick Sort
B) Merge Sort
C) Selection Sort
D) Heap Sort

### 31. What happens if you try to merge `[1, 5]` and `[2, 3]`?
A) You get `[1, 5, 2, 3]`
B) You get `[1, 2, 3, 5]`
C) An error occurs.
D) You get `[5, 3, 2, 1]`

### 32. In recursive calculating of factorial `fact(n)`, what is the base case?
A) `if n == 1: return 1`
B) `if n == 0: return 1`
C) Both A and B are acceptable.
D) `if n == n: return n`

### 33. Why do we say "Divide and Conquer" algorithms are generally efficient?
A) Because they use less memory.
B) Because halving a problem size drastically reduces the number of operations needed (Logarithmic efficiency).
C) Because they avoid using `if` statements.
D) Because they are iterative.

### 34. What is the value of `len(arr) // 2` for an array of size 7?
A) 3.5
B) 3
C) 4
D) 7

### 35. If you sort a list of dictionaries in Python using `sorted(data, key=lambda x: x['age'])`, what are you doing?
A) Throwing an error.
B) Sorting the dictionaries ascending by their 'age' value.
C) Sorting by the key names alphabetically.
D) Reversing the list.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) Breaking a problem into smaller subproblems, solving them, and combining the results.**
2. **C) Merge Sort**
3. **A) The condition that causes the function to stop calling itself.**
4. **B) It triggers a `RecursionError` (Stack Overflow).**
5. **A) Until it is size 1.**
6. **B) O(n log n)**
7. **B) O(n log n)**
8. **C) O(n)**
9. **B) Because it requires creating new temporary arrays during the merge step.**
10. **A) Yes, equal elements retain their original relative order.**
11. **B) An element chosen to divide the array into elements smaller than it and larger than it.**
12. **B) O(n log n)**
13. **B) O(n^2)**
14. **B) When the array is already perfectly sorted or reverse-sorted.**
15. **B) Pick a random element as the pivot, or pick the median.**
16. **B) O(log n) on average.**
17. **B) Quick Sort (despite its worst-case scenario).**
18. **B) No**
19. **B) Merge Sort**
20. **C) Stack**
21. **B) `[2, 1]`**
22. **B) 2 (one for the `left` array, one for the `right` array).**
23. **B) It adds any remaining unmerged elements from `left` to the result list.**
24. **B) `arr.sort()` or `sorted(arr)`**
25. **B) Merge Sort and Insertion Sort**
26. **D) Merge Sort**
27. **A) Linearly, proportional to the depth of the recursion.**
28. **B) The number of times the data set can be halved (depth of a tree).**
29. **A) Yes, by swapping elements around the pivot.**
30. **B) Merge Sort**
31. **B) You get `[1, 2, 3, 5]`**
32. **C) Both A and B are acceptable.**
33. **B) Because halving a problem size drastically reduces the number of operations needed.**
34. **B) 3**
35. **B) Sorting the dictionaries ascending by their 'age' value.**

</details>
