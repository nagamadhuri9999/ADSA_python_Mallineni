# Day 1: Python Basics, Variables, & Data Types Quiz

Test your knowledge of Day 1 concepts! Choose the best answer for each question.

---

### 1. Which of the following is a valid Python variable name?
A) `1st_number`
B) `first-number`
C) `first_number`
D) `first number`

### 2. What will the following code output?
```python
x = 10
y = "20"
print(x + y)
```
A) `30`
B) `1020`
C) A `TypeError`
D) `"30"`

### 3. Which data type is used to represent True or False values?
A) `int`
B) `str`
C) `bool`
D) `float`

### 4. What is the output of `15 // 4` in Python?
A) `3.75`
B) `3`
C) `4`
D) `15`

### 5. Which of the following collections is ordered and changeable (mutable)?
A) List
B) Tuple
C) Set
D) None of the above

### 6. What operator is used for exponentiation (power) in Python?
A) `^`
B) `**`
C) `//`
D) `%`

### 7. What does the modulo operator `%` return?
A) The quotient of a division
B) The remainder of a division
C) The percentage
D) The square root

### 8. What is the output of `"A" * 3`?
A) `AAA`
B) `A A A`
C) `3A`
D) `TypeError`

### 9. How do you convert the string `"10.5"` into a mathematical decimal?
A) `int("10.5")`
B) `dec("10.5")`
C) `float("10.5")`
D) `str("10.5")`

### 10. What does `bool([])` evaluate to?
A) `True`
B) `False`
C) `None`
D) `Error`

### 11. What does `bool(" ")` evaluate to? (A string containing a space)
A) `True`
B) `False`
C) `None`
D) `Error`

### 12. Are single quotes (`'`) and double quotes (`"`) treated differently for string creation in Python?
A) Yes, double quotes are for characters, single quotes for strings
B) Yes, single quotes are for characters, double quotes for strings
C) No, they are exactly the same
D) Double quotes allow multi-line strings, single quotes do not

### 13. Which syntax is used to create a multi-line string in Python?
A) `// string //`
B) `/* string */`
C) `''' string '''`
D) `-- string --`

### 14. What is the primary difference between a List and a Tuple?
A) Lists are ordered, Tuples are unordered
B) Lists can hold numbers, Tuples only strings
C) Lists use `()`, Tuples use `[]`
D) Lists are mutable, Tuples are immutable

### 15. In a Python Dictionary, which of the following is true?
A) Keys must be unique, values can be duplicated
B) Keys can be duplicated, values must be unique
C) Both keys and values must be unique
D) Both keys and values can be duplicated

### 16. What is the output of `print(set([1, 2, 2, 3, 3]))`?
A) `{1, 2, 2, 3, 3}`
B) `[1, 2, 3]`
C) `{1, 2, 3}`
D) `Error`

### 17. Which function is used to find the number of characters in a string?
A) `size()`
B) `count()`
C) `length()`
D) `len()`

### 18. What does `type(3.14)` return?
A) `<class 'float'>`
B) `<class 'int'>`
C) `<class 'double'>`
D) `<class 'decimal'>`

### 19. What is the difference between the `is` operator and the `==` operator?
A) `is` checks for value equality, `==` checks for memory identity
B) `is` checks for memory identity, `==` checks for value equality
C) They are exactly the same
D) `is` is used for numbers, `==` is used for strings

### 20. What does `"a" in "banana"` evaluate to?
A) `True`
B) `False`
C) `3`
D) `Error`

### 21. Which string method converts "hello" to "HELLO"?
A) `.uppercase()`
B) `.capitalize()`
C) `.upper()`
D) `.title()`

### 22. What does `"cat dog cat".replace("cat", "bird")` return?
A) `"bird dog cat"`
B) `"bird dog bird"`
C) `"cat dog bird"`
D) `"bird"`

### 23. Which method removes whitespace from the beginning and end of a string?
A) `.trim()`
B) `.strip()`
C) `.remove()`
D) `.cut()`

### 24. What does `True and False` evaluate to?
A) `True`
B) `False`
C) `None`
D) `1`

### 25. What does `True or False` evaluate to?
A) `True`
B) `False`
C) `None`
D) `1`

### 26. What does `not True` evaluate to?
A) `True`
B) `False`
C) `None`
D) `0`

### 27. What happens when you do `x = 10` and then `x = "Ten"` on the next line?
A) It causes a type error
B) It converts the integer `10` to the string `"Ten"`
C) The variable `x` simply points to the new string `"Ten"`
D) `x` becomes a list containing `10` and `"Ten"`

### 28. Which keyword is used to completely delete a variable from memory?
A) `remove`
B) `delete`
C) `del`
D) `erase`

### 29. In a dictionary `d = {"a": 1}`, what does `d.get("b")` return?
A) `1`
B) `None`
C) `False`
D) A `KeyError`

### 30. How do you add the item `"apple"` to the end of a list named `fruits`?
A) `fruits.add("apple")`
B) `fruits.insert("apple")`
C) `fruits.push("apple")`
D) `fruits.append("apple")`

### 31. What is the output of `"Python"[-1]`?
A) `P`
B) `y`
C) `n`
D) `o`

### 32. What is the output of `[10, 20, 30, 40][1:3]`?
A) `[10, 20]`
B) `[20, 30]`
C) `[20, 30, 40]`
D) `[10, 20, 30]`

### 33. What does `[1, 2, 3][::-1]` do?
A) Returns `[1, 2, 3]`
B) Returns `[3, 2, 1]`
C) Returns `[-1, -2, -3]`
D) Returns an error

### 34. What is the output of `10 + 5 * 2`?
A) `30`
B) `20`
C) `17`
D) `100`

### 35. How do you calculate the sum of all elements in the list `nums = [1, 2, 3]`?
A) `nums.total()`
B) `sum(nums)`
C) `nums.sum()`
D) `math.sum(nums)`

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **C) `first_number`**
2. **C) A `TypeError`** (Cannot add int and str directly).
3. **C) `bool`**
4. **B) `3`** (Floor division rounds down).
5. **A) List**
6. **B) `**`** (Exponentiation).
7. **B) The remainder of a division**
8. **A) `AAA`**
9. **C) `float("10.5")`**
10. **B) `False`** (Empty collections evaluate to False).
11. **A) `True`** (Non-empty strings, even just spaces, evaluate to True).
12. **C) No, they are exactly the same**
13. **C) `''' string '''`** (Triple quotes).
14. **D) Lists are mutable, Tuples are immutable**
15. **A) Keys must be unique, values can be duplicated**
16. **C) `{1, 2, 3}`** (Sets remove duplicates).
17. **D) `len()`**
18. **A) `<class 'float'>`**
19. **B) `is` checks for memory identity, `==` checks for value equality**
20. **A) `True`**
21. **C) `.upper()`**
22. **B) `"bird dog bird"`** (Replaces all occurrences).
23. **B) `.strip()`**
24. **B) `False`** (Both must be True).
25. **A) `True`** (Only one needs to be True).
26. **B) `False`**
27. **C) The variable `x` simply points to the new string `"Ten"`** (Dynamic typing).
28. **C) `del`**
29. **B) `None`** (`.get()` safely returns None instead of crashing with a KeyError).
30. **D) `fruits.append("apple")`**
31. **C) `n`** (Negative indices count from the back).
32. **B) `[20, 30]`** (Slicing is inclusive of the start, exclusive of the end).
33. **B) Returns `[3, 2, 1]`** (Step of -1 reverses the list).
34. **B) `20`** (Multiplication happens before addition).
35. **B) `sum(nums)`**

</details>
