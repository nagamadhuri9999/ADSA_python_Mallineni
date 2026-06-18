# Day 10: 50 Questions and Answers on Sorting Algorithms

## General Sorting Concepts
**1. What is a sorting algorithm?**
An algorithm that puts elements of a list into an order (numerical or lexicographical).

**2. What is an "in-place" sorting algorithm?**
An algorithm that uses constant $O(1)$ extra space to produce the sorted output (e.g., Bubble Sort, Quick Sort, Heap Sort).

**3. What makes a sorting algorithm "stable"?**
A stable sort maintains the relative order of records with equal keys/values.

**4. Name 3 stable sorting algorithms.**
Merge Sort, Insertion Sort, Bubble Sort.

**5. Name 3 unstable sorting algorithms.**
Quick Sort, Heap Sort, Selection Sort.

**6. What is the lower bound time complexity for any comparison-based sorting algorithm?**
$O(N \log N)$.

**7. Is it possible to sort an array in $O(N)$ time?**
Yes, but only using non-comparison-based sorts like Radix Sort, Counting Sort, or Bucket Sort, assuming specific constraints on the input data.

**8. What is an adaptive sorting algorithm?**
An algorithm that takes advantage of existing order in its input to run faster. Insertion sort is adaptive; standard Merge Sort is not.

## Bubble, Selection, and Insertion Sort ($O(N^2)$)
**9. How does Bubble Sort work?**
It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

**10. What is the worst-case time complexity of Bubble Sort?**
$O(N^2)$.

**11. How can you optimize Bubble Sort?**
Add a boolean flag to track if any swaps occurred during a pass. If no swaps occur, the array is already sorted, allowing early termination (Adaptive).

**12. How does Selection Sort work?**
It divides the input into a sorted and an unsorted region, repeatedly finding the minimum element from the unsorted region and putting it at the end of the sorted region.

**13. Does Selection Sort perform many swaps?**
No, it performs exactly $O(N)$ swaps, making it useful when memory writing is costly.

**14. Is Selection Sort stable?**
By default, no. Swapping a minimum element from the right can disrupt the relative order of equal elements.

**15. How does Insertion Sort work?**
It builds the final sorted array one item at a time by taking elements from the unsorted part and inserting them into their correct position in the sorted part.

**16. When is Insertion Sort highly efficient?**
When the array is already mostly sorted (almost sorted), running in $O(N)$ time, or when the array size is very small.

## Merge Sort
**17. What algorithm paradigm does Merge Sort use?**
Divide and Conquer.

**18. What is the time complexity of Merge Sort?**
$O(N \log N)$ for Best, Average, and Worst cases.

**19. What is the space complexity of Merge Sort?**
$O(N)$ because of the auxiliary arrays used during the merge phase.

**20. Is Merge Sort an in-place sort?**
No, it requires $O(N)$ extra space.

**21. Why is Merge Sort preferred for Linked Lists?**
In linked lists, we can insert items in the middle in $O(1)$ extra space and $O(1)$ time, meaning we don't need the $O(N)$ auxiliary space required for arrays.

**22. How do you find the middle of a Linked List for Merge Sort?**
Using the slow and fast pointer (Tortoise and Hare) method.

## Quick Sort
**23. How does Quick Sort work?**
It picks a "pivot" element, partitions the array so smaller elements are to the left and larger to the right, and then recursively sorts the sub-arrays.

**24. What is the worst-case time complexity of Quick Sort?**
$O(N^2)$, which occurs when the pivot chosen is consistently the smallest or largest element (e.g., array is already sorted and we pick the first/last element as pivot).

**25. How do we avoid the $O(N^2)$ worst-case in Quick Sort?**
By using a randomized pivot or using the "Median of Three" method for choosing the pivot.

**26. What is the average-case time complexity of Quick Sort?**
$O(N \log N)$.

**27. Why is Quick Sort generally faster than Merge Sort in practice?**
Quick sort has excellent spatial locality (cache-friendly) because it does in-place sorting and accesses elements sequentially during partitioning.

**28. Is Quick Sort stable?**
No, standard Quick Sort is unstable due to the swapping during partitioning.

**29. What is the space complexity of Quick Sort?**
$O(\log N)$ on average for the recursion stack, $O(N)$ in the worst case.

## Heap Sort
**30. What data structure does Heap Sort use?**
A binary heap (typically a max-heap for sorting in ascending order).

**31. What are the two main phases of Heap Sort?**
1) Build a Max-Heap from the array. 2) Repeatedly extract the maximum element (root) and replace it with the last element, then heapify the root.

**32. What is the time complexity of building the heap?**
$O(N)$.

**33. What is the overall time complexity of Heap Sort?**
$O(N \log N)$ for all cases.

**34. Is Heap Sort stable?**
No, operations on the heap can alter the relative order of equivalent keys.

## Non-Comparison Based Sorts
**35. How does Counting Sort work?**
It counts the number of occurrences of each unique element, then uses arithmetic to calculate the position of each element in the sorted output.

**36. When should you use Counting Sort?**
When the range of input values (k) is not significantly greater than the number of elements (N).

**37. What is the time complexity of Counting Sort?**
$O(N + K)$ where K is the range of the input.

**38. How does Radix Sort work?**
It processes the keys digit by digit (starting from the least significant digit to most significant digit) using a stable sort (like counting sort) as a subroutine.

**39. What is the time complexity of Radix Sort?**
$O(d \times (N + K))$, where $d$ is the number of digits and $K$ is the base.

**40. How does Bucket Sort work?**
It distributes elements into a number of "buckets", sorts each bucket individually (often using insertion sort), and then concatenates the buckets.

## Practical & Advanced Questions
**41. What sorting algorithm does Python's `sort()` use?**
Timsort.

**42. What is Timsort?**
A hybrid, stable sorting algorithm derived from Merge Sort and Insertion Sort.

**43. Which algorithm is best if memory is extremely limited?**
Heap Sort, as it guarantees $O(N \log N)$ time with $O(1)$ auxiliary space.

**44. Which algorithm is best if you need a stable sort and have extra memory?**
Merge Sort.

**45. If the array is already sorted, which algorithm will perform the fastest?**
Insertion sort or optimized Bubble sort ($O(N)$).

**46. You are sorting a 10 GB file with only 1 GB of RAM. How do you do it?**
External Merge Sort. Divide the file into 10 chunks of 1 GB, sort them in memory using Quick Sort, save them to disk, and then merge the 10 sorted files.

**47. What is the difference between Internal and External sorting?**
Internal sorting happens entirely in RAM. External sorting involves data too large to fit in RAM, relying on external storage (like Hard Drives/SSDs).

**48. Can Quick Sort be implemented iteratively?**
Yes, by using an explicit stack data structure to store the subarray bounds instead of the recursive call stack.

**49. Why is Insertion Sort used for small arrays within advanced algorithms like Quick Sort and Timsort?**
Because its constant factors and overhead are very low, making it faster than $O(N \log N)$ algorithms for small $N$ (usually $N < 16$ or $N < 32$).

**50. How do you sort an array of 0s, 1s, and 2s in $O(N)$ time and $O(1)$ space?**
Using the Dutch National Flag algorithm (3-way partitioning).
