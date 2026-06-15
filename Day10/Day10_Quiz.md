# Day 10: Introduction to Stacks Quiz

Test your knowledge of Day 10 concepts! Choose the best answer for each question.

---

### 1. What does the acronym LIFO stand for?
A) Last In, First Out
B) List In, File Out
C) Last Item, Final Object
D) Leave In, Find Out

### 2. Which real-world example best represents a Stack?
A) A line of people waiting for a bus.
B) A stack of cafeteria plates.
C) A dictionary of words.
D) A web of connected cities.

### 3. Which operation adds an item to the top of a stack?
A) Push
B) Pop
C) Peek
D) Enqueue

### 4. Which operation removes and returns the item from the top of a stack?
A) Push
B) Pop
C) Peek
D) Dequeue

### 5. What does the `peek()` or `top()` operation do?
A) Removes the top item.
B) Adds an item to the bottom.
C) Returns the top item without removing it.
D) Clears the entire stack.

### 6. What is the time complexity of the `push` operation in a standard stack?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 7. What is the time complexity of the `pop` operation in a standard stack?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 8. In Python, what built-in data structure is typically used to implement a Stack?
A) tuple
B) dictionary
C) list
D) set

### 9. Which Python list method is used to simulate a `push` operation?
A) `.add()`
B) `.push()`
C) `.append()`
D) `.insert(0, item)`

### 10. Which Python list method is used to simulate a `pop` operation?
A) `.remove()`
B) `.pop()`
C) `.delete()`
D) `.pop(0)`

### 11. How do you `peek` at the top item of a stack implemented as a Python list?
A) `stack.peek()`
B) `stack[0]`
C) `stack[-1]`
D) `stack.top()`

### 12. Why is it a bad idea to use `.insert(0, item)` to push onto a Python list stack?
A) It causes a syntax error.
B) It takes O(n) time because all other elements must be shifted.
C) It deletes the list.
D) It only works on strings.

### 13. If you push 'A', then 'B', then 'C' onto an empty stack, what will the first `pop()` return?
A) 'A'
B) 'B'
C) 'C'
D) None

### 14. If you push 1, 2, 3, pop once, push 4, and pop again, what is returned by the last pop?
A) 1
B) 2
C) 3
D) 4

### 15. What is the main characteristic of a Monotonic Increasing Stack?
A) It only holds integers.
B) Elements are always in strictly increasing order from bottom to top.
C) It cannot be popped.
D) It never grows larger than 5 elements.

### 16. In a Valid Parentheses problem, when you encounter a closing bracket `)`, what should you do?
A) Push it onto the stack.
B) Check if the stack is empty. If not, pop the top and check if it's an `(`.
C) Delete the stack.
D) Ignore it.

### 17. If a string is "()[]{}", will the stack be empty at the very end of processing?
A) Yes
B) No

### 18. If a string is "([)]", what happens when you process the `)`?
A) You pop `[`, they don't match, so it's invalid.
B) You pop `(`, they match, so it's valid.
C) You push `)`.
D) The program crashes.

### 19. What does the "Call Stack" do in most programming languages?
A) Makes phone calls over the internet.
B) Keeps track of active functions and where they should return when finished.
C) Stores the source code.
D) Deletes unused variables.

### 20. If Function A calls Function B, which function is at the top of the Call Stack?
A) Function A
B) Function B
C) Neither
D) The main program

### 21. What happens if the Call Stack grows too large (e.g., infinite recursion)?
A) Stack Overflow
B) Stack Underflow
C) Out of Bounds Error
D) Syntax Error

### 22. What is Reverse Polish Notation (RPN)?
A) A way to write numbers backwards.
B) A mathematical notation in which operators follow their operands (e.g., `3 4 +`).
C) A sorting algorithm.
D) A database format.

### 23. How do you evaluate an RPN expression using a Stack?
A) Push operators, pop numbers.
B) Push numbers. When you see an operator, pop two numbers, apply the operator, and push the result.
C) You can't use a stack for RPN.
D) Sort the expression first.

### 24. For the RPN expression `5 1 2 + 4 * + 3 -`, what is pushed onto the stack first?
A) `+`
B) `5`
C) `3`
D) `-`

### 25. What does the Backspace String Compare problem demonstrate?
A) That keyboards are unreliable.
B) That stacks are perfect for simulating typing where a character (like `#`) "undoes" or pops the previous character.
C) That arrays are faster than stacks.
D) How to encrypt passwords.

### 26. To reverse a string using a stack, what do you do?
A) Push all characters onto the stack, then pop them all off into a new string.
B) Pop all characters.
C) Sort the stack.
D) Count the stack length.

### 27. What is "Stack Underflow"?
A) Pushing too many items.
B) Popping from an empty stack.
C) A memory leak.
D) Using floats instead of integers.

### 28. In Python, what error occurs if you call `.pop()` on an empty list?
A) ValueError
B) TypeError
C) IndexError: pop from empty list
D) KeyError

### 29. Can a Stack be implemented using a Linked List?
A) Yes, by keeping a pointer to the head and performing O(1) insertions/deletions at the head.
B) No, Stacks must be arrays.
C) Yes, but it takes O(n) time for every operation.
D) Only in C++.

### 30. Which real-world software feature is NOT typically implemented with a Stack?
A) Browser history (Back button)
B) Undo mechanism in a text editor
C) A printer queue (first to click print, first to get paper)
D) Call Stack for recursion

### 31. If you need to find the "Next Greater Element" for every item in an array in O(n) time, what type of stack is best?
A) A randomized stack.
B) A monotonic decreasing stack.
C) A string stack.
D) A binary tree.

### 32. In the "Daily Temperatures" problem, what do you typically store in the stack?
A) The actual temperature values.
B) The indices of the temperatures, so you can calculate how many days passed.
C) The string "hot" or "cold".
D) Nothing.

### 33. If you push items 1, 2, 3 into a stack, how many pops does it take to empty it?
A) 1
B) 2
C) 3
D) 4

### 34. What is the Space Complexity of a Stack containing `N` items?
A) O(1)
B) O(log N)
C) O(N)
D) O(N^2)

### 35. Does a Stack allow you to access the middle element in O(1) time?
A) Yes, via `stack.mid()`.
B) No, a strict Stack only allows access to the top element.
C) Yes, via indexing.
D) Only if the stack length is odd.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **A) Last In, First Out**
2. **B) A stack of cafeteria plates.**
3. **A) Push**
4. **B) Pop**
5. **C) Returns the top item without removing it.**
6. **A) O(1)**
7. **A) O(1)**
8. **C) list**
9. **C) `.append()`**
10. **B) `.pop()`**
11. **C) `stack[-1]`**
12. **B) It takes O(n) time because all other elements must be shifted.**
13. **C) 'C'**
14. **D) 4**
15. **B) Elements are always in strictly increasing order from bottom to top.**
16. **B) Check if the stack is empty. If not, pop the top and check if it's an `(`.**
17. **A) Yes**
18. **A) You pop `[`, they don't match, so it's invalid.**
19. **B) Keeps track of active functions and where they should return when finished.**
20. **B) Function B**
21. **A) Stack Overflow**
22. **B) A mathematical notation in which operators follow their operands.**
23. **B) Push numbers. When you see an operator, pop two numbers, apply the operator, and push the result.**
24. **B) `5`**
25. **B) That stacks are perfect for simulating typing where a character (like `#`) "undoes" or pops the previous character.**
26. **A) Push all characters onto the stack, then pop them all off into a new string.**
27. **B) Popping from an empty stack.**
28. **C) IndexError: pop from empty list**
29. **A) Yes, by keeping a pointer to the head and performing O(1) insertions/deletions at the head.**
30. **C) A printer queue (first to click print, first to get paper)**
31. **B) A monotonic decreasing stack.**
32. **B) The indices of the temperatures, so you can calculate how many days passed.**
33. **C) 3**
34. **C) O(N)**
35. **B) No, a strict Stack only allows access to the top element.**

</details>
