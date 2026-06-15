# Day 10 Practice Problems: Stacks
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

# ==========================================
# Problems 1-10: Stack Basics and Mechanics
# ==========================================

def problem_1_create_stack():
    # TODO: Create an empty stack (using a Python list) and push 'A', 'B', 'C' to it.
    pass

    # --- SOLUTION ---
    # stack = []
    # stack.append('A')
    # stack.append('B')
    # stack.append('C')
    # print(stack)


def problem_2_pop_stack():
    # TODO: Given `stack = [1, 2, 3]`, pop the top element and store it in a variable.
    pass

    # --- SOLUTION ---
    # stack = [1, 2, 3]
    # top_val = stack.pop()
    # print(top_val, stack)


def problem_3_peek_stack():
    # TODO: Given `stack = [10, 20, 30]`, access the top element WITHOUT removing it.
    pass

    # --- SOLUTION ---
    # stack = [10, 20, 30]
    # top_val = stack[-1]
    # print(top_val, stack)


def problem_4_check_empty():
    # TODO: Write a function `is_empty(stack)` that returns True if empty, False otherwise.
    pass

    # --- SOLUTION ---
    # def is_empty(stack):
    #     return len(stack) == 0


def problem_5_reverse_string_with_stack():
    # TODO: Use a stack to reverse the string "hello".
    pass

    # --- SOLUTION ---
    # s = "hello"
    # stack = []
    # for char in s:
    #     stack.append(char)
    # rev = ""
    # while stack:
    #     rev += stack.pop()
    # print(rev)


def problem_6_clear_stack():
    # TODO: Pop elements from `stack = [1, 2, 3, 4]` using a while loop until it's empty.
    pass

    # --- SOLUTION ---
    # stack = [1, 2, 3, 4]
    # while stack:
    #     stack.pop()


def problem_7_stack_size():
    # TODO: Write a function to return the number of elements in a stack.
    pass

    # --- SOLUTION ---
    # def get_size(stack):
    #     return len(stack)


def problem_8_bottom_element():
    # TODO: Without destroying the stack, return the bottom-most element of `stack = [5, 6, 7]`.
    pass

    # --- SOLUTION ---
    # stack = [5, 6, 7]
    # bottom = stack[0] # List indexing gives us this for free in Python!


def problem_9_search_stack():
    # TODO: Return True if `target` is in the stack, False otherwise.
    pass

    # --- SOLUTION ---
    # def search(stack, target):
    #     return target in stack


def problem_10_pop_n_elements():
    # TODO: Pop `n` elements off the top of the stack. Handle cases where `n > len(stack)`.
    pass

    # --- SOLUTION ---
    # def pop_n(stack, n):
    #     for _ in range(min(n, len(stack))):
    #         stack.pop()


# ==========================================
# Problems 11-20: Advanced Stack Applications
# ==========================================

def problem_11_valid_parentheses_simple():
    # TODO: Write a simple checker that returns True if a string has an equal number of '(' and ')'.
    # (Note: This doesn't check order, just counts)
    pass

    # --- SOLUTION ---
    # def simple_check(s):
    #     count = 0
    #     for ch in s:
    #         if ch == '(': count += 1
    #         elif ch == ')': count -= 1
    #     return count == 0


def problem_12_remove_adjacent_duplicates():
    # TODO: Given a string like "abbaca", remove adjacent duplicates to get "ca". Use a stack.
    pass

    # --- SOLUTION ---
    # def remove_duplicates(s):
    #     stack = []
    #     for ch in s:
    #         if stack and stack[-1] == ch:
    #             stack.pop()
    #         else:
    #             stack.append(ch)
    #     return "".join(stack)


def problem_13_decimal_to_binary():
    # TODO: Use a stack to convert an integer `n` to a binary string. 
    # (Hint: append `n % 2` to stack, then `n = n // 2`, then pop all).
    pass

    # --- SOLUTION ---
    # def to_binary(n):
    #     if n == 0: return "0"
    #     stack = []
    #     while n > 0:
    #         stack.append(str(n % 2))
    #         n //= 2
    #     res = ""
    #     while stack:
    #         res += stack.pop()
    #     return res


def problem_14_min_stack_concept():
    # TODO: Create a tuple-based stack `[(val, current_min)]` to track the minimum element in O(1) time.
    pass

    # --- SOLUTION ---
    # stack = []
    # val = 5
    # current_min = val if not stack else min(val, stack[-1][1])
    # stack.append((val, current_min))


def problem_15_monotonic_increasing_stack():
    # TODO: Build a stack where every pushed element forces strictly LARGER elements to pop.
    pass

    # --- SOLUTION ---
    # def build_mono(arr):
    #     stack = []
    #     for num in arr:
    #         while stack and stack[-1] > num:
    #             stack.pop()
    #         stack.append(num)
    #     return stack


def problem_16_browser_history():
    # TODO: Simulate visiting URLs. Push URLs to a stack. Write a function to go "back".
    pass

    # --- SOLUTION ---
    # history = []
    # history.append("google.com")
    # history.append("youtube.com")
    # current_page = history.pop() if history else None


def problem_17_evaluate_postfix_simple():
    # TODO: Given tokens `['2', '3', '+']`, use a stack to evaluate it to `5`.
    pass

    # --- SOLUTION ---
    # tokens = ['2', '3', '+']
    # stack = []
    # for t in tokens:
    #     if t == '+':
    #         stack.append(stack.pop() + stack.pop())
    #     else:
    #         stack.append(int(t))
    # print(stack[0])


def problem_18_sort_stack():
    # TODO: Sort a stack using a temporary secondary stack.
    pass

    # --- SOLUTION ---
    # def sort_stack(stack):
    #     temp_stack = []
    #     while stack:
    #         curr = stack.pop()
    #         while temp_stack and temp_stack[-1] > curr:
    #             stack.append(temp_stack.pop())
    #         temp_stack.append(curr)
    #     return temp_stack


def problem_19_next_greater_element_brute():
    # TODO: Given an array, find the next greater element for each item using a brute-force O(n^2) loop.
    pass

    # --- SOLUTION ---
    # def nge_brute(arr):
    #     res = [-1] * len(arr)
    #     for i in range(len(arr)):
    #         for j in range(i+1, len(arr)):
    #             if arr[j] > arr[i]:
    #                 res[i] = arr[j]
    #                 break
    #     return res


def problem_20_implement_stack_using_class():
    # TODO: Write a CustomStack class with push, pop, and peek methods.
    pass

    # --- SOLUTION ---
    # class CustomStack:
    #     def __init__(self):
    #         self.items = []
    #     def push(self, val):
    #         self.items.append(val)
    #     def pop(self):
    #         if not self.is_empty(): return self.items.pop()
    #     def peek(self):
    #         if not self.is_empty(): return self.items[-1]
    #     def is_empty(self):
    #         return len(self.items) == 0


if __name__ == "__main__":
    print("Welcome to Day 10 Practice Problems (Stacks)!")
