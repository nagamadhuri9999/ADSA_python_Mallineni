# 100 Interview Questions & Answers on Stacks and Queues

Welcome to the ultimate preparation guide for Stacks and Queues. This document contains 100 essential interview questions ranging from basic definitions to advanced algorithmic applications.

## Part 1: Basic Stack Concepts (1-20)

1. **What is a Stack?**
   A Stack is a linear data structure that follows the LIFO (Last-In-First-Out) principle, meaning the last element added is the first one removed.

2. **What are the primary operations of a Stack?**
   `push()` (add to top), `pop()` (remove from top), `peek()`/`top()` (view top element without removing), and `isEmpty()`.

3. **What is the time complexity of Stack operations?**
   All primary operations (`push`, `pop`, `peek`, `isEmpty`) take $O(1)$ time.

4. **What is Stack Overflow?**
   Stack Overflow occurs when an attempt is made to push an element onto a stack that is already full (exceeds its maximum capacity).

5. **What is Stack Underflow?**
   Stack Underflow occurs when an attempt is made to pop an element from an empty stack.

6. **How is a Stack different from an Array?**
   An Array allows random access to elements via indices, whereas a Stack only allows sequential access at one end (the top).

7. **Can we implement a Stack using a Linked List?**
   Yes. The head of the Linked List acts as the top of the Stack. Pushing inserts a node at the head, and popping removes the node at the head. Both are $O(1)$.

8. **Why are Stacks useful for recursion?**
   Recursion relies on the Call Stack. Each function call pushes its context onto the stack, and when it returns, the context is popped, naturally resuming the previous state.

9. **Give a real-world example of a Stack.**
   The "Undo" feature in text editors or the "Back" button in a web browser.

10. **Is Python’s `list` a good Stack?**
    Yes. Appending to the end and popping from the end of a Python `list` both take $O(1)$ amortized time.

11. **What is postfix notation?**
    An algebraic notation where the operator follows its operands (e.g., `A B +`). It is easily evaluated using a Stack.

12. **What is prefix notation?**
    An algebraic notation where the operator precedes its operands (e.g., `+ A B`).

13. **How does a Stack evaluate a postfix expression?**
    Scan left to right. Push operands to the stack. When an operator is found, pop the top two operands, apply the operator, and push the result back.

14. **Why convert infix to postfix?**
    Postfix notation removes the need for parentheses and operator precedence rules, making it easier for computers to evaluate using a Stack.

15. **What is the space complexity of reversing a string using a Stack?**
    $O(N)$, where N is the length of the string, since all characters must be pushed onto the stack.

16. **How do you find the middle element of a Stack?**
    Standard Stacks do not allow random access. To find the middle, you must pop half the elements into an auxiliary stack (or use a doubly-linked list with a middle pointer for an optimized custom implementation).

17. **What is the "Valid Parentheses" problem?**
    A classic Stack problem where you verify if every opening bracket has a corresponding and correctly ordered closing bracket.

18. **Can you sort a Stack using only one auxiliary Stack?**
    Yes. Pop an element, compare it with the top of the auxiliary stack. If the auxiliary stack's top is greater, pop it back to the original stack until the correct spot is found, then push the element.

19. **What happens if you use `insert(0, val)` to implement a push in a Python list?**
    It creates a stack where the "top" is at index 0. However, this makes `push` and `pop` take $O(N)$ time because all other elements must shift.

20. **Is a Stack a recursive data structure?**
    Conceptually, yes. A Stack can be defined as an element (top) and the rest of the Stack.

---

## Part 2: Basic Queue Concepts (21-40)

21. **What is a Queue?**
    A Queue is a linear data structure that follows the FIFO (First-In-First-Out) principle.

22. **What are the primary operations of a Queue?**
    `enqueue()` (add to rear), `dequeue()` (remove from front), `front()`/`peek()`, and `isEmpty()`.

23. **What is the time complexity of Queue operations?**
    Ideally, $O(1)$ for all primary operations.

24. **Why is using a Python `list` for a Queue bad?**
    `list.pop(0)` takes $O(N)$ time because it requires shifting all remaining elements one position to the left.

25. **What is the proper way to implement a Queue in Python?**
    Using `collections.deque` (Double-Ended Queue), which provides $O(1)$ time for both `append()` and `popleft()`.

26. **Give a real-world example of a Queue.**
    A line of people waiting at a ticket counter, or a printer spooler managing print jobs.

27. **What is a Circular Queue?**
    A fixed-size Queue where the last position connects back to the first position, effectively utilizing empty spaces created by dequeued elements.

28. **How do you calculate the next rear position in a Circular Queue?**
    `rear = (rear + 1) % capacity`.

29. **What is a Priority Queue?**
    A special type of Queue where each element is associated with a priority. Elements are dequeued in order of priority rather than insertion order.

30. **How is a Priority Queue usually implemented?**
    Using a Heap (specifically a Min-Heap or Max-Heap), which allows insertion and extraction in $O(\log N)$ time.

31. **What is a Deque?**
    A Double-Ended Queue. It allows insertion and deletion from both the front and the rear in $O(1)$ time.

32. **Can a Deque be used as a Stack?**
    Yes, by only using operations at one end (e.g., `append()` and `pop()`).

33. **Can a Deque be used as a Queue?**
    Yes, by using `append()` at one end and `popleft()` at the other.

34. **What is the difference between BFS and DFS?**
    Breadth-First Search (BFS) explores level by level and uses a **Queue**. Depth-First Search (DFS) explores as deep as possible and uses a **Stack** (or recursion).

35. **How do you reverse a Queue?**
    Dequeue all elements and push them onto a Stack, then pop all elements from the Stack and enqueue them back into the Queue.

36. **How do you implement a Queue using two Stacks?**
    One stack handles `enqueue` (push). For `dequeue`, if the second stack is empty, pop everything from the first stack and push it to the second, then pop from the second stack.

37. **What is the amortized time complexity of dequeue in the two-stack implementation?**
    $O(1)$ amortized. Even though moving elements takes $O(N)$, it only happens occasionally, averaging out to $O(1)$ per operation.

38. **How do you implement a Stack using two Queues?**
    On `push`, enqueue the element to `q2`, then dequeue everything from `q1` and enqueue to `q2`. Swap `q1` and `q2`. This makes `push` $O(N)$ and `pop` $O(1)$.

39. **What is a Blocking Queue?**
    A Queue used in multithreading that blocks a thread attempting to dequeue from an empty queue, or enqueue to a full queue. Python's `queue.Queue` is blocking.

40. **What is the "Josephus Problem"?**
    A classic theoretical problem involving people standing in a circle. It is often simulated using a Circular Queue.

---

## Part 3: Python Implementation & Types (41-60)

41. **What module provides thread-safe queues in Python?**
    The `queue` module (`queue.Queue`, `queue.LifoQueue`, `queue.PriorityQueue`).

42. **What is the difference between `collections.deque` and `queue.Queue`?**
    `deque` is fast but not intrinsically safe for complex multi-threading (though atomic appends/pops are safe). `queue.Queue` has built-in locking and blocking mechanics for threads.

43. **How do you create a bounded (fixed-size) deque?**
    `deque(maxlen=N)`. If you append when full, the oldest item is automatically dropped.

44. **What happens if you use `heapq` in Python for a priority queue?**
    `heapq` provides functions to manipulate a standard `list` as a Min-Heap.

45. **How do you create a Max-Heap Priority Queue in Python?**
    Since `heapq` is a min-heap, you multiply all numeric values by `-1` before pushing, and multiply by `-1` again after popping.

46. **What is `queue.LifoQueue`?**
    It is a thread-safe Stack provided by Python's standard library.

47. **Why might you choose a custom Linked List over `deque`?**
    You almost never would in Python for production, but it is useful in interviews to demonstrate memory manipulation and node references.

48. **Does `deque` store elements contiguously in memory like `list`?**
    No. CPython implements `deque` as a doubly-linked list of blocks (chunks of memory).

49. **Why is `list` iteration faster than `deque` iteration?**
    Because a `list` is a single contiguous block of memory, which is highly cache-friendly compared to the linked chunks of a `deque`.

50. **How do you sort a `deque`?**
    You cannot sort a `deque` directly in-place. You must convert it to a `list`, sort it, and convert it back: `deque(sorted(d))`.

51. **What exception does `queue.Queue.get(block=False)` raise if empty?**
    It raises `queue.Empty`.

52. **What exception does `deque.pop()` raise if empty?**
    It raises `IndexError: pop from an empty deque`.

53. **How do you access the middle element of a `deque`?**
    `dq[len(dq) // 2]`. However, unlike a list, accessing middle elements in a `deque` is $O(N)$, not $O(1)$.

54. **Is `heapq.heappush()` $O(1)$?**
    No, it is $O(\log N)$ because the heap must rebalance to maintain its properties.

55. **How do you initialize a heap with an existing list in $O(N)$ time?**
    Use `heapq.heapify(my_list)`.

56. **What happens when multiple threads write to a standard `list` simultaneously?**
    It can cause race conditions or corrupt the list, as `list` is not thread-safe for complex operations.

57. **What is a deque's `rotate()` method?**
    `dq.rotate(n)` shifts the deque elements n steps to the right. If n is negative, it shifts to the left.

58. **How does Python's Garbage Collector handle popped nodes from a custom Linked List stack?**
    Once the reference count of the popped Node reaches 0 (no variables point to it), the GC automatically reclaims its memory.

59. **Can a Queue contain mixed data types in Python?**
    Yes. Python lists, deques, and queues are dynamically typed and can hold any combination of objects.

60. **How do you implement an LRU (Least Recently Used) Cache using a Queue?**
    Using a combination of a Hash Map (for $O(1)$ lookups) and a Doubly Linked List (or Deque) to keep track of access order. In Python, `collections.OrderedDict` perfectly replicates this.

---

## Part 4: Advanced Concepts & Monotonic Sequences (61-80)

61. **What is a Monotonic Stack?**
    A stack whose elements are strictly increasing or strictly decreasing from bottom to top.

62. **What problem does a Monotonic Stack solve?**
    It solves the "Next Greater Element" or "Next Smaller Element" problem in $O(N)$ time.

63. **How do you maintain an increasing Monotonic Stack?**
    Before pushing a new element, pop all elements from the stack that are strictly greater than the new element.

64. **What is the time complexity of building a Monotonic Stack?**
    $O(N)$. Even though there is a `while` loop inside a `for` loop, every element is pushed and popped at most once.

65. **What is a Monotonic Queue?**
    Similar to a Monotonic Stack, but typically implemented as a Deque, allowing elements to drop off the "front" as well (used for sliding windows).

66. **How do you solve "Sliding Window Maximum"?**
    Use a Monotonic Decreasing Deque. Store indices. Remove indices out of the window from the left, and pop smaller elements from the right before adding the new index.

67. **What is the "Largest Rectangle in Histogram" problem?**
    A classic Hard problem solved optimally using a Monotonic Increasing Stack to find the nearest smaller bars to the left and right.

68. **How does a Min Stack work?**
    It maintains two stacks internally: one for the actual values, and one that specifically tracks the minimum value seen so far at that depth.

69. **Can a Min Stack be optimized to use less space?**
    Yes. Instead of pushing the min value every time, only push to the `min_stack` when the new value is $\le$ the current minimum.

70. **How do you solve "Daily Temperatures"?**
    Use a Monotonic Decreasing Stack. As you iterate, if the current temp is warmer than the temp at the index on top of the stack, pop the stack and calculate the day difference.

71. **What is the "Asteroid Collision" problem?**
    A simulation problem. Use a Stack. Positive asteroids are pushed. Negative asteroids destroy positive ones on the top of the stack if their absolute value is greater.

72. **What is "Stock Spanner"?**
    Finding the maximum consecutive days the stock was $\le$ today. Solved using a Monotonic Stack storing `(price, span)`.

73. **How do you evaluate mathematical strings like `"3+2*2"`?**
    Use a Stack to handle multiplication/division first. Push numbers to the stack, apply `*` or `/` immediately to the top of the stack, then sum the stack at the end.

74. **What is the "Simplify Path" problem?**
    Resolving UNIX paths like `/a/./b/../../c/`. Split by `/`, push valid folder names to a Stack, and pop when encountering `..`.

75. **How does Breadth-First Search track levels?**
    By capturing the `size = len(queue)` at the start of a level iteration, and popping exactly `size` times.

76. **How do you detect a cycle in a Directed Graph using Queues?**
    Using Kahn's Algorithm for Topological Sort. Maintain an in-degree array. Enqueue nodes with in-degree 0. If the popped count != total nodes, there is a cycle.

77. **What happens in Topological Sort if multiple items are in the queue?**
    It means there are multiple valid topological orderings.

78. **What is the "Rotting Oranges" problem?**
    A multi-source BFS problem. Initially, enqueue all rotting oranges. Then perform BFS level-by-level to infect adjacent fresh oranges.

79. **How do you find the shortest path in an unweighted maze?**
    Use BFS with a Queue, keeping track of visited cells.

80. **Why does DFS use less memory than BFS on deep, non-branching trees?**
    The Call Stack in DFS is proportional to the depth of the tree ($O(H)$), whereas the Queue in BFS is proportional to the width of the tree (which could be $O(2^H)$ at the bottom level).

---

## Part 5: Edge Cases, Tricks, and Rapid Fire (81-100)

81. **What is the edge case when finding the Next Greater Element?**
    If no greater element exists, you must handle the logic to output `-1` (usually by processing whatever is left in the stack at the end).

82. **What is the edge case in a Circular Queue?**
    Differentiating between "Queue is Full" and "Queue is Empty" because both conditions can result in the `head` and `tail` pointers matching if not tracked properly.

83. **How do you solve the full/empty ambiguity in Circular Queues?**
    Either maintain a separate `size` counter, or make the underlying array size $N+1$ and leave one slot intentionally empty.

84. **Can you push `None` onto a Stack in Python?**
    Yes, lists and deques can hold `None`. However, you must be careful not to confuse popping `None` with the stack being empty.

85. **What is the "Remove All Adjacent Duplicates" problem?**
    Iterate characters. If the stack top matches the current character, pop the stack. Otherwise, push. E.g., `abbaca` -> `ca`.

86. **How do you handle k-duplicates (e.g., remove 3 adjacent)?**
    Push a tuple `(character, count)` to the Stack. If count reaches `k`, pop it.

87. **In a Multi-threaded Queue, what is a "poison pill"?**
    A special token (like `None` or a custom object) enqueued to signal worker threads that they should terminate gracefully.

88. **If `pop(0)` is $O(N)$, why is `pop()` $O(1)$?**
    `pop()` removes the last element. The array length shrinks, but no other elements need to shift their memory addresses.

89. **What is "Flatten Nested List Iterator"?**
    An algorithm that uses a Stack to flatten `[[1,1],2,[1,1]]`. You push the list in reverse order, so the first elements are on top.

90. **Why would you use an Array-based Stack over a Linked-List Stack in performance-critical C/C++ code?**
    Spatial locality. Arrays are contiguous in memory, leading to fewer cache misses in the CPU.

91. **What is "Data Stream as Disjoint Intervals"?**
    A complex problem involving merging intervals. Can be optimized using a Priority Queue or a BST.

92. **How does Python's `heapq` handle ties in priority?**
    It compares the next element in the tuple. If you push `(priority, object)`, Python tries to compare `object`. If the object doesn't support `<` comparison, it throws an error.

93. **How do you fix the `heapq` tie-breaker error?**
    Push a 3-element tuple: `(priority, unique_counter, object)`. The `unique_counter` ensures it never has to compare the object itself.

94. **What is a "Double-ended Priority Queue"?**
    A structure that can quickly find/remove both the minimum and maximum elements. Implemented using an Interval Heap or two coupled Heaps.

95. **If a tree is perfectly balanced, how many elements are in the Queue during BFS at the lowest level?**
    Roughly half the total number of nodes in the tree ($N/2$).

96. **If you have an infinite stream of data, can you use a Stack to reverse it?**
    No. A Stack requires the entire stream to end before it can start popping in reverse order.

97. **Can a Priority Queue be implemented using an unsorted array?**
    Yes, but finding/removing the highest priority item takes $O(N)$ time.

98. **Can a Priority Queue be implemented using a sorted array?**
    Yes. Finding the highest priority is $O(1)$, but inserting a new item takes $O(N)$ because elements must shift. This is why Heaps ($O(\log N)$) are the perfect middle ground.

99. **Is recursion always better than an explicit Stack?**
    No. Recursion is elegant, but an explicit Stack avoids the strict memory limits of the OS Call Stack (Python's recursion limit is usually 1000).

100. **What is the single most important rule when using Stacks/Queues in interviews?**
     **Always check if it's empty before calling `pop()` or `peek()`!** Forgetting `if stack:` or `if queue:` is the #1 cause of bugs in whiteboard interviews.
