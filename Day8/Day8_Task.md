# Day 8 Capstone Task: The E-commerce Sorter

## Objective
Build an application that takes a massive, unsorted list of e-commerce products and uses **Merge Sort** to organize them by price (from lowest to highest). This tests your ability to apply Divide and Conquer to complex data structures like dictionaries.

## Requirements

1. **The Dataset:**
   - Define a list of at least 8 product dictionaries.
   - Example: 
     ```python
     products = [
         {"name": "Laptop", "price": 999.99},
         {"name": "Mouse", "price": 25.50},
         {"name": "Keyboard", "price": 45.00},
         {"name": "Monitor", "price": 199.99},
         # ... add more
     ]
     ```

2. **The Sorting Function:**
   - Create a function `merge_sort_products(arr)`.
   - Implement the **Merge Sort** algorithm.
   - **CRITICAL TWEAK:** When you write the `merge(left, right)` helper function, you cannot simply compare `left[i] < right[j]`. You must compare the *prices* inside the dictionaries: `left[i]['price'] < right[j]['price']`.

3. **Integration:**
   - Print the unsorted catalog.
   - Call your function and store the result.
   - Loop through the sorted result and print each product nicely.

## Example Output
```text
--- UNSORTED CATALOG ---
Laptop - $999.99
Mouse - $25.50
Keyboard - $45.00
Monitor - $199.99

Sorting with Divide & Conquer...

--- SORTED CATALOG ---
Mouse - $25.50
Keyboard - $45.00
Monitor - $199.99
Laptop - $999.99
```

Good luck! Notice how easily Merge Sort scales, even when comparing complex objects!
