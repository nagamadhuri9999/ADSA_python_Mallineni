<<<<<<< HEAD

=======
# variables.py
# This script is for practice and review of Python variables.

# 1. Basic Variable Assignment
# A variable is a container for storing data. Python infers the type automatically.
name = "riya"  # String
age = 25          # Integer
height = 5.6      # Float
is_student = True # Boolean

print("--- Basic Variables ---")
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# 2. Dynamic Typing and Reassignment
# Variables can be reassigned to new values, even of different types.
print("\n--- Reassignment ---")
x = 10
print("x starts as:", x)
x = "Now I am a string!"
print("x is reassigned to:", x)

# 3. Naming Conventions (Snake Case)
# Good practice: descriptive names with underscores.
total_sales_amount = 1500.50
user_first_name = "Rahul"

# Bad practice examples (commented out to prevent errors):
# 1st_name = "Rahul"  # Cannot start with a number
# first-name = "Rahul" # Cannot use hyphens
# class = "Python"    # Cannot use reserved keywords

# 4. Multiple Assignment
print("\n--- Multiple Assignment ---")
a, b, c = 1, 2, 3
print(f"a: {a}, b: {b}, c: {c}")

# Assigning the same value to multiple variables
x = y = z = 100
print(f"x: {x}, y: {y}, z: {z}")
>>>>>>> f94e5d3 (second update)
