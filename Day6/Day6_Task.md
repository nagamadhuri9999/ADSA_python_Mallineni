# Day 6 Capstone Task: The Phonebook Searcher

## Objective
Build a program that searches for a contact in a large, alphabetically sorted list of names using **Binary Search**. This will test your understanding of algorithmic efficiency and string comparisons.

## Requirements

1. **The Dataset:**
   - Define a list of at least 15 names, sorted alphabetically.
   - Example: `contacts = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Mallory", "Oscar", "Peggy", "Trent", "Victor", "Walter"]`

2. **The Search Function:**
   - Create a function `find_contact(contacts, target_name)`.
   - Implement the **Binary Search** algorithm inside this function using `left` and `right` pointers.
   - Remember that strings in Python can be compared using `<` and `>` (e.g., `"Alice" < "Bob"` is `True` because 'A' comes before 'B').

3. **Tracking Efficiency (Bonus):**
   - Add a counter variable inside your loop to track how many "steps" or "checks" the algorithm makes before finding the target (or realizing it's missing).
   - Print this step count.

4. **Integration:**
   - Prompt the user to input a name to search for.
   - Call the function.
   - If found, print the index and the number of steps it took.
   - If not found, print a message stating the contact is not in the phonebook.

## Example Output
```text
Phonebook loaded with 16 contacts.
Enter name to search: Heidi

Searching...
Target found at index 7!
It took 3 steps to find this contact.
```

Good luck! Notice how few steps it takes even if you make the list much larger!
