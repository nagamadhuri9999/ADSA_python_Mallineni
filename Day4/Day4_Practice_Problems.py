# Day 4 Practice Problems: String Methods, Anagrams, and Recursion
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_string_lower():
    # TODO: Convert the string "PyThOn" to fully lowercase.
    pass

    # --- SOLUTION ---
    # text = "PyThOn"
    # print(text.lower())


def problem_2_string_upper():
    # TODO: Convert the string "hello" to fully uppercase.
    pass

    # --- SOLUTION ---
    # text = "hello"
    # print(text.upper())


def problem_3_string_strip():
    # TODO: Remove the extra spaces from "   data   ".
    pass

    # --- SOLUTION ---
    # text = "   data   "
    # print(text.strip())


def problem_4_string_replace():
    # TODO: Replace "bad" with "good" in "This is a bad idea".
    pass

    # --- SOLUTION ---
    # text = "This is a bad idea"
    # print(text.replace("bad", "good"))


def problem_5_string_split():
    # TODO: Split "apple,banana,cherry" into a list using the comma as a delimiter.
    pass

    # --- SOLUTION ---
    # text = "apple,banana,cherry"
    # print(text.split(","))


def problem_6_string_join():
    # TODO: Join the list ["A", "B", "C"] into a single string separated by dashes ("-").
    pass

    # --- SOLUTION ---
    # items = ["A", "B", "C"]
    # print("-".join(items))


def problem_7_string_find():
    # TODO: Find the index of the word "fox" in "The quick brown fox".
    pass

    # --- SOLUTION ---
    # text = "The quick brown fox"
    # print(text.find("fox"))


def problem_8_string_count():
    # TODO: Count how many times the letter "p" appears in "apple".
    pass

    # --- SOLUTION ---
    # text = "apple"
    # print(text.count("p"))


def problem_9_is_digit():
    # TODO: Check if the string "12345" consists only of digits using .isdigit().
    pass

    # --- SOLUTION ---
    # text = "12345"
    # print(text.isdigit())


def problem_10_anagram_sorting():
    # TODO: Write a function that takes two strings and returns True if they are anagrams using sorted().
    pass

    # --- SOLUTION ---
    # def is_anagram(s1, s2):
    #     return sorted(s1) == sorted(s2)
    # print(is_anagram("listen", "silent"))


def problem_11_anagram_frequency():
    # TODO: Write an anagram checker using a dictionary to count frequencies instead of sorting.
    pass

    # --- SOLUTION ---
    # def is_anagram_freq(s1, s2):
    #     if len(s1) != len(s2): return False
    #     counts = {}
    #     for char in s1:
    #         counts[char] = counts.get(char, 0) + 1
    #     for char in s2:
    #         if counts.get(char, 0) == 0: return False
    #         counts[char] -= 1
    #     return True


def problem_12_basic_recursion():
    # TODO: Write a recursive function 'print_down(n)' that prints from n down to 1.
    pass

    # --- SOLUTION ---
    # def print_down(n):
    #     if n <= 0: return
    #     print(n)
    #     print_down(n - 1)
    # print_down(3)


def problem_13_recursive_sum():
    # TODO: Write a recursive function to find the sum of numbers from 1 to n.
    pass

    # --- SOLUTION ---
    # def recursive_sum(n):
    #     if n <= 1: return 1
    #     return n + recursive_sum(n - 1)


def problem_14_recursive_factorial():
    # TODO: Write a recursive function to find the factorial of n (n!).
    pass

    # --- SOLUTION ---
    # def factorial(n):
    #     if n == 1: return 1
    #     return n * factorial(n - 1)


def problem_15_recursive_fibonacci():
    # TODO: Write a recursive function to find the nth Fibonacci number. (fib(0)=0, fib(1)=1)
    pass

    # --- SOLUTION ---
    # def fibonacci(n):
    #     if n <= 1: return n
    #     return fibonacci(n - 1) + fibonacci(n - 2)


def problem_16_recursive_power():
    # TODO: Write a recursive function to calculate base^exp (e.g., power(2, 3) = 8).
    pass

    # --- SOLUTION ---
    # def power(base, exp):
    #     if exp == 0: return 1
    #     return base * power(base, exp - 1)


def problem_17_palindrome_checker():
    # TODO: Write a function to check if a string is a palindrome. Use string methods to clean it first.
    pass

    # --- SOLUTION ---
    # def is_palindrome(s):
    #     cleaned = s.replace(" ", "").lower()
    #     return cleaned == cleaned[::-1]


def problem_18_vowel_counter():
    # TODO: Write a function that counts how many vowels are in a string using a loop and string methods.
    pass

    # --- SOLUTION ---
    # def count_vowels(s):
    #     count = 0
    #     for char in s.lower():
    #         if char in "aeiou": count += 1
    #     return count


def problem_19_title_case():
    # TODO: Convert "python is fun" to "Python Is Fun" using .title().
    pass

    # --- SOLUTION ---
    # text = "python is fun"
    # print(text.title())


def problem_20_starts_with():
    # TODO: Check if "Data Science" starts with "Data" using .startswith().
    pass

    # --- SOLUTION ---
    # text = "Data Science"
    # print(text.startswith("Data"))


if __name__ == "__main__":
    print("Welcome to Day 4 Practice Problems!")
    # problem_1_string_lower()
