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
