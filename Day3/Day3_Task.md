# Day 3 Capstone Task: Text Analyzer

## Objective
Build a "Text Analyzer" program using functions, string slicing, and sequence methods. This will solidify your understanding of modular code and data extraction.

## Requirements

1. **Setup the Main Function:**
   - Define a function called `analyze_text(text)`.
   - All logic below should be placed inside this function.

2. **Count the Characters:**
   - Calculate and print the total length of the string using `len()`.

3. **Word Extraction (Lists):**
   - Use the string `.split()` method to break the text into a list of words.
   - Print the total number of words.
   - Print the *first* word and the *last* word using positive and negative indexing.

4. **Palindrome Check (Slicing):**
   - Check if the original text reads the same forwards and backwards.
   - *Hint:* First, remove spaces and convert the text to lowercase (e.g., `cleaned_text = text.replace(" ", "").lower()`).
   - Use slicing `[::-1]` to reverse the cleaned string and compare it to the original cleaned string.
   - Print whether it is a palindrome or not.

5. **Test Your Function:**
   - Call your function multiple times with different inputs.
   - Example 1: `analyze_text("Race car")`
   - Example 2: `analyze_text("Python is amazing")`

## Example Output for "Race car"
```text
--- Text Analysis ---
Total characters: 8
Total words: 2
First word: Race
Last word: car
Is Palindrome: True
```

Good luck!
