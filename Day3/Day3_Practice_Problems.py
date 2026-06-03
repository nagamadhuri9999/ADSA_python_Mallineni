# Day 3: 50 Basic Practice Problems and Solutions
# Topics: Strings, Lists, Loop Control, Functions, Scope, and Recursion

# ==========================================
# SECTION 1: STRING OPERATIONS (1 - 10)
# ==========================================

# 1. Print the first character of the string "Python".
s1 = "Python"
print("1.", s1[0])

# 2. Print the last character of the string "Data" using negative indexing.
s2 = "Data"
print("2.", s2[-1])

# 3. Slice the first 3 characters from "Programming".
s3 = "Programming"
print("3.", s3[0:3])

# 4. Reverse the string "Hello" using slicing.
s4 = "Hello"
print("4.", s4[::-1])

# 5. Concatenate "Good" and "Morning" with a space in between.
print("5.", "Good" + " " + "Morning")

# 6. Repeat the string "Hi" 4 times.
print("6.", "Hi" * 4)

# 7. Print the characters from index 2 to 5 in "Developer".
s7 = "Developer"
print("7.", s7[2:6])

# 8. Use negative slicing to get the last two characters of "World".
s8 = "World"
print("8.", s8[-2:])

# 9. Extract every second character from "abcdefgh".
s9 = "abcdefgh"
print("9.", s9[::2])

# 10. Check the length of the string "OpenAI" using len().
s10 = "OpenAI"
print("10.", len(s10))

# ==========================================
# SECTION 2: LIST OPERATIONS (11 - 20)
# ==========================================

# 11. Create a list of 3 colors and print the second color.
colors = ["Red", "Green", "Blue"]
print("11.", colors[1])

# 12. Print the last element of [10, 20, 30, 40] using negative indexing.
nums12 = [10, 20, 30, 40]
print("12.", nums12[-1])

# 13. Slice the middle two elements from [1, 2, 3, 4].
nums13 = [1, 2, 3, 4]
print("13.", nums13[1:3])

# 14. Reverse the list [1, 2, 3, 4, 5] using slicing.
nums14 = [1, 2, 3, 4, 5]
print("14.", nums14[::-1])

# 15. Concatenate two lists: [1, 2] and [3, 4].
print("15.", [1, 2] + [3, 4])

# 16. Extract the first 3 elements of [10, 20, 30, 40, 50].
nums16 = [10, 20, 30, 40, 50]
print("16.", nums16[:3])

# 17. Extract all elements except the first and last in [10, 20, 30, 40].
nums17 = [10, 20, 30, 40]
print("17.", nums17[1:-1])

# 18. Repeat the list [0] 5 times.
print("18.", [0] * 5)

# 19. Find the length of the list [5, 10, 15, 20, 25].
nums19 = [5, 10, 15, 20, 25]
print("19.", len(nums19))

# 20. Slice the last three elements of [1, 2, 3, 4, 5, 6].
nums20 = [1, 2, 3, 4, 5, 6]
print("20.", nums20[-3:])


# ==========================================
# SECTION 3: LOOP CONTROL & EXCEPTIONS (21 - 30)
# ==========================================

# 21. Write a for loop from 1 to 5, but break when reaching 3.
print("21.")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# 22. Write a for loop from 1 to 4, and skip 2 using continue.
print("22.")
for i in range(1, 5):
    if i == 2:
        continue
    print(i)

# 23. Create an empty for loop using pass.
for i in range(3):
    pass
print("23. Empty loop executed with pass.")

# 24. Write a while loop from 1 to 5, breaking if the number is 4.
print("24.")
w24 = 1
while w24 <= 5:
    if w24 == 4:
        break
    print(w24)
    w24 += 1

# 25. Use a while loop to print 1 to 4, but skip 3.
print("25.")
w25 = 0
while w25 < 4:
    w25 += 1
    if w25 == 3:
        continue
    print(w25)

# 26. Write an if-statement that uses pass.
if True:
    pass
print("26. If-statement executed with pass.")

# 27. Intentionally cause an IndexError and catch it with try/except.
print("27.")
try:
    print([1, 2][5])
except IndexError as e:
    print("Caught:", e)

# 28. Print characters in "Cat", break if 'a' is found.
print("28.")
for char in "Cat":
    if char == 'a':
        break
    print(char)

# 29. Print characters in "Dog", continue if 'o' is found.
print("29.")
for char in "Dog":
    if char == 'o':
        continue
    print(char)

# 30. Access a string out of bounds and catch IndexError.
print("30.")
try:
    print("Hi"[10])
except IndexError:
    print("String index out of range!")


# ==========================================
# SECTION 4: FUNCTIONS (31 - 40)
# ==========================================

# 31. Write a function that prints "Hello, World!" and call it.
print("31.")
def say_hello():
    print("Hello, World!")
say_hello()

# 32. Write a function that takes a name and prints a greeting.
print("32.")
def greet(name):
    print(f"Hi, {name}!")
greet("Venkatesh")

# 33. Write a function that returns the sum of two numbers.
print("33.")
def add(a, b):
    return a + b
print(add(5, 7))

# 34. Write a function with a default parameter for message.
print("34.")
def show_msg(msg="Default message"):
    print(msg)
show_msg()
show_msg("Custom message")

# 35. Write a function that returns the square of a number.
print("35.")
def square(n):
    return n * n
print(square(4))

# 36. Write a function that accepts *args and returns their sum.
print("36.")
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))

# 37. Write a function that accepts **kwargs and prints them.
print("37.")
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name="Alice", age=25)

# 38. Write a function with both positional and *args.
print("38.")
def show_first_and_rest(first, *rest):
    print("First:", first, "Rest:", rest)
show_first_and_rest(10, 20, 30, 40)

# 39. Write a function that returns the first character of a string.
print("39.")
def first_char(s):
    return s[0]
print(first_char("Python"))

# 40. Write a function that checks if a list is empty.
print("40.")
def is_empty(lst):
    return len(lst) == 0
print(is_empty([]))


# ==========================================
# SECTION 5: VARIABLE SCOPE (41 - 45)
# ==========================================

# 41. Define a global variable and access it inside a function.
print("41.")
g_var = 100
def access_global():
    print(g_var)
access_global()

# 42. Define a local variable and print it inside the function.
print("42.")
def access_local():
    l_var = 50
    print(l_var)
access_local()

# 43. Modify a global variable inside a function using the 'global' keyword.
print("43.")
count = 0
def increment():
    global count
    count += 1
increment()
print(count)

# 44. Create a local variable with the same name as a global variable.
print("44.")
x = "Global"
def shadow_var():
    x = "Local"
    print("Inside:", x)
shadow_var()
print("Outside:", x)

# 45. Demonstrate that a local variable is destroyed after function exits.
print("45.")
def temp_func():
    temp_var = 99
# temp_var is not accessible here
print("temp_var is only accessible inside temp_func")


# ==========================================
# SECTION 6: RECURSION (46 - 50)
# ==========================================

# 46. Write a recursive function to print numbers from N down to 1.
print("46.")
def countdown(n):
    if n <= 0:
        return
    print(n, end=" ")
    countdown(n - 1)
countdown(3)
print()

# 47. Write a recursive function to calculate the factorial of N.
print("47.")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(4))

# 48. Write a recursive function to find the sum of numbers from 1 to N.
print("48.")
def sum_n(n):
    if n <= 1:
        return 1
    return n + sum_n(n - 1)
print(sum_n(5))

# 49. Write a recursive function to find the Nth Fibonacci number.
print("49.")
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fib(5) =", fibonacci(5))

# 50. Write a recursive function to reverse a string.
print("50.")
def reverse_str(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse_str(s[:-1])
print(reverse_str("hello"))

# --- End of Practice Problems ---
