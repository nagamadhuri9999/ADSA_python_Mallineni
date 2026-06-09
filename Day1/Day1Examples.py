
# --- variables.py ---
<<<<<<< HEAD

=======
# variables.py
# This script is for practice and review of Python variables.

# 1. Basic Variable Assignment
# A variable is a container for storing data. Python infers the type automatically.
name = "Supriya"  # String
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


# --- datatypes.py ---
# datatypes.py
# This script is for practice and review of Python Data Types.

print("--- 1. Numeric Types ---")
items_count = 5          # int: whole numbers
product_price = 19.99    # float: decimal numbers
print(f"Items: {items_count} (Type: {type(items_count)})")
print(f"Price: {product_price} (Type: {type(product_price)})")

print("\n--- 2. String Type ---")
greeting = "Hello, Python!"
user_email = 'user@example.com'
print(f"Greeting: {greeting} (Type: {type(greeting)})")
# Strings can be combined (concatenation)
full_message = greeting + " Please contact " + user_email
print("Combined:", full_message)

print("\n--- 3. Boolean Type ---")
is_active = True
has_discount = False
print(f"Active: {is_active} (Type: {type(is_active)})")

print("\n--- 4. Collection Types ---")
# List: Ordered and mutable (changeable)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange") # modifying the list
print(f"List (fruits): {fruits}")

# Tuple: Ordered and immutable (unchangeable)
coordinates = (12.9716, 77.5946) # e.g., Bangalore coordinates
print(f"Tuple (coordinates): {coordinates}")

# Dictionary: Key-value pairs
user_profile = {
    "name": "Amit",
    "role": "Admin",
    "age": 30
}
print(f"Dictionary (user_profile): {user_profile}")
print(f"User's Role: {user_profile['role']}")

# Set: Unordered collection of unique items
unique_ids = {101, 102, 103, 101} # Notice the duplicate 101
print(f"Set (unique_ids - duplicates removed): {unique_ids}")

print("\n--- 5. Type Conversion ---")
# Converting string to integer and float
str_number = "100"
converted_int = int(str_number)
converted_float = float(str_number)

print(f"Original string: '{str_number}'")
print(f"As Integer: {converted_int} -> Now we can add: {converted_int + 50}")
print(f"As Float: {converted_float}")


# --- operators.py ---
# operators.py
# This script is for practice and review of Python Operators.

a = 15
b = 4

print("--- 1. Arithmetic Operators ---")
print(f"a = {a}, b = {b}")
print("Addition (+):", a + b)
print("Subtraction (-):", a - b)
print("Multiplication (*):", a * b)
print("Division (/):", a / b)         # Always returns a float
print("Integer Division (//):", a // b) # Drops the decimal part
print("Modulo/Remainder (%):", a % b)   # Remainder of division
print("Exponent (**):", a ** 2)       # a squared

print("\n--- 2. Comparison Operators ---")
# These return Boolean values (True or False)
print(f"Is a equal to b? (a == b): {a == b}")
print(f"Is a not equal to b? (a != b): {a != b}")
print(f"Is a greater than b? (a > b): {a > b}")
print(f"Is a less than or equal to 15? (a <= 15): {a <= 15}")

print("\n--- 3. Logical Operators ---")
# Used to combine conditional statements
credit_score = 750
income = 60000

# AND: True if BOTH conditions are true
is_eligible_loan = (credit_score > 700) and (income > 50000)
print(f"Eligible for loan (AND): {is_eligible_loan}")

# OR: True if AT LEAST ONE condition is true
has_guarantor = False
can_rent_apartment = (income > 60000) or has_guarantor
print(f"Can rent apartment (OR): {can_rent_apartment}")

# NOT: Reverses the boolean value
is_banned = False
print(f"Can access system (NOT banned): {not is_banned}")

print("\n--- 4. Assignment Operators ---")
counter = 10
print(f"Initial counter: {counter}")
counter += 5  # Same as: counter = counter + 5
print(f"After counter += 5: {counter}")
counter *= 2  # Same as: counter = counter * 2
print(f"After counter *= 2: {counter}")

print("\n--- 5. Membership Operators ---")
# Check if a sequence is present in an object
allowed_users = ["admin", "moderator", "superuser"]
current_user = "guest"

print(f"Users list: {allowed_users}")
print(f"Is '{current_user}' in allowed_users? {'in' in allowed_users}")
print(f"Is '{current_user}' NOT in allowed_users? {current_user not in allowed_users}")

