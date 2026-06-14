# Day 1 Practice Problems: Python Fundamentals, Variables, Data Types & Operators
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_basics():
    # TODO: Print "Hello, Python!" to the console
    pass

    # --- SOLUTION ---
    # print("Hello, Python!")


def problem_2_variables():
    # TODO: Create a variable called 'user_age' and set it to 25.
    # TODO: Create a variable called 'user_name' and set it to "Alice".
    # TODO: Print a message saying "Alice is 25 years old."
    pass

    # --- SOLUTION ---
    # user_age = 25
    # user_name = "Alice"
    # print(user_name, "is", user_age, "years old.")


def problem_3_datatypes():
    # TODO: Create a variable 'price' with the value 19.99
    # TODO: Use the built-in type() function to print the data type of 'price'
    pass

    # --- SOLUTION ---
    # price = 19.99
    # print(type(price))


def problem_4_type_casting():
    # TODO: You have a string variable: str_num = "50"
    # TODO: Convert it into an integer, add 10 to it, and print the result.
    str_num = "50"
    pass

    # --- SOLUTION ---
    # num = int(str_num)
    # result = num + 10
    # print(result)


def problem_5_arithmetic():
    # TODO: Calculate the total bill for 3 coffees.
    # Each coffee is $4.50. The tax is a flat $1.50.
    # Store the result in 'total_bill' and print it.
    pass

    # --- SOLUTION ---
    # coffee_price = 4.50
    # num_coffees = 3
    # tax = 1.50
    # total_bill = (coffee_price * num_coffees) + tax
    # print(total_bill)


def problem_6_modulo():
    # TODO: Create a variable 'number' and set it to 15.
    # TODO: Use the modulo operator (%) to find the remainder when 'number' is divided by 2.
    # Print the remainder.
    pass

    # --- SOLUTION ---
    # number = 15
    # remainder = number % 2
    # print(remainder)


def problem_7_lists():
    # TODO: Create a list named 'fruits' containing "apple", "banana", and "cherry".
    # TODO: Print the second item in the list ("banana").
    pass

    # --- SOLUTION ---
    # fruits = ["apple", "banana", "cherry"]
    # print(fruits[1])


def problem_8_dictionaries():
    # TODO: Create a dictionary named 'student' with keys "name" and "grade".
    # Set "name" to "John" and "grade" to "A".
    # TODO: Print the student's grade.
    pass

    # --- SOLUTION ---
    # student = {"name": "John", "grade": "A"}
    # print(student["grade"])


def problem_9_comparison():
    # TODO: You have a saved password "secret123" and an input password "secret123".
    # TODO: Create a variable 'is_match' that uses the equality operator (==) to compare them.
    # Print 'is_match'.
    saved_pwd = "secret123"
    input_pwd = "secret123"
    pass

    # --- SOLUTION ---
    # is_match = (saved_pwd == input_pwd)
    # print(is_match)


def problem_10_logical():
    # TODO: To get a discount, a customer must be a member (is_member = True)
    # AND must have spent over $50 (spent = 60).
    # TODO: Create a boolean variable 'gets_discount' using logical operators and print it.
    is_member = True
    spent = 60
    pass

    # --- SOLUTION ---
    # gets_discount = is_member and (spent > 50)
    # print(gets_discount)

def problem_11_string_formatting():
    # TODO: Use an f-string to print "My favorite language is Python." 
    # Use the variable provided below inside the f-string.
    language = "Python"
    pass

    # --- SOLUTION ---
    # print(f"My favorite language is {language}.")


def problem_12_string_methods():
    # TODO: Convert the string 'shout' to uppercase using a string method and print it.
    shout = "hello"
    pass

    # --- SOLUTION ---
    # print(shout.upper())


def problem_13_length():
    # TODO: Use a built-in function to print the number of characters in the word "Supercalifragilisticexpialidocious".
    word = "Supercalifragilisticexpialidocious"
    pass

    # --- SOLUTION ---
    # print(len(word))


def problem_14_tuples():
    # TODO: Create a tuple named 'coordinates' containing the numbers 10 and 20.
    # TODO: Try to assign the value 30 to the first element (index 0). Watch it fail! (Tuples are immutable)
    pass

    # --- SOLUTION ---
    # coordinates = (10, 20)
    # # coordinates[0] = 30 # This will raise a TypeError!


def problem_15_sets():
    # TODO: Create a set named 'unique_numbers' with the values: 1, 1, 2, 3, 3, 4.
    # Print the set. Notice how duplicates are automatically removed!
    pass

    # --- SOLUTION ---
    # unique_numbers = {1, 1, 2, 3, 3, 4}
    # print(unique_numbers)


def problem_16_swap():
    # TODO: Swap the values of 'a' and 'b' without using a third temporary variable.
    # Print 'a' and 'b' to verify they swapped.
    a = 100
    b = 200
    pass

    # --- SOLUTION ---
    # a, b = b, a
    # print(a, b)


def problem_17_assignment_operator():
    # TODO: Use the '+=' assignment operator to add 50 to 'score'. Print 'score'.
    score = 10
    pass

    # --- SOLUTION ---
    # score += 50
    # print(score)


def problem_18_membership_operator():
    # TODO: Check if the letter "z" is in the string "alphabet" using the 'in' operator.
    # Print the boolean result.
    word = "alphabet"
    pass

    # --- SOLUTION ---
    # print("z" in word)


def problem_19_identity_operator():
    # TODO: Create two variables: list1 = [1, 2] and list2 = [1, 2].
    # TODO: Use the 'is' operator to check if they are the exact same object in memory. Print the result.
    pass

    # --- SOLUTION ---
    # list1 = [1, 2]
    # list2 = [1, 2]
    # print(list1 is list2) # Returns False because they are two distinct lists in memory!


def problem_20_precedence():
    # TODO: Calculate the result of 10 + 5 * 2. 
    # TODO: Now use parentheses to force the addition to happen first. Print both results.
    pass

    # --- SOLUTION ---
    # print(10 + 5 * 2)       # Output: 20
    # print((10 + 5) * 2)     # Output: 30

def problem_21_string_slicing():
    # TODO: Create a variable 'text' = "Python Programming".
    # TODO: Slice the string to extract just the word "Python" and print it.
    pass

    # --- SOLUTION ---
    # text = "Python Programming"
    # print(text[0:6])


def problem_22_dict_keys():
    # TODO: You have a dictionary: car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    # TODO: Print only the keys of the dictionary.
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    pass

    # --- SOLUTION ---
    # print(car.keys())


def problem_23_dict_values():
    # TODO: Using the same 'car' dictionary, print only the values.
    car = {"brand": "Ford", "model": "Mustang", "year": 1964}
    pass

    # --- SOLUTION ---
    # print(car.values())


def problem_24_list_append():
    # TODO: Create a list 'colors' = ["red", "green"].
    # TODO: Add "blue" to the end of the list and print the list.
    pass

    # --- SOLUTION ---
    # colors = ["red", "green"]
    # colors.append("blue")
    # print(colors)


def problem_25_type_error():
    # TODO: Try to concatenate a string "Age: " and an integer 25 using the '+' operator.
    # TODO: Watch it fail! Fix it by converting the integer to a string first, then print it.
    pass

    # --- SOLUTION ---
    # # print("Age: " + 25) # This raises a TypeError!
    # print("Age: " + str(25))


def problem_26_boolean_math():
    # TODO: In Python, True is 1 and False is 0. 
    # TODO: Print the result of True + True.
    pass

    # --- SOLUTION ---
    # print(True + True) # Outputs 2


def problem_27_floor_division():
    # TODO: Calculate 10 divided by 3 using standard division (/) and print it.
    # TODO: Calculate 10 divided by 3 using floor division (//) and print it. Notice the difference!
    pass

    # --- SOLUTION ---
    # print(10 / 3)   # Outputs 3.3333333333333335
    # print(10 // 3)  # Outputs 3


def problem_28_exponentiation():
    # TODO: Calculate 2 to the power of 5 using the exponentiation operator (**) and print it.
    pass

    # --- SOLUTION ---
    # print(2 ** 5)   # Outputs 32


def problem_29_dynamic_typing():
    # TODO: Create a variable 'x' and assign it the integer 100.
    # TODO: Reassign 'x' to the string "Now I'm a string!" and print 'x'. This demonstrates dynamic typing.
    pass

    # --- SOLUTION ---
    # x = 100
    # x = "Now I'm a string!"
    # print(x)


def problem_30_string_repetition():
    # TODO: Use the multiplication operator (*) to print a string of 20 dashes ("-").
    pass

    # --- SOLUTION ---
    # print("-" * 20)

def problem_31_negative_indexing():
    # TODO: Create a list 'letters' = ["a", "b", "c", "d", "e"].
    # TODO: Use negative indexing to print the last element ("e") of the list.
    pass

    # --- SOLUTION ---
    # letters = ["a", "b", "c", "d", "e"]
    # print(letters[-1])


def problem_32_list_membership():
    # TODO: Create a list 'vowels' = ["a", "e", "i", "o", "u"].
    # TODO: Check if the letter "x" is in the 'vowels' list using 'in' and print the boolean result.
    pass

    # --- SOLUTION ---
    # vowels = ["a", "e", "i", "o", "u"]
    # print("x" in vowels)


def problem_33_delete_variable():
    # TODO: Create a variable 'temp_data' = 500.
    # TODO: Delete the variable using the 'del' keyword. 
    # Try printing it afterwards to see the NameError (comment out the print so the script runs).
    pass

    # --- SOLUTION ---
    # temp_data = 500
    # del temp_data
    # # print(temp_data) # This would raise a NameError


def problem_34_multiline_strings():
    # TODO: Create a multiline string using triple quotes (""") containing a short poem or message.
    # Print the multiline string.
    pass

    # --- SOLUTION ---
    # message = """This is a
    # multiline string
    # in Python!"""
    # print(message)


def problem_35_boolean_casting():
    # TODO: Use bool() to cast an empty string "" to a boolean and print it.
    # TODO: Use bool() to cast a non-empty string "Python" to a boolean and print it.
    pass

    # --- SOLUTION ---
    # print(bool(""))       # Outputs False
    # print(bool("Python")) # Outputs True


def problem_36_multiple_assignment():
    # TODO: Assign the values 10, 20, and 30 to variables x, y, and z in a single line of code.
    # Print x, y, and z.
    pass

    # --- SOLUTION ---
    # x, y, z = 10, 20, 30
    # print(x, y, z)


def problem_37_update_dictionary():
    # TODO: Create a dictionary 'user' = {"name": "Bob", "age": 30}.
    # TODO: Update the "age" key to 31 and print the updated dictionary.
    pass

    # --- SOLUTION ---
    # user = {"name": "Bob", "age": 30}
    # user["age"] = 31
    # print(user)


def problem_38_modify_list():
    # TODO: Create a list 'scores' = [80, 90, 100].
    # TODO: Modify the first element (index 0) to be 85 instead of 80. Print the list.
    pass

    # --- SOLUTION ---
    # scores = [80, 90, 100]
    # scores[0] = 85
    # print(scores)


def problem_39_id_function():
    # TODO: Create variables 'a' = 10 and 'b' = 10.
    # TODO: Print the memory identity of both variables using the id() function. They should be the same!
    pass

    # --- SOLUTION ---
    # a = 10
    # b = 10
    # print(id(a), id(b))


def problem_40_comparison_chaining():
    # TODO: Create a variable 'age' = 25.
    # TODO: Check if 'age' is between 18 and 30 (inclusive) by chaining comparison operators (e.g., 18 <= age <= 30).
    # Print the boolean result.
    pass

    # --- SOLUTION ---
    # age = 25
    # print(18 <= age <= 30)

def problem_41_none_type():
    # TODO: Create a variable 'empty_val' and assign it the special 'None' value.
    # Print the type of 'empty_val'.
    pass

    # --- SOLUTION ---
    # empty_val = None
    # print(type(empty_val))


def problem_42_list_length():
    # TODO: Create a list 'guests' = ["Alice", "Bob", "Charlie", "David"].
    # TODO: Use the len() function to print how many guests are in the list.
    pass

    # --- SOLUTION ---
    # guests = ["Alice", "Bob", "Charlie", "David"]
    # print(len(guests))


def problem_43_dict_get():
    # TODO: You have a dictionary 'config' = {"theme": "dark"}.
    # TODO: Use the .get() method to safely fetch the "font_size". It shouldn't crash if it doesn't exist!
    # Print the result.
    pass

    # --- SOLUTION ---
    # config = {"theme": "dark"}
    # print(config.get("font_size")) # Outputs None


def problem_44_string_replace_chaining():
    # TODO: You have string 'text' = "I like apples and apples".
    # TODO: Chain the .replace() method to replace "apples" with "bananas", and then "like" with "love".
    # Print the final string.
    pass

    # --- SOLUTION ---
    # text = "I like apples and apples"
    # final_text = text.replace("apples", "bananas").replace("like", "love")
    # print(final_text)


def problem_45_modulo_last_digit():
    # TODO: You have a number 'num' = 12345.
    # TODO: Use the modulo operator (%) to extract and print the very last digit of the number.
    pass

    # --- SOLUTION ---
    # num = 12345
    # print(num % 10) # Outputs 5


def problem_46_exponentiation_sqrt():
    # TODO: Calculate the square root of 64 using ONLY the exponentiation operator (**) and print it.
    pass

    # --- SOLUTION ---
    # print(64 ** 0.5) # Outputs 8.0


def problem_47_fstring_math():
    # TODO: Use an f-string to print the result of 5 + 7 directly inside the string.
    # Expected output: "5 + 7 is 12"
    pass

    # --- SOLUTION ---
    # print(f"5 + 7 is {5 + 7}")


def problem_48_list_slicing_reverse():
    # TODO: You have a list 'nums' = [1, 2, 3, 4, 5].
    # TODO: Use list slicing with a negative step to print the list in reverse order.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3, 4, 5]
    # print(nums[::-1])


def problem_49_single_element_tuple():
    # TODO: Create a tuple named 'single' containing just the number 99.
    # Hint: Without a comma, Python thinks it's just a number in parentheses!
    # Print the type of 'single' to verify it is a tuple.
    pass

    # --- SOLUTION ---
    # single = (99,)
    # print(type(single))


def problem_50_set_operations():
    # TODO: Create two sets: set_a = {1, 2, 3} and set_b = {3, 4, 5}.
    # TODO: Find the intersection (common items) using the '&' operator and print it.
    pass

    # --- SOLUTION ---
    # set_a = {1, 2, 3}
    # set_b = {3, 4, 5}
    # print(set_a & set_b)


def problem_51_isalnum():
    # TODO: Check if the string "Python3" contains only letters and numbers using .isalnum()
    # Print the boolean result.
    pass

    # --- SOLUTION ---
    # print("Python3".isalnum())


def problem_52_not_in_operator():
    # TODO: Check if the word "error" is NOT IN the string "All systems nominal."
    # Print the boolean result.
    pass

    # --- SOLUTION ---
    # print("error" not in "All systems nominal.")


def problem_53_inequality_operator():
    # TODO: You have 'a' = 10 and 'b' = 20.
    # TODO: Use the inequality operator (!=) to check if they are different and print the result.
    pass

    # --- SOLUTION ---
    # a = 10
    # b = 20
    # print(a != b)


def problem_54_floor_div_negative():
    # TODO: Calculate -10 divided by 3 using floor division (//) and print it.
    # Note how floor division rounds DOWN to the nearest integer!
    pass

    # --- SOLUTION ---
    # print(-10 // 3) # Outputs -4, not -3!


def problem_55_string_join():
    # TODO: You have a list of words: words = ["Python", "is", "awesome"]
    # TODO: Use the .join() method to combine them into a single string separated by spaces. Print it.
    pass

    # --- SOLUTION ---
    # words = ["Python", "is", "awesome"]
    # print(" ".join(words))


def problem_56_string_split():
    # TODO: You have a CSV string: data = "apple,banana,cherry"
    # TODO: Use the .split() method to break it into a list of fruits and print the list.
    pass

    # --- SOLUTION ---
    # data = "apple,banana,cherry"
    # print(data.split(","))


def problem_57_empty_list_bool():
    # TODO: Cast an empty list [] to a boolean using bool() and print it.
    # Empty sequences evaluate to False in Python!
    pass

    # --- SOLUTION ---
    # print(bool([])) # Outputs False


def problem_58_type_comparison():
    # TODO: Create a variable 'x' = 50.
    # TODO: Check if the type of 'x' is exactly equal to 'int' and print the result.
    pass

    # --- SOLUTION ---
    # x = 50
    # print(type(x) == int)


def problem_59_multi_variable_same_value():
    # TODO: Assign the value 0 to variables 'a', 'b', and 'c' in a single line of code.
    # Print 'a', 'b', and 'c'.
    pass

    # --- SOLUTION ---
    # a = b = c = 0
    # print(a, b, c)


def problem_60_short_circuit_logic():
    # TODO: Python stops evaluating 'and' / 'or' as soon as the result is known.
    # TODO: Print the result of (False and (10 / 0 == 0)). It won't crash!
    pass

    # --- SOLUTION ---
    # print(False and (10 / 0 == 0)) # Outputs False without raising ZeroDivisionError

if __name__ == "__main__":
    print("Welcome to Day 1 Practice Problems!")
    print("Fill in the code for each function and call them here to test your answers.")
    # problem_1_basics()
