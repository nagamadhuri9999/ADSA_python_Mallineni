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
