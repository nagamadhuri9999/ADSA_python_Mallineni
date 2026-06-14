# Day 4 Capstone Task: The Anagram Detective

## Objective
Build a program that takes a massive list of scrambled words and groups all the anagrams together. This will test your knowledge of string methods, sorting, and dictionary manipulation.

## Requirements

1. **Setup the Function:**
   - Define a function called `group_anagrams(words)`.
   - `words` will be a list of strings (e.g., `["eat", "tea", "tan", "ate", "nat", "bat"]`).

2. **The Dictionary:**
   - Create an empty dictionary called `anagram_groups`. This dictionary will use the "sorted version" of a word as the **key**, and a list of the actual words as the **value**.

3. **Processing the Words:**
   - Loop through each word in the `words` list.
   - For each word:
     - Sort the word to find its "canonical" form. Since `sorted("eat")` returns a list `['a', 'e', 't']`, you must use `"".join(sorted(word))` to turn it back into the string `"aet"`.
     - Check if this sorted string is already a key in `anagram_groups`.
     - If it is NOT, add it as a key with an empty list as its value.
     - Append the original word to the list associated with that key.

4. **Return the Results:**
   - Return just the values of the dictionary (using `anagram_groups.values()`) as a list of lists.

## Example Output
```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

# Expected Output:
# [
#   ["eat", "tea", "ate"],
#   ["tan", "nat"],
#   ["bat"]
# ]
```

## Bonus Challenge (Recursion)
Write a completely separate recursive function called `reverse_string_recursive(s)` that reverses a string without using slicing or loops. 
*(Hint: `return s[-1] + reverse_string_recursive(s[:-1])` ... don't forget the base case!)*
