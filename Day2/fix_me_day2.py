# Debugging Exercise: Day 2
# This file contains intentional logic and syntax errors involving loops and conditionals.
# Find them and fix them!

print("Welcome to the Day 2 Debugging Challenge!")

# 1. Syntax error in if statement
temperature = 30
if temperature > 25
    print("It's a hot day!")
else:
    print("It's not too hot.")

# 2. Infinite Loop Error
# Warning: If you run this without fixing it, press Ctrl+C in your terminal to stop it!
count = 5
while count > 0:
    print("Countdown:", count)
    # Hint: Something is missing here that causes the loop to never end

# 3. Logic Error in loop range
# We want to print numbers from 1 to 5 (inclusive)
print("Numbers 1 to 5:")
for i in range(1, 5):
    print(i)

# 4. Indentation Error
# We want to print the multiplication table for 3
for j in range(1, 6):
result = 3 * j
print(f"3 x {j} = {result}")

# 5. Logic error in condition order
# We want to print "Fizz" for multiples of 3, "Buzz" for 5, and "FizzBuzz" for both (like 15).
# Right now, 15 is printing "Fizz". Fix the logic!
num = 15
if num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
elif num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
else:
    print(num)

print("If you see this and the outputs look correct, you fixed all the errors! Great job!")
