# Day 5 Practice Problems: List Methods and Problem Solving
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

def problem_1_list_append():
    # TODO: Create an empty list 'nums'. Append 10, then append 20. Print the list.
    pass

    # --- SOLUTION ---
    # nums = []
    # nums.append(10)
    # nums.append(20)
    # print(nums)


def problem_2_list_extend():
    # TODO: You have lst1 = [1, 2] and lst2 = [3, 4]. Use .extend() to add lst2 to lst1.
    pass

    # --- SOLUTION ---
    # lst1 = [1, 2]
    # lst2 = [3, 4]
    # lst1.extend(lst2)
    # print(lst1)


def problem_3_list_insert():
    # TODO: You have fruits = ["apple", "cherry"]. Insert "banana" at index 1.
    pass

    # --- SOLUTION ---
    # fruits = ["apple", "cherry"]
    # fruits.insert(1, "banana")
    # print(fruits)


def problem_4_list_remove():
    # TODO: You have items = [1, 5, 1, 9]. Remove the FIRST occurrence of 1 using .remove().
    pass

    # --- SOLUTION ---
    # items = [1, 5, 1, 9]
    # items.remove(1)
    # print(items)


def problem_5_list_pop():
    # TODO: You have nums = [10, 20, 30]. Use .pop() to remove and print the last element.
    pass

    # --- SOLUTION ---
    # nums = [10, 20, 30]
    # last = nums.pop()
    # print(last, nums)


def problem_6_list_index():
    # TODO: Find the index of "cat" in animals = ["dog", "cat", "bird"].
    pass

    # --- SOLUTION ---
    # animals = ["dog", "cat", "bird"]
    # print(animals.index("cat"))


def problem_7_list_count():
    # TODO: Count how many times 5 appears in [5, 2, 5, 5, 1].
    pass

    # --- SOLUTION ---
    # nums = [5, 2, 5, 5, 1]
    # print(nums.count(5))


def problem_8_list_sort():
    # TODO: Sort the list [4, 1, 8, 3] in ascending order in-place.
    pass

    # --- SOLUTION ---
    # nums = [4, 1, 8, 3]
    # nums.sort()
    # print(nums)


def problem_9_list_reverse():
    # TODO: Reverse the list [1, 2, 3] in-place using .reverse().
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # nums.reverse()
    # print(nums)


def problem_10_map_input():
    # TODO: Assume user types "1 2 3". Write code to parse this into a list of integers [1, 2, 3].
    pass

    # --- SOLUTION ---
    # # raw = input()
    # raw = "1 2 3" # Simulated input
    # nums = list(map(int, raw.split()))
    # print(nums)


def problem_11_sum_list():
    # TODO: Write a loop to calculate the sum of [10, 20, 30] without using the built-in sum().
    pass

    # --- SOLUTION ---
    # nums = [10, 20, 30]
    # total = 0
    # for n in nums: total += n
    # print(total)


def problem_12_product_list():
    # TODO: Write a loop to calculate the product (multiplication) of [2, 3, 4].
    pass

    # --- SOLUTION ---
    # nums = [2, 3, 4]
    # prod = 1
    # for n in nums: prod *= n
    # print(prod)


def problem_13_sum_of_squares():
    # TODO: Calculate the sum of the squares of [1, 2, 3] -> (1^2 + 2^2 + 3^2)
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # total = 0
    # for n in nums: total += (n ** 2)
    # print(total)


def problem_14_frequency_count():
    # TODO: Write a loop to create a frequency dictionary for [1, 1, 2, 3, 3, 3].
    pass

    # --- SOLUTION ---
    # nums = [1, 1, 2, 3, 3, 3]
    # freq = {}
    # for n in nums:
    #     freq[n] = freq.get(n, 0) + 1
    # print(freq)


def problem_15_all_pairs():
    # TODO: Print all unique pairs from [1, 2, 3] using nested loops.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3]
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         print((nums[i], nums[j]))


def problem_16_list_clear():
    # TODO: You have lst = [1, 2, 3]. Empty it completely using a list method.
    pass

    # --- SOLUTION ---
    # lst = [1, 2, 3]
    # lst.clear()
    # print(lst)


def problem_17_min_max_loops():
    # TODO: Find the maximum value in [4, 9, 2, 7] using a loop, not the max() function.
    pass

    # --- SOLUTION ---
    # nums = [4, 9, 2, 7]
    # current_max = nums[0]
    # for n in nums:
    #     if n > current_max: current_max = n
    # print(current_max)


def problem_18_copy_list():
    # TODO: Create a shallow copy of lst1 = [1, 2, 3] into lst2. Append 4 to lst2. lst1 should NOT change.
    pass

    # --- SOLUTION ---
    # lst1 = [1, 2, 3]
    # lst2 = lst1.copy() # or lst1[:]
    # lst2.append(4)
    # print(lst1, lst2)


def problem_19_filter_evens():
    # TODO: Given nums = [1, 2, 3, 4, 5, 6], create a new list containing only the even numbers.
    pass

    # --- SOLUTION ---
    # nums = [1, 2, 3, 4, 5, 6]
    # evens = []
    # for n in nums:
    #     if n % 2 == 0: evens.append(n)
    # print(evens)


def problem_20_list_membership():
    # TODO: Check if 10 is inside the list [5, 10, 15] and print True or False.
    pass

    # --- SOLUTION ---
    # nums = [5, 10, 15]
    # print(10 in nums)


if __name__ == "__main__":
    print("Welcome to Day 5 Practice Problems!")
    # problem_1_list_append()
