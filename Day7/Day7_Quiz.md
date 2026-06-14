# Day 7: Sorting Algorithms & Space Complexity Quiz

Test your knowledge of Day 7 concepts! Choose the best answer for each question.

---

### 1. What does Space Complexity measure?
A) How much hard drive space a program takes up.
B) How much extra working memory (RAM) an algorithm needs as the input grows.
C) How long the code takes to type.
D) The number of variables in the code.

### 2. If an algorithm modifies a list "in-place" without creating any new data structures, what is its Space Complexity?
A) O(1) Constant
B) O(n) Linear
C) O(n^2) Quadratic
D) O(log n) Logarithmic

### 3. If an algorithm creates a brand new copy of a list of size `n`, what is its Space Complexity?
A) O(1)
B) O(n)
C) O(log n)
D) O(n^2)

### 4. Which of the following defines Bubble Sort?
A) Finds the minimum element and puts it at the beginning.
B) Inserts elements one by one into a sorted portion.
C) Repeatedly compares adjacent elements and swaps them if they are in the wrong order.
D) Divides the array into halves recursively.

### 5. What is the worst-case Time Complexity of Bubble Sort?
A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

### 6. What happens after the FIRST pass of Bubble Sort?
A) The smallest element is at the beginning.
B) The largest element "bubbles" to the very end of the array.
C) The array is completely sorted.
D) Nothing happens.

### 7. How can Bubble Sort be optimized?
A) By using a hash map.
B) By stopping early if a full pass occurs with ZERO swaps.
C) By starting from the middle.
D) Bubble sort cannot be optimized.

### 8. What is the best-case Time Complexity of an optimized Bubble Sort (if the array is already sorted)?
A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

### 9. Which of the following defines Selection Sort?
A) Repeatedly swaps adjacent elements.
B) Finds the minimum element from the unsorted part and swaps it with the first unsorted element.
C) Builds a sorted array one element at a time.
D) Uses a "pivot" to divide the array.

### 10. Does Selection Sort have a fast best-case scenario if the array is already sorted?
A) Yes, it runs in O(n).
B) No, it still scans the entire unsorted part every time, resulting in O(n^2).
C) Yes, it runs in O(1).
D) It crashes if the array is sorted.

### 11. What is the Space Complexity of Selection Sort?
A) O(1)
B) O(n)
C) O(log n)
D) O(n^2)

### 12. Which of the following defines Insertion Sort?
A) Swaps adjacent elements repeatedly.
B) Finds the minimum and places it at the front.
C) Takes the next unsorted element and inserts it into its correct position within the already sorted part.
D) Merges two sorted arrays.

### 13. Which sorting algorithm simulates how most people sort playing cards in their hands?
A) Bubble Sort
B) Selection Sort
C) Insertion Sort
D) Quick Sort

### 14. What is the best-case Time Complexity of Insertion Sort (if the array is already sorted)?
A) O(1)
B) O(n)
C) O(n log n)
D) O(n^2)

### 15. In Insertion Sort, what happens if the current `key` is smaller than the elements before it?
A) It gets deleted.
B) The larger elements are shifted one position to the right to make room.
C) The array is reversed.
D) The algorithm terminates.

### 16. To find the SECOND maximum in an array without sorting, how many passes through the array are required?
A) 1 pass (O(n))
B) 2 passes (O(2n))
C) It requires nested loops (O(n^2)).
D) It cannot be done without sorting.

### 17. How do you extract elements at EVEN indices using a `for` loop?
A) `for i in range(len(arr)): if i % 2 == 0:`
B) `for i in range(0, len(arr), 2):`
C) Both A and B work, but B is more efficient.
D) None of the above.

### 18. What does `arr[1::2]` do using Python slicing?
A) Returns elements at even indices.
B) Returns elements at odd indices (1, 3, 5...).
C) Reverses the array.
D) Returns the first two elements.

### 19. How do you swap two variables `a` and `b` in Python without a temporary variable?
A) `a = b; b = a`
B) `a, b = b, a`
C) `swap(a, b)`
D) `a.swap(b)`

### 20. If you need to find the 3 largest elements in an array, what is the simplest approach in Python?
A) Write 3 separate `for` loops.
B) Sort the array in descending order and slice the first 3 elements (`sorted(arr, reverse=True)[:3]`).
C) Use Bubble Sort.
D) Use a dictionary.

### 21. Which sorting algorithm performs the MOST swaps in the worst case?
A) Selection Sort
B) Bubble Sort
C) Insertion Sort
D) They all perform the exact same number of swaps.

### 22. Which sorting algorithm performs the LEAST swaps (usually O(n) swaps)?
A) Selection Sort
B) Bubble Sort
C) Insertion Sort
D) Merge Sort

### 23. What is a "Stable" sort?
A) It never crashes.
B) It runs in O(1) space.
C) It maintains the relative order of elements with equal values.
D) It can sort strings and integers together.

### 24. Is Bubble Sort typically stable?
A) Yes, because we only swap if the left is strictly greater than the right (`>`).
B) No, it scrambles equal elements.

### 25. What happens if you use `<` instead of `>` in the `if` condition of Bubble Sort?
A) The array will be sorted in descending order.
B) The algorithm will infinite loop.
C) The array will remain unsorted.
D) It throws a SyntaxError.

### 26. In an array of size $N$, how many comparisons are made in the FIRST pass of Bubble Sort?
A) $N$
B) $N - 1$
C) $N / 2$
D) 1

### 27. Why does the inner loop of optimized Bubble Sort go up to `n - i - 1` instead of `n - 1`?
A) To avoid `IndexError`.
B) Because after `i` passes, the last `i` elements are already perfectly sorted at the end.
C) Because Python requires it.
D) To make the code look shorter.

### 28. In Selection Sort, what variable is constantly updated during the inner loop?
A) `max_val`
B) `min_idx` (the index of the minimum element found so far)
C) `swap_count`
D) `key`

### 29. In Insertion Sort, what happens to the element at `arr[i]` at the start of the outer loop?
A) It is deleted.
B) It is saved into a variable usually called `key`.
C) It is swapped immediately.
D) It is printed.

### 30. Which of these sorting algorithms is considered the BEST for a dataset that is ALREADY mostly sorted?
A) Selection Sort
B) Insertion Sort
C) Random Sort
D) Bubble Sort (unoptimized)

### 31. If you are asked to sort an array "in-place", what does that mean?
A) Do not return anything.
B) Do not use any temporary variables.
C) Do not allocate a new array; modify the original array (Space Complexity O(1)).
D) You must use a specific library.

### 32. What is the time complexity of the built-in Python `sorted()` function?
A) O(n)
B) O(n^2)
C) O(n log n) (It uses Timsort)
D) O(1)

### 33. Can you sort an array of strings using these sorting algorithms?
A) Yes, strings are compared lexicographically (alphabetically).
B) No, these only work for numbers.
C) Yes, but only Selection Sort works for strings.
D) No, strings are immutable.

### 34. What is the primary disadvantage of O(n^2) sorting algorithms?
A) They are too difficult to write.
B) They use too much memory.
C) They are extremely slow for large datasets.
D) They cannot sort negative numbers.

### 35. If you need to find the maximum value of elements located at perfect square indices (0, 1, 4, 9), what is the best loop structure?
A) `for i in range(len(arr)): if is_square(i):`
B) `i = 0; while i*i < len(arr): check arr[i*i]; i += 1`
C) `for i in arr:`
D) `while True:`

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) How much extra working memory (RAM) an algorithm needs as the input grows.**
2. **A) O(1) Constant**
3. **B) O(n)**
4. **C) Repeatedly compares adjacent elements and swaps them if they are in the wrong order.**
5. **D) O(n^2)**
6. **B) The largest element "bubbles" to the very end of the array.**
7. **B) By stopping early if a full pass occurs with ZERO swaps.**
8. **B) O(n)**
9. **B) Finds the minimum element from the unsorted part and swaps it.**
10. **B) No, it still scans the entire unsorted part every time, resulting in O(n^2).**
11. **A) O(1)**
12. **C) Takes the next unsorted element and inserts it into its correct position.**
13. **C) Insertion Sort**
14. **B) O(n)**
15. **B) The larger elements are shifted one position to the right to make room.**
16. **A) 1 pass (O(n))** (or B, but it can be done in 1 pass by tracking two variables simultaneously).
17. **C) Both A and B work, but B is more efficient.**
18. **B) Returns elements at odd indices (1, 3, 5...).**
19. **B) `a, b = b, a`**
20. **B) Sort the array in descending order and slice the first 3 elements.**
21. **B) Bubble Sort**
22. **A) Selection Sort** (It does at most O(n) swaps, though O(n^2) comparisons).
23. **C) It maintains the relative order of elements with equal values.**
24. **A) Yes, because we only swap if the left is strictly greater than the right (`>`).**
25. **A) The array will be sorted in descending order.**
26. **B) $N - 1$**
27. **B) Because after `i` passes, the last `i` elements are already perfectly sorted at the end.**
28. **B) `min_idx`**
29. **B) It is saved into a variable usually called `key`.**
30. **B) Insertion Sort** (It immediately realizes the element is in the right place and moves on).
31. **C) Do not allocate a new array; modify the original array (Space Complexity O(1)).**
32. **C) O(n log n)**
33. **A) Yes, strings are compared lexicographically (alphabetically).**
34. **C) They are extremely slow for large datasets.**
35. **B) `i = 0; while i*i < len(arr): check arr[i*i]; i += 1`**

</details>
