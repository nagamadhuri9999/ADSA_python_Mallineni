# Day 3 Examples: Control Statements, Data Structures, and Functions

# 1. Loop Control Statements: break, continue, pass
print("--- 1. Loop Control Statements ---")
for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break     # Stop at 8
    print(i)

if True:
    pass # Placeholder

input("\nPress Enter to see the next example...")

# 2. IndexError Example
print("--- 2. IndexError Example ---")
text = "Python"
print("Length of text:", len(text))
try:
    print(text[10]) # This will cause an IndexError
except IndexError as e:
    print("Caught an IndexError:", e)

input("\nPress Enter to see the next example...")

# 3. String Indexing and Slicing
print("--- 3. String Indexing and Slicing ---")
word = "Education"
print(f"Word: {word}")
print("Positive Index 0:", word[0])
print("Negative Index -1:", word[-1])
print("Slicing [0:3]:", word[0:3])
print("Negative Slicing [-4:-1]:", word[-4:-1])
print("Reversing [::-1]:", word[::-1])

input("\nPress Enter to see the next example...")

# 4. String Concatenation and Repetition
print("--- 4. String Concatenation and Repetition ---")
greeting = "Hello"
name = "Alice"
print("Concatenation:", greeting + " " + name)
print("Repetition:", "Ha" * 3)

input("\nPress Enter to see the next example...")

# 5. List Indexing and Slicing
print("--- 5. List Indexing and Slicing ---")
numbers = [10, 20, 30, 40, 50, 60]
print(f"List: {numbers}")
print("Index 2:", numbers[2])
print("Negative Index -2:", numbers[-2])
print("Slicing [1:4]:", numbers[1:4])

input("\nPress Enter to see the next example...")

# 6. List Concatenation
print("--- 6. List Concatenation ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Combined List: {combined}")

input("\nPress Enter to see the next example...")

# 7. Basic Function and Default Arguments
print("--- 7. Basic Function and Default Arguments ---")
def greet_user(name, message="Welcome to the class!"):
    print(f"Hello {name}, {message}")

greet_user("Venkatesh")
greet_user("Bob", "Good morning!")

input("\nPress Enter to see the next example...")

# 8. *args and **kwargs
print("--- 8. *args and **kwargs ---")
def student_info(*args, **kwargs):
    print("Positional args (Tuple):", args)
    print("Keyword args (Dictionary):", kwargs)

student_info("Alice", "Math", 95, grade="A", status="Passed")

input("\nPress Enter to see the next example...")

# 9. Variable Scope
print("--- 9. Variable Scope ---")
global_var = 100

def scope_test():
    local_var = 50
    print("Inside function - Global:", global_var, "Local:", local_var)

scope_test()
# print(local_var)  # This would raise a NameError

input("\nPress Enter to see the next example...")

# 10. Recursion
print("--- 10. Recursion ---")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))

print("\n--- End of Examples ---")
