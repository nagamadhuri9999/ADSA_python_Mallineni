# Day 3: Control Flow & Data Structures Quiz

Test your knowledge of Day 3 concepts! Choose the best answer for each question.

---

### 1. What is the output of the following code?
```python
for i in range(5):
    if i == 3:
        break
    print(i, end="")
```
A) `01234`
B) `0123`
C) `012`
D) `0124`

### 2. Which statement correctly reverses a string `s`?
A) `s.reverse()`
B) `s[::-1]`
C) `s[:-1]`
D) `s.reversed()`

### 3. What will this code output?
```python
def my_func(a, b=5):
    return a + b
print(my_func(2))
```
A) `5`
B) `7`
C) `Error`
D) `2`

### 4. What type of object does `*args` create inside a function?
A) List
B) Dictionary
C) Tuple
D) Set

### 5. Why is a base case necessary in recursion?
A) To speed up execution
B) To stop the recursive calls and prevent a RecursionError
C) To define global variables
D) To return multiple values

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **C) `012`** (The loop prints 0, 1, and 2. When `i` becomes 3, the `break` statement exits the loop before printing).
2. **B) `s[::-1]`** (This is the standard slicing technique to reverse a sequence in Python).
3. **B) `7`** (`a` gets the value 2. `b` defaults to 5. The sum is 7).
4. **C) Tuple** (`*args` collects extra positional arguments into a tuple).
5. **B) To stop the recursive calls and prevent a RecursionError** (Without a base case, the function would call itself infinitely until the call stack is exceeded).

</details>
