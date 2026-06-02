# Day 2: Control Flow & Loops Quiz

Test your knowledge of Day 2 concepts! Choose the best answer for each question.

---

### 1. What will the following code print?
```python
x = 5
if x > 10:
    print("A")
elif x > 3:
    print("B")
else:
    print("C")
```
A) `A`
B) `B`
C) `C`
D) `A` and `B`

### 2. How many times will this `for` loop execute?
```python
for i in range(2, 6):
    print(i)
```
A) 6 times
B) 5 times
C) 4 times
D) 3 times

### 3. Which keyword is used to stop a loop entirely before it has finished all its iterations?
A) `stop`
B) `continue`
C) `break`
D) `exit`

### 4. What is the output of the following code?
```python
count = 0
while count < 3:
    print(count)
    count += 1
```
A) `0 1 2` (on separate lines)
B) `1 2 3` (on separate lines)
C) `0 1 2 3` (on separate lines)
D) It creates an infinite loop

### 5. In a nested loop, how many times does the inner loop execute?
```python
for i in range(3):
    for j in range(2):
        print("Hello")
```
A) 2 times
B) 3 times
C) 5 times
D) 6 times

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) `B`** (The condition `x > 10` is False, so it moves to `elif x > 3`, which is True. Once a true condition is met, the rest of the block is skipped).
2. **C) 4 times** (`range(2, 6)` generates the numbers 2, 3, 4, and 5. It stops *before* 6).
3. **C) `break`** (The `break` statement immediately terminates the loop containing it).
4. **A) `0 1 2` (on separate lines)** (The loop starts at 0, prints it, increments to 1. Prints 1, increments to 2. Prints 2, increments to 3. The condition `3 < 3` is False, so the loop ends).
5. **D) 6 times** (The outer loop runs 3 times. For *each* of those 3 times, the inner loop runs 2 times. 3 * 2 = 6).

</details>
