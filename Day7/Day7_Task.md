# Day 7 Capstone Task: The Leaderboard Organizer

## Objective
Build a program that takes an unsorted list of player scores and uses **Insertion Sort** to organize them into a descending leaderboard (highest score first). This will test your ability to adapt an algorithm and manipulate arrays in-place (O(1) Space Complexity).

## Requirements

1. **The Dataset:**
   - Define a list of unsorted integer scores.
   - Example: `scores = [45, 92, 12, 78, 92, 33, 88, 5]`

2. **The Sorting Function:**
   - Create a function `build_leaderboard(arr)`.
   - Implement the **Insertion Sort** algorithm inside this function.
   - **CRITICAL TWEAK:** Instead of sorting ascending (lowest to highest), you must modify the inner `while` loop condition to sort **descending** (highest to lowest).
   - The sort must happen *in-place*. Do not create a new list.

3. **The Formatter (Bonus):**
   - After the list is sorted, print the top 5 scores nicely formatted.
   - Handle the case where there might be fewer than 5 scores in the total list.

## Example Output
```text
Unsorted Scores: [45, 92, 12, 78, 92, 33, 88, 5]

Sorting...

--- TOP 5 LEADERBOARD ---
1st Place: 92 pts
2nd Place: 92 pts
3rd Place: 88 pts
4th Place: 78 pts
5th Place: 45 pts
```

Good luck! Remember how the `while` loop condition `key < arr[j]` determines the sort order. What happens if you change it to `key > arr[j]`?
