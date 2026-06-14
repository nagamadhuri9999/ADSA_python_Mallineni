# Day 9: Advanced Sorting Mechanics Quiz

Test your knowledge of Day 9 concepts! Choose the best answer for each question.

---

### 1. What problem does the QuickSelect algorithm solve?
A) Sorting an array as fast as possible.
B) Finding the K-th smallest or largest element in an unsorted array.
C) Merging two sorted arrays.
D) Counting inversions.

### 2. What is the average time complexity of QuickSelect?
A) O(log n)
B) O(n)
C) O(n log n)
D) O(n^2)

### 3. Why is QuickSelect faster than sorting the array to find the K-th element?
A) It uses a hash map.
B) It ignores the half of the array that cannot possibly contain the K-th element.
C) It runs on multiple threads.
D) It doesn't use recursion.

### 4. If you partition an array around a pivot, and the pivot ends up at index 5, what is the pivot's rank in the array?
A) It is the 5th smallest element (0-indexed).
B) It is the largest element.
C) It is the median.
D) We cannot know its rank.

### 5. In QuickSelect, if you are looking for the 7th smallest element (k=7) and the pivot ends up at index 4, where do you search next?
A) The left partition.
B) The right partition.
C) You return the pivot.
D) You sort the whole array.

### 6. What is the WORST-case time complexity of QuickSelect?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

### 7. Which partitioning scheme uses the last element as the pivot?
A) Hoare
B) Lomuto
C) Dijkstra
D) Floyd

### 8. Which partitioning scheme uses two pointers starting at opposite ends moving towards each other?
A) Hoare
B) Lomuto
C) Timsort
D) Merge

### 9. Which is generally considered more efficient in practice due to fewer swaps?
A) Hoare Partitioning
B) Lomuto Partitioning
C) They are identical in performance.
D) Neither; partitioning is inherently slow.

### 10. What is an "inversion" in an array?
A) When the array is reversed.
B) A pair of indices (i, j) where i < j but arr[i] > arr[j].
C) A pair of indices (i, j) where i < j and arr[i] < arr[j].
D) A negative number.

### 11. What does the number of inversions in an array indicate?
A) The length of the array.
B) How many negative numbers are present.
C) How far (or close) the array is from being fully sorted.
D) The maximum element.

### 12. If an array is perfectly sorted in ascending order, how many inversions does it have?
A) 0
B) 1
C) n/2
D) n^2

### 13. Which algorithm is best adapted to count inversions efficiently?
A) Bubble Sort
B) Selection Sort
C) Quick Sort
D) Merge Sort

### 14. What is the time complexity of counting inversions using the modified Merge Sort?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

### 15. In the inversion-counting Merge Sort, when is an inversion detected?
A) When left[i] <= right[j].
B) When right[j] < left[i] (an element from the right array is smaller than the current left element).
C) Only when the arrays are empty.
D) It is impossible to detect.

### 16. If `left = [3, 5]` and `right = [1, 4]`, when `1` is merged into the result, how many inversions are added?
A) 1
B) 2 (Because `1` is smaller than both `3` and `5`).
C) 3
D) 0

### 17. What algorithm does Python's `sort()` and `sorted()` use under the hood?
A) Pure Quick Sort
B) Pure Merge Sort
C) Timsort
D) Bubble Sort

### 18. Timsort is a hybrid of which two algorithms?
A) Quick Sort and Heap Sort
B) Merge Sort and Insertion Sort
C) Selection Sort and Bubble Sort
D) Quick Sort and Bubble Sort

### 19. Why does Timsort use Insertion Sort for small chunks?
A) Because it is easy to write.
B) Because Insertion Sort is incredibly fast on small or nearly-sorted arrays.
C) Because it uses O(n) space.
D) It doesn't; it uses Bubble Sort.

### 20. What is a "run" in the context of Timsort?
A) A sequence of elements that are already ordered.
B) A variable used in the loop.
C) The total execution time.
D) A memory leak.

### 21. What is the BEST-case time complexity of Timsort?
A) O(1)
B) O(n) (When the array is already sorted or reverse-sorted).
C) O(n log n)
D) O(n^2)

### 22. What is the WORST-case time complexity of Timsort?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(n^3)

### 23. Is Timsort a stable sorting algorithm?
A) Yes
B) No

### 24. What does the Master Theorem help us calculate?
A) The memory limit of a computer.
B) The time complexity of divide-and-conquer algorithms based on their recurrence relations.
C) The exact number of seconds a program will run.
D) Syntax errors.

### 25. The recurrence relation for Merge Sort is `T(n) = 2T(n/2) + O(n)`. What does the `O(n)` represent?
A) The time it takes to divide the array.
B) The time it takes to merge the two halves.
C) The base case.
D) A mistake.

### 26. In QuickSelect, if `k` is less than or equal to the size of the left partition, what happens?
A) We recursively search the right partition.
B) We recursively search the left partition.
C) We return the pivot.
D) The algorithm fails.

### 27. When finding the 5th smallest element, what is `k` using a 1-indexed approach?
A) 4
B) 5
C) 6
D) 0

### 28. If you want to find the K-th LARGEST element using QuickSelect, you can search for the ___-th smallest element.
A) K
B) N - K + 1
C) N / K
D) K + N

### 29. Can QuickSelect be done in-place?
A) Yes, by using an in-place partition scheme like Lomuto or Hoare.
B) No, it always requires O(n) space.
C) Yes, but only in Java.
D) No.

### 30. Which sorting algorithm is NOT comparison-based?
A) Merge Sort
B) Quick Sort
C) Counting Sort / Radix Sort
D) Insertion Sort

### 31. What is the theoretical lower bound time complexity for any comparison-based sorting algorithm?
A) O(n)
B) O(n log n)
C) O(n^2)
D) O(1)

### 32. If an array has `N` elements, what is the maximum number of inversions it can have (when reversed)?
A) N
B) N - 1
C) N * (N - 1) / 2
D) N^2

### 33. Why is Lomuto partition easier to implement than Hoare?
A) It uses complex math.
B) It only maintains one moving pointer and one index for the swap boundary.
C) It uses built-in functions.
D) It doesn't use a pivot.

### 34. In Hoare partitioning, what happens when the left and right pointers cross (`i >= j`)?
A) The partition is complete and `j` is returned as the partition index.
B) An error is thrown.
C) The array is sorted.
D) The pointers reset.

### 35. Which of the following is a real-world application of counting inversions?
A) Sorting a database alphabetically.
B) Measuring how similar two users' rankings of movies are (Collaborative Filtering).
C) Finding the shortest path in a graph.
D) Drawing graphics on a screen.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) Finding the K-th smallest or largest element in an unsorted array.**
2. **B) O(n)**
3. **B) It ignores the half of the array that cannot possibly contain the K-th element.**
4. **A) It is the 5th smallest element (0-indexed).**
5. **B) The right partition.**
6. **C) O(n^2)**
7. **B) Lomuto**
8. **A) Hoare**
9. **A) Hoare Partitioning**
10. **B) A pair of indices (i, j) where i < j but arr[i] > arr[j].**
11. **C) How far (or close) the array is from being fully sorted.**
12. **A) 0**
13. **D) Merge Sort**
14. **B) O(n log n)**
15. **B) When right[j] < left[i]**
16. **B) 2 (Because `1` is smaller than both `3` and `5`).**
17. **C) Timsort**
18. **B) Merge Sort and Insertion Sort**
19. **B) Because Insertion Sort is incredibly fast on small or nearly-sorted arrays.**
20. **A) A sequence of elements that are already ordered.**
21. **B) O(n)**
22. **B) O(n log n)**
23. **A) Yes**
24. **B) The time complexity of divide-and-conquer algorithms based on their recurrence relations.**
25. **B) The time it takes to merge the two halves.**
26. **B) We recursively search the left partition.**
27. **B) 5**
28. **B) N - K + 1**
29. **A) Yes, by using an in-place partition scheme like Lomuto or Hoare.**
30. **C) Counting Sort / Radix Sort**
31. **B) O(n log n)**
32. **C) N * (N - 1) / 2**
33. **B) It only maintains one moving pointer and one index for the swap boundary.**
34. **A) The partition is complete and `j` is returned as the partition index.**
35. **B) Measuring how similar two users' rankings of movies are.**

</details>
