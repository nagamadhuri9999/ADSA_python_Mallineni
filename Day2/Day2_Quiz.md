# Day 2: Control Flow (Conditionals & Loops) Quiz

Test your knowledge of Day 2 concepts! Choose the best answer for each question.

---

### 1. Which keyword is used to start a conditional statement in Python?
A) `when`
B) `if`
C) `check`
D) `condition`

### 2. What keyword is used for "else if" in Python?
A) `elseif`
B) `else if`
C) `elif`
D) `elsif`

### 3. What will the following code print?
```python
x = 5
if x > 2:
    print("A")
elif x > 4:
    print("B")
else:
    print("C")
```
A) A
B) B
C) C
D) A and B

### 4. Can an `if` statement exist without an `else` statement?
A) Yes
B) No

### 5. What is required at the end of an `if`, `elif`, or `else` line?
A) Semicolon `;`
B) Colon `:`
C) Period `.`
D) Nothing

### 6. Which loop is best used when you know exactly how many times you want to iterate?
A) `while` loop
B) `do-while` loop
C) `for` loop
D) `until` loop

### 7. What will `range(5)` generate?
A) `1, 2, 3, 4, 5`
B) `0, 1, 2, 3, 4`
C) `0, 1, 2, 3, 4, 5`
D) `1, 2, 3, 4`

### 8. What is the output of `list(range(1, 10, 2))`?
A) `[1, 3, 5, 7, 9]`
B) `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
C) `[2, 4, 6, 8, 10]`
D) `[1, 3, 5, 7]`

### 9. Which loop repeats as long as a condition is True?
A) `for` loop
B) `while` loop
C) `repeat` loop
D) `until` loop

### 10. What happens if a `while` loop condition never becomes False?
A) It skips the loop
B) It runs 100 times and stops
C) It creates an infinite loop
D) It raises a SyntaxError

### 11. Which statement completely stops a loop and exits it?
A) `stop`
B) `exit`
C) `break`
D) `continue`

### 12. Which statement skips the rest of the current iteration and goes to the next iteration?
A) `skip`
B) `pass`
C) `next`
D) `continue`

### 13. What will this code print?
```python
for i in range(3):
    if i == 1:
        continue
    print(i, end="")
```
A) `012`
B) `02`
C) `12`
D) `0`

### 14. What does the `pass` keyword do in Python?
A) Skips the iteration
B) Stops the program
C) Does absolutely nothing (placeholder)
D) Reverses the loop

### 15. True or False: You can place a `for` loop inside another `for` loop.
A) True
B) False

### 16. In a nested loop setup (Outer loop runs 3 times, Inner runs 4 times), how many times does the inner body execute total?
A) 3
B) 4
C) 7
D) 12

### 17. Can a `while` loop have an `else` block in Python?
A) Yes, it runs when the condition becomes False (if not broken)
B) No, `else` is only for `if` statements
C) Yes, it runs only if the loop is broken
D) No, `else` is only for `for` loops

### 18. What is the output of the following?
```python
x = 0
while x < 3:
    print(x, end="")
    x += 1
```
A) `123`
B) `0123`
C) `012`
D) `Infinite loop`

### 19. What does the `end=" "` parameter do in the `print()` function?
A) Stops the program
B) Replaces the default newline with a space
C) Adds a space at the beginning of the string
D) Ends the loop

### 20. How do you print a string "Hello" 5 times on the same line?
A) `print("Hello" * 5)`
B) `print("Hello", 5)`
C) `print("Hello" + 5)`
D) `print("Hello^5")`

### 21. Which indentation is correctly applied in Python?
A) 2 spaces
B) 4 spaces
C) 1 tab
D) All are valid, but must be consistent within the block

### 22. What happens if you mix spaces and tabs for indentation in the same block?
A) It works perfectly
B) It raises an `IndentationError`
C) It converts tabs to spaces
D) It ignores the indentation

### 23. What will this code print?
```python
if False:
    print("A")
elif True:
    print("B")
elif True:
    print("C")
```
A) A
B) B
C) B and C
D) C

### 24. What is the value of `i` after this loop completes?
```python
for i in range(5):
    pass
```
A) `4`
B) `5`
C) `0`
D) `Undefined`

### 25. Which function is often used with `for` loops to iterate over a list while getting the index too?
A) `index()`
B) `enumerate()`
C) `count()`
D) `zip()`

### 26. What does `range(10, 0, -1)` produce?
A) `0 to 10`
B) `10 down to 1`
C) `10 down to 0`
D) `Error`

### 27. What happens if a `break` statement is executed inside a nested inner loop?
A) It stops both loops
B) It stops only the inner loop
C) It stops only the outer loop
D) It skips the iteration

### 28. What will this print?
```python
count = 0
while True:
    count += 1
    if count == 3:
        break
print(count)
```
A) 0
B) 2
C) 3
D) Infinite loop

### 29. Can you iterate over a string with a `for` loop?
A) Yes, it iterates character by character
B) Yes, it iterates word by word
C) No, strings are not iterable
D) Yes, but only if converted to a list first

### 30. What does the following pattern print?
```python
for i in range(2):
    for j in range(2):
        print("*", end="")
    print()
```
A) A 2x2 square of stars
B) A 2x4 rectangle
C) A single line of 4 stars
D) A right triangle

### 31. What is the correct way to write an infinite loop?
A) `while True:`
B) `for forever:`
C) `loop:`
D) `while 1 == 2:`

### 32. What is the output of `bool(0)`?
A) `True`
B) `False`
C) `None`
D) `0`

### 33. If `x = []` (an empty list), what does `if x:` evaluate to?
A) `True`
B) `False`
C) `SyntaxError`
D) `TypeError`

### 34. What is the outcome of `10 > 5 > 2`?
A) `True`
B) `False`
C) `TypeError`
D) `10`

### 35. Can you use `else` with a `while` loop in Python?
A) Yes, and it executes when the condition becomes False.
B) No, `else` is only for conditionals.
C) Yes, but it executes on every iteration.
D) Yes, but only if the loop uses `break`.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) `if`**
2. **C) `elif`**
3. **A) A** (It checks from top to bottom. Since 5 > 2 is True, it executes the first block and skips the rest).
4. **A) Yes**
5. **B) Colon `:`**
6. **C) `for` loop**
7. **B) `0, 1, 2, 3, 4`**
8. **A) `[1, 3, 5, 7, 9]`**
9. **B) `while` loop**
10. **C) It creates an infinite loop**
11. **C) `break`**
12. **D) `continue`**
13. **B) `02`** (Iteration `1` is skipped).
14. **C) Does absolutely nothing (placeholder)**
15. **A) True**
16. **D) 12** (3 * 4 = 12).
17. **A) Yes, it runs when the condition becomes False (if not broken)**
18. **C) `012`**
19. **B) Replaces the default newline with a space**
20. **A) `print("Hello" * 5)`**
21. **D) All are valid, but must be consistent within the block** (PEP 8 recommends 4 spaces).
22. **B) It raises an `IndentationError`**
23. **B) B** (The first `True` condition is executed, the rest are skipped).
24. **A) `4`** (The loop ends after iterating `0, 1, 2, 3, 4`).
25. **B) `enumerate()`**
26. **B) `10 down to 1`** (Stop parameter is exclusive).
27. **B) It stops only the inner loop**
28. **C) 3**
29. **A) Yes, it iterates character by character**
30. **A) A 2x2 square of stars**
31. **A) `while True:`**
32. **B) `False`**
33. **B) `False`** (Empty sequences evaluate to False).
34. **A) `True`** (Chained comparisons).
35. **A) Yes, and it executes when the condition becomes False.**

</details>
