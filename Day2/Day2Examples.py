# Day 2 Examples: Control Flow and Loops

# 1. If / Elif / Else example
score = 85
if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
elif score > 60:
    print("D")
elif score > 50:
    print("E")
else:
    print("Try better next time")

# 2. Nested if example
number = 15
if number > 0:
    if number % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Zero or negative")

# 3. For loop with range
for i in range(1, 6):
    print(i)

# 4. For loop over a string
name = "Venkatesh"
for letter in name:
    print(letter)

# 5. While loop example
num = 1
while num <= 5:
    print(num)
    num += 1

# 6. Countdown using while
num = 10
while num >= 1:
    print(num)
    num -= 1

# 7. Nested loop example
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

# 8. Star pattern
for i in range(1, 5):
    print("* " * i)

# 9. FizzBuzz example
for num in range(1, 16):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

# 10. Nested for loops: multiplication table
for i in range(1, 5):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
    print()

# 11. Nested for loops: star square pattern with row and column control
size = 5
for row in range(size):
    for col in range(size):
        print("*", end=" ")
    print()

# 12. Nested conditions example
age = 20
has_permission = True
if age >= 18:
    if has_permission:
        print("Allowed to continue")
    else:
        print("Permission denied")
else:
    print("Too young")

# 13. Nested while loops: number grid using while
rows = 3
cols = 4
r = 1
while r <= rows:
    c = 1
    while c <= cols:
        print(f"{r},{c}", end=" ")
        c += 1
    print()
    r += 1

# 14. Nested while loops: star pattern with while
n = 4
outer = 1
while outer <= n:
    inner = 1
    while inner <= outer:
        print("*", end=" ")
        inner += 1
    print()
    outer += 1

# 15. Nested conditions inside loop for divisibility check
for num in range(1, 11):
    if num % 2 == 0:
        if num % 4 == 0:
            print(f"{num} is divisible by 4")
        else:
            print(f"{num} is even but not divisible by 4")
    else:
        print(f"{num} is odd")
