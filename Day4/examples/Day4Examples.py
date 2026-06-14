# Day 4 Examples: String Methods, Anagrams, and Advanced Recursion

# 1. String Methods
print("--- 1. String Methods ---")
text = "  Hello, Python World!  "
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Lower: '{text.lower()}'")
print(f"Upper: '{text.upper()}'")
print(f"Replace 'World' with 'Class': '{text.replace('World', 'Class')}'")
print(f"Find 'Python': {text.find('Python')}")
print(f"Count 'o': {text.lower().count('o')}")

input("\nPress Enter to see the next example...")

# 2. Split and Join
print("--- 2. Split and Join ---")
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")
print("Split into list:", fruits)
joined_string = " - ".join(fruits)
print("Joined back:", joined_string)

input("\nPress Enter to see the next example...")

# 3. Anagram Detection (Sorting)
print("--- 3. Anagram Detection (Sorting) ---")
def is_anagram_sort(s1, s2):
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    return sorted(s1_clean) == sorted(s2_clean)

word1 = "listen"
word2 = "silent"
print(f"Are '{word1}' and '{word2}' anagrams? {is_anagram_sort(word1, word2)}")

input("\nPress Enter to see the next example...")

# 4. Anagram Detection (Frequency Counting)
print("--- 4. Anagram Detection (Frequency Counting) ---")
def is_anagram_freq(s1, s2):
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    
    if len(s1_clean) != len(s2_clean):
        return False
        
    counts = {}
    for char in s1_clean:
        counts[char] = counts.get(char, 0) + 1
    
    for char in s2_clean:
        if char not in counts:
            return False
        counts[char] -= 1
        if counts[char] == 0:
            del counts[char]
            
    return len(counts) == 0

word3 = "Astronomer"
word4 = "Moon starer"
print(f"Are '{word3}' and '{word4}' anagrams? {is_anagram_freq(word3, word4)}")

input("\nPress Enter to see the next example...")

# 5. Recursion Dry Run Example (Factorial)
print("--- 5. Recursion Dry Run Example (Factorial) ---")
def fact(n):
    print(f"  Calling fact({n})")
    if n == 1:
        print(f"  Base case hit for fact({n}), returning 1")
        return 1
    result = n * fact(n - 1)
    print(f"  Returning {result} from fact({n})")
    return result

print("Starting fact(4):")
ans = fact(4)
print(f"Final answer: {ans}")

input("\nPress Enter to see the next example...")

# 6. Recursion Tree Example (Fibonacci)
print("--- 6. Recursion Tree Example (Fibonacci) ---")
# Using a global counter to show how many times the function is called
calls = 0
def fib(n):
    global calls
    calls += 1
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 5
print(f"Calculating fib({n})...")
fib_ans = fib(n)
print(f"fib({n}) is {fib_ans}")
print(f"Total function calls made: {calls}")
# For n=5, notice the number of calls is 15! This shows overlapping subproblems.

print("\n--- End of Examples ---")
