# Day 3: Strings, Lists, and Functions Quiz

Test your knowledge of Day 3 concepts! Choose the best answer for each question.

---

### 1. What does the index `-1` refer to in a Python sequence?
A) The first element
B) The last element
C) It throws an IndexError
D) The second element

### 2. If `word = "Python"`, what is `word[1:4]`?
A) `yth`
B) `ytho`
C) `Pyt`
D) `hon`

### 3. What happens if you try to access an index that is out of bounds (e.g., `word[100]`)?
A) It returns `None`
B) It returns an empty string
C) It raises an `IndexError`
D) It wraps around to the beginning

### 4. What is the output of `"Hello" + "World"`?
A) `"Hello World"`
B) `"HelloWorld"`
C) `["Hello", "World"]`
D) `TypeError`

### 5. What does the slice `[::-1]` do to a sequence?
A) Returns the last element
B) Removes the last element
C) Reverses the sequence
D) Throws an error

### 6. If `nums = [10, 20, 30, 40]`, what is `nums[:2]`?
A) `[10, 20, 30]`
B) `[10, 20]`
C) `[20, 30]`
D) `[30, 40]`

### 7. What is the output of `"Ha" * 3`?
A) `"Ha 3"`
B) `"HaHaHa"`
C) `["Ha", "Ha", "Ha"]`
D) `TypeError`

### 8. Which keyword is used to define a function in Python?
A) `function`
B) `def`
C) `fun`
D) `define`

### 9. What is the difference between an argument and a parameter?
A) They are exactly the same thing.
B) Parameters are in the definition; arguments are the values passed.
C) Arguments are in the definition; parameters are the values passed.
D) Parameters are only for numbers.

### 10. Can a function return multiple values in Python?
A) No, only one value is allowed.
B) Yes, by returning them separated by commas (it returns a Tuple).
C) Yes, but only if returning a List.
D) Yes, but only using multiple `return` statements.

### 11. What happens if a function doesn't have a `return` statement?
A) It returns `0`.
B) It returns `False`.
C) It returns `None`.
D) It raises a `SyntaxError`.

### 12. If `def greet(name="User"):`, what is `"User"`?
A) A keyword argument
B) A positional argument
C) A default argument
D) An arbitrary argument

### 13. What does `*args` do in a function definition?
A) Unpacks a dictionary.
B) Collects positional arguments into a Tuple.
C) Collects keyword arguments into a Dictionary.
D) Multiplies the arguments.

### 14. What does `**kwargs` do in a function definition?
A) Collects positional arguments into a Tuple.
B) Collects keyword arguments into a Dictionary.
C) Performs exponentiation.
D) It is illegal syntax.

### 15. True or False: Positional arguments must appear before keyword arguments in a function call.
A) True
B) False

### 16. What is "Local Scope"?
A) Variables defined anywhere in the file.
B) Variables defined inside a function.
C) Variables imported from another file.
D) Variables defined in a `for` loop.

### 17. Can a local variable have the same name as a global variable?
A) No, it throws a `NameError`.
B) Yes, and modifying the local one automatically modifies the global one.
C) Yes, the local variable "shadows" the global variable within the function.
D) No, Python will crash.

### 18. Which keyword allows you to modify a global variable inside a function?
A) `local`
B) `modify`
C) `global`
D) `external`

### 19. What is "Recursion"?
A) A function that loops forever using `while True`.
B) A function that calls another function.
C) A function that calls itself.
D) A function that returns a function.

### 20. What is essential for a recursive function to prevent an infinite loop?
A) A `while` loop
B) A `break` statement
C) A Base Case
D) A `continue` statement

### 21. What error do you get if recursion goes too deep without stopping?
A) `MemoryError`
B) `RecursionError`
C) `InfiniteLoopError`
D) `StackError`

### 22. Which sequence type is immutable (cannot be changed after creation)?
A) List
B) Dictionary
C) Set
D) String

### 23. If `word = "Cat"`, what happens if you try `word[0] = "B"`?
A) `word` becomes `"Bat"`
B) `word` becomes `"B Cat"`
C) It raises a `TypeError`
D) It raises a `SyntaxError`

### 24. How do you find the length of a string or list?
A) `.length()`
B) `.size()`
C) `len()`
D) `count()`

### 25. If `x = [1, 2, 3]`, what does `x.append(4)` do?
A) Creates a new list `[1, 2, 3, 4]`.
B) Adds `4` to the beginning of `x`.
C) Modifies `x` in-place to add `4` at the end.
D) Returns `[1, 2, 3, 4]` but leaves `x` unchanged.

### 26. What does `list.pop()` do if no index is provided?
A) Removes the first element.
B) Removes a random element.
C) Removes and returns the last element.
D) Clears the entire list.

### 27. What is slice assignment? (e.g., `nums[1:3] = [8, 9]`)
A) It inserts `[8, 9]` into the list as a nested list.
B) It replaces the elements at indices 1 and 2 with 8 and 9.
C) It throws an error.
D) It appends 8 and 9 to the end.

### 28. What is the output of `bool("")`?
A) `True`
B) `False`
C) `None`
D) `Error`

### 29. Can a function be passed as an argument to another function in Python?
A) Yes, functions are first-class objects.
B) No, only variables can be passed.
C) Yes, but only built-in functions.
D) No, that causes a `SyntaxError`.

### 30. What will `[1, 2] + [3, 4]` produce?
A) `[4, 6]`
B) `[[1, 2], [3, 4]]`
C) `[1, 2, 3, 4]`
D) `TypeError`

### 31. What is the output of `len("  hi  ")`?
A) 2
B) 4
C) 6
D) 0

### 32. Which method removes whitespace from the beginning and end of a string?
A) `.clean()`
B) `.strip()`
C) `.remove()`
D) `.trim()`

### 33. If `s = "hello"`, what does `s.upper()` return?
A) `"HELLO"`
B) `"Hello"`
C) It modifies `s` to be `"HELLO"` and returns `None`.
D) `TypeError`

### 34. What does the `.split()` method do to a string?
A) Cuts it in half.
B) Splits it into a list of substrings (defaulting by whitespace).
C) Splits it into a tuple of characters.
D) Joins it with another string.

### 35. What is the output of `"-".join(["A", "B", "C"])`?
A) `["A-B-C"]`
B) `"A-B-C"`
C) `"ABC-"`
D) `"-ABC"`

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) The last element**
2. **A) `yth`** (Start at index 1 'y', stop before index 4 'o').
3. **C) It raises an `IndexError`**
4. **B) `"HelloWorld"`**
5. **C) Reverses the sequence**
6. **B) `[10, 20]`**
7. **B) `"HaHaHa"`**
8. **B) `def`**
9. **B) Parameters are in the definition; arguments are the values passed.**
10. **B) Yes, by returning them separated by commas (it returns a Tuple).**
11. **C) It returns `None`.**
12. **C) A default argument**
13. **B) Collects positional arguments into a Tuple.**
14. **B) Collects keyword arguments into a Dictionary.**
15. **A) True**
16. **B) Variables defined inside a function.**
17. **C) Yes, the local variable "shadows" the global variable within the function.**
18. **C) `global`**
19. **C) A function that calls itself.**
20. **C) A Base Case**
21. **B) `RecursionError`**
22. **D) String**
23. **C) It raises a `TypeError`** (Strings do not support item assignment).
24. **C) `len()`**
25. **C) Modifies `x` in-place to add `4` at the end.**
26. **C) Removes and returns the last element.**
27. **B) It replaces the elements at indices 1 and 2 with 8 and 9.**
28. **B) `False`** (Empty strings are falsy).
29. **A) Yes, functions are first-class objects.**
30. **C) `[1, 2, 3, 4]`**
31. **C) 6**
32. **B) `.strip()`**
33. **A) `"HELLO"`** (Returns a new string, `s` remains unchanged).
34. **B) Splits it into a list of substrings (defaulting by whitespace).**
35. **B) `"A-B-C"`**

</details>
