# Day 9 Capstone Task: The QuickSelector Median Finder

## Objective
Build a program that finds the **Median Salary** of a large list of employees using the **QuickSelect** algorithm. This tests your ability to find a specific element (the median) in $O(n)$ time without having to sort the entire array in $O(n \log n)$ time.

## Requirements

1. **The Dataset:**
   - Define an unsorted list of integer salaries. Ensure the length of the list is an **odd number** to make finding the median simpler (the exact middle element).
   - Example: `salaries = [45000, 120000, 30000, 75000, 60000, 50000, 90000]`

2. **The QuickSelect Function:**
   - Create a function `quickselect(arr, k)`.
   - Implement the QuickSelect algorithm.
   - It should recursively partition the array around a pivot and return the $K$-th smallest element.

3. **Integration:**
   - Determine what `k` should be to find the median of an odd-length array. (Hint: if `n = 7`, the median is the 4th smallest element).
   - Print the unsorted list of salaries.
   - Call `quickselect(salaries, k)` and print the result.
   
## Example Output
```text
Unsorted Salaries: [45000, 120000, 30000, 75000, 60000, 50000, 90000]

Finding the median (4th smallest) using QuickSelect...

Median Salary: $60000
```

Good luck! Notice how the algorithm ignores huge chunks of the array that it knows cannot contain the median.
