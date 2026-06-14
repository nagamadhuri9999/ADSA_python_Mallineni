# Day 3 Practice Problems: Strings, Lists, and Functions
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_string_indexing():
    # TODO: Create a string 'word' = "Developer".
    # TODO: Print the first and last characters using positive and negative indexing.
    pass

    # --- SOLUTION ---
    # word = "Developer"
    # print(word[0], word[-1])


def problem_2_list_indexing():
    # TODO: Create a list 'nums' = [10, 20, 30, 40, 50].
    # TODO: Print the third item (30) using indexing.
    pass

    # --- SOLUTION ---
    # nums = [10, 20, 30, 40, 50]
    # print(nums[2])


def problem_3_string_slicing():
    # TODO: You have text = "PythonProgramming".
    # TODO: Extract and print the word "Python" using slicing.
    pass

    # --- SOLUTION ---
    # text = "PythonProgramming"
    # print(text[0:6])


def problem_4_list_slicing():
    # TODO: You have items = ["apple", "banana", "cherry", "date", "elderberry"].
    # TODO: Extract and print ["banana", "cherry", "date"] using slicing.
    pass

    # --- SOLUTION ---
    # items = ["apple", "banana", "cherry", "date", "elderberry"]
    # print(items[1:4])


def problem_5_slicing_steps():
    # TODO: You have numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].
    # TODO: Use slicing with a step to print all odd numbers: [1, 3, 5, 7, 9].
    pass

    # --- SOLUTION ---
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # print(numbers[1::2])


def problem_6_reverse_string():
    # TODO: Use negative step slicing to print the reverse of "hello".
    pass

    # --- SOLUTION ---
    # word = "hello"
    # print(word[::-1])


def problem_7_basic_function():
    # TODO: Define a function 'say_hello' that takes no parameters and prints "Hello, World!".
    # TODO: Call the function.
    pass

    # --- SOLUTION ---
    # def say_hello():
    #     print("Hello, World!")
    # say_hello()


def problem_8_function_with_parameters():
    # TODO: Define a function 'multiply' that takes two parameters 'a' and 'b'.
    # TODO: It should return the product of a and b. Call it with 5 and 4 and print the result.
    pass

    # --- SOLUTION ---
    # def multiply(a, b):
    #     return a * b
    # print(multiply(5, 4))


def problem_9_default_arguments():
    # TODO: Define a function 'greet' with parameter 'name' and 'msg' which defaults to "Welcome".
    # TODO: Print f"{msg}, {name}!". Call it once with only a name, and once with both.
    pass

    # --- SOLUTION ---
    # def greet(name, msg="Welcome"):
    #     print(f"{msg}, {name}!")
    # greet("Alice")
    # greet("Bob", "Good morning")


def problem_10_args():
    # TODO: Define a function 'sum_all' that takes *args.
    # TODO: Use the built-in sum() function to return the sum of all passed numbers.
    # TODO: Print sum_all(1, 2, 3, 4, 5).
    pass

    # --- SOLUTION ---
    # def sum_all(*args):
    #     return sum(args)
    # print(sum_all(1, 2, 3, 4, 5))


def problem_11_kwargs():
    # TODO: Define a function 'print_info' that takes **kwargs.
    # TODO: Iterate through kwargs.items() and print the key and value.
    # TODO: Call it with name="John", age=30.
    pass

    # --- SOLUTION ---
    # def print_info(**kwargs):
    #     for key, value in kwargs.items():
    #         print(f"{key}: {value}")
    # print_info(name="John", age=30)


def problem_12_global_scope():
    # TODO: Create a global variable 'counter' = 0.
    # TODO: Define a function that uses the 'global' keyword to increment 'counter' by 1.
    pass

    # --- SOLUTION ---
    # counter = 0
    # def increment():
    #     global counter
    #     counter += 1
    # increment()


def problem_13_list_concatenation():
    # TODO: You have list1 = [1, 2] and list2 = [3, 4].
    # TODO: Combine them into list3 without using the append method (use +).
    pass

    # --- SOLUTION ---
    # list1 = [1, 2]
    # list2 = [3, 4]
    # list3 = list1 + list2
    # print(list3)


def problem_14_string_repetition():
    # TODO: Use the '*' operator to print "Ha" 5 times consecutively.
    pass

    # --- SOLUTION ---
    # print("Ha" * 5)


def problem_15_function_calling_function():
    # TODO: Define 'square(x)' that returns x*x.
    # TODO: Define 'sum_of_squares(x, y)' that returns square(x) + square(y).
    pass

    # --- SOLUTION ---
    # def square(x):
    #     return x * x
    # def sum_of_squares(x, y):
    #     return square(x) + square(y)
    # print(sum_of_squares(3, 4))


def problem_16_return_vs_print():
    # TODO: Define 'add_print(a, b)' that prints a+b but returns None.
    # TODO: Define 'add_return(a, b)' that returns a+b.
    # Note the difference when you try to assign their results to a variable!
    pass

    # --- SOLUTION ---
    # def add_print(a, b):
    #     print(a + b)
    # def add_return(a, b):
    #     return a + b
    # res1 = add_print(2, 2)   # res1 is None
    # res2 = add_return(2, 2)  # res2 is 4


def problem_17_recursive_countdown():
    # TODO: Define a recursive function 'countdown(n)'.
    # TODO: Base case: if n <= 0, print "Blastoff!".
    # TODO: Recursive step: print n, then call countdown(n - 1).
    pass

    # --- SOLUTION ---
    # def countdown(n):
    #     if n <= 0:
    #         print("Blastoff!")
    #     else:
    #         print(n)
    #         countdown(n - 1)
    # countdown(3)


def problem_18_string_immutability():
    # TODO: Strings are immutable. Try to change text = "Cat" to "Bat" using indexing (text[0] = "B").
    # Watch it throw a TypeError. Then do it the right way using string concatenation or slicing.
    pass

    # --- SOLUTION ---
    # text = "Cat"
    # # text[0] = "B"  # Throws TypeError
    # text = "B" + text[1:]
    # print(text)


def problem_19_list_mutability():
    # TODO: Lists ARE mutable. Create nums = [1, 2, 3].
    # TODO: Change the first element to 99 using indexing. Print nums.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # nums[0] = 99
    # print(nums)


def problem_20_slice_assignment():
    # TODO: You have nums = [1, 2, 3, 4, 5].
    # TODO: Replace the sublist [2, 3] with [8, 9] using slice assignment.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3, 4, 5]
    # nums[1:3] = [8, 9]
    # print(nums)


if __name__ == "__main__":
    print("Welcome to Day 3 Practice Problems!")
    # problem_1_string_indexing()
