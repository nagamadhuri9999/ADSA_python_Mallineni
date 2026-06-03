# Day 4: 50 Basic Practice Problems and Solutions
# Topics: String Methods, Anagrams, Recursion

# ==========================================
# SECTION 1: STRING METHODS (1 - 20)
# ==========================================

# 1. Convert the string "hello" to uppercase.
print("1.", "hello".upper())

# 2. Convert the string "WORLD" to lowercase.
print("2.", "WORLD".lower())

# 3. Remove the leading and trailing spaces from "  python  ".
print("3.", "  python  ".strip())

# 4. Remove the trailing spaces from "data   ".
print("4.", "data   ".rstrip())

# 5. Replace "cat" with "dog" in the string "The cat sat".
print("5.", "The cat sat".replace("cat", "dog"))

# 6. Split the string "a,b,c,d" by comma.
print("6.", "a,b,c,d".split(","))

# 7. Split the string "Hello World" by space.
print("7.", "Hello World".split())

# 8. Join the list ["a", "b", "c"] with a dash "-".
print("8.", "-".join(["a", "b", "c"]))

# 9. Find the index of "y" in "Python".
print("9.", "Python".find("y"))

# 10. Check if the string "12345" consists only of digits.
print("10.", "12345".isdigit())

# 11. Check if the string "hello" consists only of alphabetic characters.
print("11.", "hello".isalpha())

# 12. Count the number of 'a's in "banana".
print("12.", "banana".count("a"))

# 13. Convert "this is a title" to title case.
print("13.", "this is a title".title())

# 14. Check if "Hello World" starts with "Hello".
print("14.", "Hello World".startswith("Hello"))

# 15. Check if "report.pdf" ends with ".pdf".
print("15.", "report.pdf".endswith(".pdf"))

# 16. Replace all spaces in "a b c" with underscores.
print("16.", "a b c".replace(" ", "_"))

# 17. Find the index of 'z' in "hello". (Should return -1).
print("17.", "hello".find("z"))

# 18. Split the string "apple-orange-grape" by "-".
print("18.", "apple-orange-grape".split("-"))

# 19. Join ["I", "love", "Python"] with spaces.
print("19.", " ".join(["I", "love", "Python"]))

# 20. Count how many times "in" appears in "interesting".
print("20.", "interesting".count("in"))

# ==========================================
# SECTION 2: ANAGRAM LOGIC (21 - 30)
# ==========================================

# 21. Check if "cat" and "act" are anagrams using sorting.
print("21.", sorted("cat") == sorted("act"))

# 22. Check if "hello" and "olleh" are anagrams.
print("22.", sorted("hello") == sorted("olleh"))

# 23. Do "test" and "tast" match using sorting?
print("23.", sorted("test") == sorted("tast"))

# 24. Write a snippet to sort characters in the string "python".
print("24.", sorted("python"))

# 25. Check anagram ignoring spaces: "dormitory" and "dirty room".
s1 = "dormitory".replace(" ", "")
s2 = "dirty room".replace(" ", "")
print("25.", sorted(s1) == sorted(s2))

# 26. Count the frequency of characters in "apple" using a dictionary.
freq = {}
for char in "apple":
    freq[char] = freq.get(char, 0) + 1
print("26.", freq)

# 27. Compare character frequencies of "tea" and "eat".
freq1 = {'t':1, 'e':1, 'a':1}
freq2 = {'e':1, 'a':1, 't':1}
print("27.", freq1 == freq2)

# 28. If len(s1) != len(s2), can they be anagrams?
print("28.", "False, they must be the same length.")

# 29. Check anagram ignoring case: "Tea" and "Eat".
print("29.", sorted("Tea".lower()) == sorted("Eat".lower()))

# 30. How do you convert a sorted list of characters back to a string?
print("30.", "".join(sorted("apple")))

# ==========================================
# SECTION 3: RECURSION (31 - 50)
# ==========================================

# 31. Write a recursive function to print "Hello" N times.
print("31.")
def print_hello(n):
    if n == 0: return
    print("Hello", end=" ")
    print_hello(n-1)
print_hello(3); print()

# 32. Recursive function to find the sum of numbers from 1 to 5.
print("32.")
def sum_n(n):
    if n == 1: return 1
    return n + sum_n(n-1)
print(sum_n(5))

# 33. Factorial of 5 using recursion.
print("33.")
def fact(n):
    if n == 0 or n == 1: return 1
    return n * fact(n-1)
print(fact(5))

# 34. Fibonacci number at position 6 using recursion.
print("34.")
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
print(fib(6))

# 35. Recursive function to count down from 3 to 1.
print("35.")
def count_down(n):
    if n == 0: return
    print(n, end=" ")
    count_down(n-1)
count_down(3); print()

# 36. Recursive function to reverse a string "abc".
print("36.")
def rev_str(s):
    if len(s) == 0: return s
    return s[-1] + rev_str(s[:-1])
print(rev_str("abc"))

# 37. Recursive function to find the length of a string.
print("37.")
def str_len(s):
    if s == "": return 0
    return 1 + str_len(s[1:])
print(str_len("python"))

# 38. Recursive function to check if a string is a palindrome.
print("38.")
def is_pal(s):
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_pal(s[1:-1])
print(is_pal("radar"))

# 39. Count occurrences of a character in a string recursively.
print("39.")
def count_char(s, char):
    if not s: return 0
    return (1 if s[0] == char else 0) + count_char(s[1:], char)
print(count_char("apple", "p"))

# 40. Calculate 2^3 using recursion.
print("40.")
def power(base, exp):
    if exp == 0: return 1
    return base * power(base, exp-1)
print(power(2, 3))

# 41. Sum of elements in a list recursively.
print("41.")
def sum_list(lst):
    if not lst: return 0
    return lst[0] + sum_list(lst[1:])
print(sum_list([1, 2, 3, 4]))

# 42. Find the max element in a list recursively.
print("42.")
def max_list(lst):
    if len(lst) == 1: return lst[0]
    m = max_list(lst[1:])
    return lst[0] if lst[0] > m else m
print(max_list([1, 5, 3, 9, 2]))

# 43. Print elements of a list recursively.
print("43.")
def print_list(lst):
    if not lst: return
    print(lst[0], end=" ")
    print_list(lst[1:])
print_list([1,2,3]); print()

# 44. Print elements of a list in reverse order recursively.
print("44.")
def print_rev_list(lst):
    if not lst: return
    print_rev_list(lst[1:])
    print(lst[0], end=" ")
print_rev_list([1,2,3]); print()

# 45. Find GCD of two numbers using Euclidean algorithm recursively.
print("45.")
def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)
print(gcd(48, 18))

# 46. Check if an array is sorted recursively.
print("46.")
def is_sorted(lst):
    if len(lst) <= 1: return True
    if lst[0] > lst[1]: return False
    return is_sorted(lst[1:])
print(is_sorted([1, 2, 3, 4]))

# 47. Recursive function to multiply two numbers without using '*'.
print("47.")
def mult(a, b):
    if b == 0: return 0
    return a + mult(a, b-1)
print(mult(5, 4))

# 48. Print the binary representation of a number recursively.
print("48.")
def dec_to_bin(n):
    if n == 0: return
    dec_to_bin(n // 2)
    print(n % 2, end="")
dec_to_bin(10); print()

# 49. Check if a number is even recursively.
print("49.")
def is_even(n):
    if n == 0: return True
    if n == 1: return False
    return is_even(n - 2)
print(is_even(10))

# 50. Remove all vowels from a string recursively.
print("50.")
def rem_vowels(s):
    if not s: return ""
    first = "" if s[0].lower() in "aeiou" else s[0]
    return first + rem_vowels(s[1:])
print(rem_vowels("hello world"))

# --- End of Practice Problems ---
