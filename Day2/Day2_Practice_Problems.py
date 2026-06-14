# Day 2 Practice Problems: Control Flow (Conditionals & Loops)
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_if():
    # TODO: Create a variable 'temperature' = 35.
    # TODO: Write an if statement that prints "It's a hot day!" if temperature is greater than 30.
    pass

    # --- SOLUTION ---
    # temperature = 35
    # if temperature > 30:
    #     print("It's a hot day!")


def problem_2_if_else():
    # TODO: Create a variable 'is_raining' = True.
    # TODO: If it's raining, print "Take an umbrella", else print "Enjoy the sun".
    pass

    # --- SOLUTION ---
    # is_raining = True
    # if is_raining:
    #     print("Take an umbrella")
    # else:
    #     print("Enjoy the sun")


def problem_3_elif():
    # TODO: Create a variable 'score' = 85.
    # TODO: if score >= 90 print "A", elif score >= 80 print "B", else print "C".
    pass

    # --- SOLUTION ---
    # score = 85
    # if score >= 90:
    #     print("A")
    # elif score >= 80:
    #     print("B")
    # else:
    #     print("C")


def problem_4_nested_if():
    # TODO: Create variables 'is_weekend' = True and 'has_money' = False.
    # TODO: If it's the weekend, check if you have money. If yes, print "Go to movies", else print "Stay home".
    # If not the weekend, print "Go to work".
    pass

    # --- SOLUTION ---
    # is_weekend = True
    # has_money = False
    # if is_weekend:
    #     if has_money:
    #         print("Go to movies")
    #     else:
    #         print("Stay home")
    # else:
    #     print("Go to work")


def problem_5_multiple_conditions():
    # TODO: Create 'age' = 25 and 'has_license' = True.
    # TODO: Print "Can drive" ONLY IF age is >= 18 AND has_license is True.
    pass

    # --- SOLUTION ---
    # age = 25
    # has_license = True
    # if age >= 18 and has_license:
    #     print("Can drive")


def problem_6_for_loop_range():
    # TODO: Use a for loop and range() to print numbers from 1 to 5 (inclusive).
    pass

    # --- SOLUTION ---
    # for i in range(1, 6):
    #     print(i)


def problem_7_for_loop_list():
    # TODO: Create a list 'fruits' = ["apple", "banana", "cherry"].
    # TODO: Use a for loop to print each fruit.
    pass

    # --- SOLUTION ---
    # fruits = ["apple", "banana", "cherry"]
    # for fruit in fruits:
    #     print(fruit)


def problem_8_for_loop_string():
    # TODO: Use a for loop to iterate over the string "Python" and print each letter on a new line.
    pass

    # --- SOLUTION ---
    # for letter in "Python":
    #     print(letter)


def problem_9_while_loop():
    # TODO: Create a variable 'count' = 3.
    # TODO: Use a while loop to print 'count' and decrement it by 1 as long as it is > 0.
    pass

    # --- SOLUTION ---
    # count = 3
    # while count > 0:
    #     print(count)
    #     count -= 1


def problem_10_break_statement():
    # TODO: Loop from 1 to 10 using for i in range(1, 11).
    # TODO: If i equals 5, break out of the loop immediately. Print 'i' in each iteration.
    pass

    # --- SOLUTION ---
    # for i in range(1, 11):
    #     if i == 5:
    #         break
    #     print(i)


def problem_11_continue_statement():
    # TODO: Loop from 1 to 5.
    # TODO: If the number is 3, use 'continue' to skip printing it. Print all other numbers.
    pass

    # --- SOLUTION ---
    # for i in range(1, 6):
    #     if i == 3:
    #         continue
    #     print(i)


def problem_12_nested_loops():
    # TODO: Create two lists: colors = ["red", "blue"] and items = ["car", "bike"].
    # TODO: Use a nested loop to print every combination (e.g., "red car").
    pass

    # --- SOLUTION ---
    # colors = ["red", "blue"]
    # items = ["car", "bike"]
    # for color in colors:
    #     for item in items:
    #         print(color, item)


def problem_13_sum_with_loop():
    # TODO: Create a variable 'total' = 0.
    # TODO: Use a for loop to add all numbers from 1 to 10 to 'total'. Print the final 'total'.
    pass

    # --- SOLUTION ---
    # total = 0
    # for i in range(1, 11):
    #     total += i
    # print(total)


def problem_14_even_numbers_range():
    # TODO: Use a for loop with a step size in range() to print all even numbers from 2 to 10.
    pass

    # --- SOLUTION ---
    # for i in range(2, 11, 2):
    #     print(i)


def problem_15_while_true():
    # TODO: Use a 'while True:' loop and a variable 'x' starting at 1.
    # TODO: Break out of the loop when 'x' reaches 4. Print 'x' and increment it each time.
    pass

    # --- SOLUTION ---
    # x = 1
    # while True:
    #     print(x)
    #     if x == 4:
    #         break
    #     x += 1


def problem_16_pattern_square():
    # TODO: Use a nested loop to print a 3x3 square of asterisks (*).
    pass

    # --- SOLUTION ---
    # for i in range(3):
    #     for j in range(3):
    #         print("*", end=" ")
    #     print()


def problem_17_pattern_triangle():
    # TODO: Use a loop to print a right-angle triangle of asterisks with 4 rows.
    # Row 1: 1 star. Row 4: 4 stars.
    pass

    # --- SOLUTION ---
    # for i in range(1, 5):
    #     print("*" * i)


def problem_18_loop_else():
    # TODO: Loop from 1 to 3. 
    # TODO: Add an 'else' block to the 'for' loop that prints "Loop finished without breaking".
    pass

    # --- SOLUTION ---
    # for i in range(1, 4):
    #     print(i)
    # else:
    #     print("Loop finished without breaking")


def problem_19_list_filtering():
    # TODO: You have nums = [1, 5, 8, 10, 15].
    # TODO: Use a for loop and an if statement to print ONLY numbers greater than 9.
    pass

    # --- SOLUTION ---
    # nums = [1, 5, 8, 10, 15]
    # for n in nums:
    #     if n > 9:
    #         print(n)


def problem_20_counting_vowels():
    # TODO: You have a string 'word' = "education".
    # TODO: Use a for loop to count how many vowels (a,e,i,o,u) are in the word. Print the final count.
    pass

    # --- SOLUTION ---
    # word = "education"
    # count = 0
    # for char in word:
    #     if char in "aeiou":
    #         count += 1
    # print(count)


if __name__ == "__main__":
    print("Welcome to Day 2 Practice Problems!")
    print("Fill in the code for each function and call them here to test your answers.")
    # problem_1_if()
