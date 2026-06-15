# Day 10: Introduction to Linked Lists Quiz

Test your knowledge of Day 10 concepts! Choose the best answer for each question.

---

### 1. What is a Linked List?
A) A sequence of elements stored in contiguous memory locations.
B) A linear collection of data elements where each element points to the next.
C) A built-in Python data type that is faster than a list.
D) A 2D grid of numbers.

### 2. In a Linked List, what is a "Node"?
A) The very last element.
B) An object containing both data and a pointer to the next element.
C) A variable that stores the length of the list.
D) A syntax error.

### 3. What does the "head" of a Linked List point to?
A) The largest element.
B) The last node.
C) The first node in the sequence.
D) `None` (always).

### 4. What does the `next` pointer of the LAST node in a singly linked list point to?
A) The head node.
B) The previous node.
C) `None` (or null).
D) Itself.

### 5. Why might you choose a Linked List over a standard Array/List?
A) To get faster O(1) access to elements by index.
B) To save memory space (Linked Lists use less memory than Arrays).
C) For efficient O(1) insertions/deletions at the beginning of the sequence.
D) Because Python forces you to.

### 6. What is the time complexity of accessing the 100th element in a Linked List?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 7. What is the time complexity of accessing the 100th element in an Array?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 8. How do you instantiate a Node with data `5` using `node = Node(5)`?
A) You must import the Node library.
B) You must define a `class Node:` with an `__init__` method.
C) It is a built-in Python command.
D) You cast an integer to a Node.

### 9. What happens if you lose the reference to the `head` node of a Linked List?
A) The list automatically recreates it.
B) You can easily find it by traversing backwards from the tail.
C) You lose access to the entire list, and it may be garbage collected.
D) Python throws an immediate error.

### 10. To traverse a Linked List, what is the standard loop condition?
A) `for i in range(len(list)):`
B) `while current is not None:`
C) `while True:`
D) `while current.next == head:`

### 11. During traversal, how do you move to the next node?
A) `current = current + 1`
B) `current += current.next`
C) `current = current.next`
D) `current.next()`

### 12. If `ll` is an empty LinkedList, what is the value of `ll.head`?
A) `0`
B) `False`
C) `None`
D) `[]`

### 13. What is the Time Complexity to insert a new node at the VERY BEGINNING (Head) of a Linked List?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 14. What are the correct steps to insert `new_node` at the Head?
A) `self.head = new_node` then `new_node.next = self.head`
B) `new_node.next = self.head` then `self.head = new_node`
C) `self.head.next = new_node`
D) `new_node = self.head`

### 15. Why is the order of operations crucial when inserting at the Head?
A) It isn't; Python handles it automatically.
B) If you overwrite `self.head` first, you lose the reference to the rest of the list.
C) It prevents memory leaks.
D) It makes the code run faster.

### 16. What is the Time Complexity to insert a new node at the END (Tail) of a singly linked list (assuming no `tail` pointer exists)?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 17. How do you find the last node in a Linked List?
A) Check if `current.next is None`.
B) Check if `current is None`.
C) Use `ll[-1]`.
D) Check if `current.data == 0`.

### 18. If you have a `tail` pointer in your LinkedList class, what becomes the Time Complexity of inserting at the end?
A) O(1)
B) O(n)
C) O(log n)
D) O(n^2)

### 19. What is a "Memory Leak" in the context of Linked Lists (in languages without garbage collection like C++)?
A) When water gets into the RAM.
B) When you delete a node from the list but forget to free its allocated memory.
C) When the list gets too long.
D) When `current.next` points to `None`.

### 20. Does Python suffer from memory leaks in the same way C++ does for Linked Lists?
A) Yes, exactly the same.
B) No, Python has a Garbage Collector that cleans up unreferenced objects.
C) Python doesn't use memory.
D) Only if the list is longer than 1000 nodes.

### 21. How do you delete the head node of a Linked List?
A) `del self.head`
B) `self.head = self.head.next`
C) `self.head.next = None`
D) `self.head = None`

### 22. What happens if you try to traverse a list and do `print(current.data)` when `current` is `None`?
A) It prints `None`.
B) It throws an `AttributeError: 'NoneType' object has no attribute 'data'`.
C) It skips the print statement.
D) It loops back to the head.

### 23. Arrays use contiguous memory. What does this mean?
A) The memory blocks are scattered everywhere.
B) The memory blocks are located right next to each other sequentially.
C) The memory changes size constantly.
D) The memory is stored on the hard drive.

### 24. A Singly Linked List allows traversal in how many directions?
A) One (Forward only)
B) Two (Forward and Backward)
C) Random access
D) Circular

### 25. If a node's `next` pointer accidentally points to a previous node in the list, what happens during traversal?
A) The list prints backwards.
B) It creates an infinite loop (a cycle).
C) It automatically fixes itself.
D) The program deletes the node.

### 26. Which operation is generally FASTER in an Array than a Linked List?
A) Inserting at the beginning.
B) Deleting the first element.
C) Accessing the 50th element.
D) Growing the size dynamically.

### 27. When deleting the LAST node in a singly linked list, why must you stop at the second-to-last node?
A) Because you need to update the second-to-last node's `next` pointer to `None`.
B) Because the last node is protected.
C) To save time.
D) You don't have to; you can stop at the last node.

### 28. How do you stop a traversal loop AT the last node (not after it)?
A) `while current is not None:`
B) `while current.next is not None:`
C) `while current.data is not None:`
D) `while current == tail:`

### 29. Can a Linked List hold different data types in Python (e.g., Node(5) -> Node("Hello") -> Node(True))?
A) Yes, because Python is dynamically typed.
B) No, Linked Lists must hold homogeneous data.
C) Only if you import a special library.
D) Yes, but only in arrays.

### 30. What does the `__init__` method do in the `Node` class?
A) Deletes the node.
B) Initializes the object's attributes (`data` and `next`) when created.
C) Prints the node.
D) Links it to the head.

### 31. If you want to insert a node `new_node` AFTER a given node `prev_node`, what is the correct order of operations?
A) `prev_node.next = new_node` then `new_node.next = prev_node.next`
B) `new_node.next = prev_node.next` then `prev_node.next = new_node`
C) `prev_node = new_node`
D) `new_node.next = None`

### 32. In the above question, what happens if you do step A instead of step B?
A) It works perfectly.
B) `new_node.next` will point to itself, and you lose the rest of the list!
C) The list is reversed.
D) A Syntax Error occurs.

### 33. What is the Space Complexity of a Linked List containing `n` elements?
A) O(1)
B) O(log n)
C) O(n)
D) O(n^2)

### 34. What is a major disadvantage of Linked Lists regarding memory?
A) They use no memory.
B) Every element requires extra memory to store the `next` pointer.
C) They require a single massive contiguous block of RAM.
D) They can only hold integers.

### 35. If you write `node1 = Node(1)` and `node2 = node1`, what happens?
A) Two separate nodes are created with value 1.
B) `node2` points to the EXACT SAME object in memory as `node1`.
C) `node2` becomes the `next` of `node1`.
D) An error occurs.

---
<details>
<summary><b>Click here to view the answers</b></summary>

1. **B) A linear collection of data elements where each element points to the next.**
2. **B) An object containing both data and a pointer to the next element.**
3. **C) The first node in the sequence.**
4. **C) `None` (or null).**
5. **C) For efficient O(1) insertions/deletions at the beginning of the sequence.**
6. **C) O(n)**
7. **A) O(1)**
8. **B) You must define a `class Node:` with an `__init__` method.**
9. **C) You lose access to the entire list, and it may be garbage collected.**
10. **B) `while current is not None:`**
11. **C) `current = current.next`**
12. **C) `None`**
13. **A) O(1)**
14. **B) `new_node.next = self.head` then `self.head = new_node`**
15. **B) If you overwrite `self.head` first, you lose the reference to the rest of the list.**
16. **C) O(n)**
17. **A) Check if `current.next is None`.**
18. **A) O(1)**
19. **B) When you delete a node from the list but forget to free its allocated memory.**
20. **B) No, Python has a Garbage Collector that cleans up unreferenced objects.**
21. **B) `self.head = self.head.next`**
22. **B) It throws an `AttributeError: 'NoneType' object has no attribute 'data'`.**
23. **B) The memory blocks are located right next to each other sequentially.**
24. **A) One (Forward only)**
25. **B) It creates an infinite loop (a cycle).**
26. **C) Accessing the 50th element.**
27. **A) Because you need to update the second-to-last node's `next` pointer to `None`.**
28. **B) `while current.next is not None:`**
29. **A) Yes, because Python is dynamically typed.**
30. **B) Initializes the object's attributes (`data` and `next`) when created.**
31. **B) `new_node.next = prev_node.next` then `prev_node.next = new_node`**
32. **B) `new_node.next` will point to itself, and you lose the rest of the list!**
33. **C) O(n)**
34. **B) Every element requires extra memory to store the `next` pointer.**
35. **B) `node2` points to the EXACT SAME object in memory as `node1`.**

</details>
