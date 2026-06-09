
# --- fix_me_day1.py ---
# Debugging Exercise: Day 1
# This file contains several intentional errors. 
# Your task is to find them, fix them, and make the script run successfully!

print("Welcome to the Day 1 Debugging Challenge!)

# 1. Variable Assignment Errors
1st_name = "Alice"
last-name = "Smith"
print(f"User: {1st_name} {last-name}")

# 2. Data Type Errors
age = 25
message = "I am " + age + " years old."
print(message)

# 3. List Errors
favorite_colors = ["Red", "Blue", "Green"
print(favorite_colors)

# 4. Math and Operator Errors
# We want to calculate the average of 3 test scores
score1 = 80
score2 = 90
score3 = 100
average_score = score1 + score2 + score3 / 3
print(f"The average score is: {average_score}")

# 5. Logic error
# Check if the user is an adult
is_adult = Age >= 18
print("Is adult?", is_adult)

print("If you see this, you fixed all the errors! Great job!")


# --- sales_analysis.py ---
# sales_analysis.py
# A practical mini-project bringing variables, data types, and operators together.

# 1. Variables and Data Types Setup
shop_name = "Brew & Byte Cafe"         # String (str)
coffee_price = 4.50                    # Floating-point (float)
is_open_today = True                   # Boolean (bool)

# 2. Collections (Lists and Dictionaries)
# Daily sales quantities for Monday to Friday
daily_sales_cups = [120, 145, 130, 160, 200]
menu_prices = {
    "espresso": 3.00, 
    "latte": 4.50, 
    "cappuccino": 4.00
}

# 3. Arithmetic Operators
# Calculating totals and averages
total_cups_sold = sum(daily_sales_cups)
days_open = len(daily_sales_cups)
average_cups_per_day = total_cups_sold / days_open

# Calculate estimated total revenue assuming average price
estimated_revenue = total_cups_sold * coffee_price

# 4. Logical & Comparison Operators
# Did we meet our weekly goal of 700 cups?
weekly_goal = 700
goal_met = total_cups_sold >= weekly_goal

# Was it an exceptional week? (Revenue > 3000 OR average cups > 150)
is_exceptional_week = (estimated_revenue > 3000) or (average_cups_per_day > 150)

# 5. Outputting the results using Print statements
print("=" * 40)
print(f"--- Sales Report for {shop_name} ---")
print("=" * 40)

print(f"Status: {'Open' if is_open_today else 'Closed'}")
print(f"Total Cups Sold: {total_cups_sold} cups")
print(f"Average Cups/Day: {average_cups_per_day} cups")
print(f"Estimated Revenue: ${estimated_revenue}")

print("-" * 40)
print(f"Weekly Goal ({weekly_goal} cups) Met? : {goal_met}")
print(f"Was this an exceptional week?        : {is_exceptional_week}")
print("=" * 40)

