# Day 12: 100 Interview Questions and Answers on Circular Queues & Deques

## Section 1: Basics of Queues
1. **What is a Queue?** A Linear data structure that follows First In First Out (FIFO).
2. **What are the primary operations of a queue?** Enqueue (insert) and Dequeue (delete).
3. **What is Front and Rear?** Front points to the first element to be deleted; Rear points to the last inserted element.
4. **What is Queue Overflow?** Trying to enqueue when the queue is full.
5. **What is Queue Underflow?** Trying to dequeue when the queue is empty.
6. **What is the time complexity of basic Queue operations?** O(1) for both enqueue and dequeue.
7. **What is the main drawback of a standard array-based queue?** The space is not reused after elements are dequeued.
8. **How does a Circular Queue solve standard queue limitations?** By connecting the last position back to the first position.
9. **Can a queue be implemented using stacks?** Yes, by using two stacks.
10. **What is the difference between a Queue and a Stack?** Queue is FIFO; Stack is LIFO.

## Section 2: Circular Queues
11. **What is a Circular Queue?** A queue where the last position is connected to the first position, making a circle.
12. **Also known as?** Ring Buffer.
13. **How is the circular nature achieved in an array?** Using modulo arithmetic: `(index + 1) % capacity`.
14. **What is the condition for a full Circular Queue?** `(rear + 1) % capacity == front`.
15. **What is the condition for an empty Circular Queue?** `front == -1` (or `front == rear` depending on implementation).
16. **How do you enqueue in a Circular Queue?** `rear = (rear + 1) % capacity; queue[rear] = value`.
17. **How do you dequeue?** `value = queue[front]; front = (front + 1) % capacity`.
18. **What happens if there's only one element and you dequeue?** You must reset `front` and `rear` to `-1`.
19. **What are real-world uses of Circular Queues?** CPU scheduling, memory management, traffic lights.
20. **Can Circular Queues be implemented with Linked Lists?** Yes, by making the last node point to the first node.

## Section 3: Deques (Double-Ended Queues)
21. **What is a Deque?** A queue where insertion and deletion can occur at both the front and the rear.
22. **Does a Deque strictly follow FIFO?** No, it blends FIFO and LIFO behavior.
23. **What is an Input-Restricted Deque?** Insertion is allowed at one end, but deletion at both ends.
24. **What is an Output-Restricted Deque?** Deletion is allowed at one end, but insertion at both ends.
25. **Can a Deque act as a Stack?** Yes, by restricting operations to one end.
26. **Can a Deque act as a Queue?** Yes, by inserting at rear and deleting at front.
27. **What is the best data structure to implement a Deque?** A Doubly Linked List.
28. **What is the time complexity of Deque operations?** O(1) for inserting/deleting at both ends.
29. **What Python library provides a Deque?** `collections.deque`.
30. **Is `collections.deque` thread-safe?** Yes, for appends and pops.

## Section 4: Implementation Mechanics
31. **How do you insert at the front of an array-based Deque?** `front = (front - 1 + capacity) % capacity; array[front] = val`.
32. **How do you insert at the rear of a Deque?** `rear = (rear + 1) % capacity; array[rear] = val`.
33. **How do you delete from the rear?** `val = array[rear]; rear = (rear - 1 + capacity) % capacity`.
34. **Why do we add `capacity` before taking the modulo in backwards steps?** To prevent negative indices in languages like C/Java (Python handles negative indices, but it's good practice).
35. **What happens when `front == rear` in a Deque?** There is exactly one element in the Deque.
36. **How do you find the number of elements in an array-based Circular Queue?** `(rear + capacity - front) % capacity + 1`.
37. **How does Python's Deque manage memory?** It uses a doubly-linked list of fixed-length blocks.
38. **Why not use a standard Python list as a Queue?** Deleting from the front `pop(0)` is O(N) because elements must shift.
39. **What is a Sliding Window algorithm?** A technique that maintains a subset of items (window) while iterating.
40. **Why is Deque the optimal structure for Sliding Window Maximum?** It maintains potential maximums in monotonic decreasing order in O(N) time.

## Section 5: Algorithmic Scenarios
41. **How to reverse a queue?** Dequeue all elements into a Stack, then pop them back into the Queue.
42. **How to sort a queue?** Use an auxiliary queue and keep elements ordered during transfers.
43. **How to reverse the first K elements of a queue?** Dequeue K elements to a stack, pop them back to the queue, then rotate the remaining N-K elements.
44. **How to implement a Stack using Queues?** Use two queues; to push, enqueue to Q2, move everything from Q1 to Q2, then swap names.
45. **How to implement a Queue using Stacks?** Use two stacks; enqueue to S1, dequeue from S2 (moving from S1 to S2 if S2 is empty).
46. **How to check if a string is a palindrome using Deque?** Enqueue characters, then repeatedly dequeue from front and rear and compare.
47. **What is the Josephus problem?** A counting-out game easily simulated using a Circular Queue.
48. **How do you find the first negative integer in every window of size K?** Using a Deque to store indices of negative numbers.
49. **How to generate binary numbers from 1 to N?** Use a queue: enqueue "1", then repeatedly dequeue `s`, print it, and enqueue `s+"0"` and `s+"1"`.
50. **How to interleave the first half of a queue with the second half?** Push the first half to a stack, then to a queue, then interleave.

## Section 6: Monotonic Deques
51. **What is a Monotonic Deque?** A deque where elements are strictly increasing or decreasing.
52. **What problem does it solve?** Finding the next/previous greater/smaller elements dynamically, like Sliding Window Maximum.
53. **In a monotonic decreasing deque, where do you insert?** At the back, removing smaller elements first.
54. **What is stored in the deque for sliding window problems?** Usually indices, to easily check if elements have fallen out of the window.
55. **How do you remove elements out of the window?** `while deque and deque[0] < i - K + 1: deque.popleft()`.

## Section 7: Priority Queues
56. **What is a Priority Queue?** A queue where elements are served based on priority, not insertion order.
57. **Is it a FIFO structure?** No.
58. **How is it usually implemented?** Using a Heap (Min-Heap or Max-Heap).
59. **Can a Deque act as a Priority Queue?** Not efficiently (insertion would be O(N)).
60. **Difference between Deque and Priority Queue?** Deque dictates position by insertion point; Priority Queue dictates position by value.

## Section 8: Memory & Complexities
61. **Space complexity of array-based Circular Queue?** O(N).
62. **Space complexity of Linked List Deque?** O(N).
63. **Is dynamic resizing possible in Circular Queues?** Yes, but you must untangle the wrapped elements during array copying.
64. **What is the amortized cost of Python's deque operations?** O(1).
65. **Time complexity of `len(deque)` in Python?** O(1).
66. **Time complexity of indexing `deque[i]` in Python?** O(N) because it requires traversing the blocks.
67. **Should you use a Deque for random access?** No, use a List instead.
68. **Is a circular linked list better than an array for Circular Queues?** It prevents resizing overhead but adds pointer memory overhead.
69. **What happens to the pointers in an empty circular linked list queue?** `rear = None`.
70. **What is a "ring buffer" drop policy?** If full, new elements overwrite the oldest elements (front advances automatically).

## Section 9: OS & Networking Uses
71. **How do operating systems use Queues?** Process scheduling (Round Robin).
72. **How do networks use Queues?** Packet buffering in routers.
73. **How do printers use Queues?** Print spooling.
74. **How are Deques used in browsers?** Maintaining browsing history (forward/back buttons).
75. **How are Deques used in Work Stealing algorithms?** Threads take tasks from the front of their deque, but steal from the rear of others.
76. **What is Spooling?** Simultaneous Peripheral Operations On-Line (uses queues).
77. **How do message brokers (RabbitMQ, Kafka) operate?** As advanced distributed queues.
78. **What is a buffer?** A temporary queue used to manage speed mismatches between producer and consumer.
79. **What is the Producer-Consumer problem?** Synchronizing threads that share a queue.
80. **What happens if consumer is faster than producer?** Queue Underflow (consumer must wait).

## Section 10: Advanced & Tricky Edge Cases
81. **Can you implement a queue with a single stack?** Yes, using the recursive call stack.
82. **If a circular queue capacity is N, why do some implementations only hold N-1 elements?** To distinguish between full (`rear+1 == front`) and empty (`front == rear`) states easily.
83. **How to avoid the N-1 limitation?** By keeping a `size` variable.
84. **What is a Double-ended Priority Queue?** A structure that allows finding/removing both min and max efficiently.
85. **What is the time complexity of reversing a Queue?** O(N).
86. **Can you sort a Queue without extra space?** No, you need at least the call stack (recursion) or an auxiliary structure.
87. **How do you find the middle element of a Queue?** Dequeue N/2 elements, record the middle, and continue enqueuing them back.
88. **What is a Bounded Queue?** A queue with a fixed maximum size (like our Circular Queue).
89. **What is an Unbounded Queue?** A queue that grows dynamically.
90. **Why does Python `deque` have a `maxlen` parameter?** To easily implement bounded queues or ring buffers that overwrite old data.
91. **What happens when you append to a full `deque(maxlen=K)`?** The opposite end pops an element automatically.
92. **How does BFS use a queue?** It enqueues neighbor nodes to explore them level by level.
93. **Why use a Queue for BFS and not a Stack?** A Stack would result in Depth-First Search (DFS).
94. **Can you implement an LRU Cache with a Deque?** Yes, move recently used items to the front and evict from the rear.
95. **What's the cost of removing an item from the middle of a `collections.deque`?** O(N).
96. **In Python, what does `deque.rotate(n)` do?** Shifts elements right by `n` steps (or left if `n` is negative) in O(K) time.
97. **Is a Circular Queue better than a Linked List Queue for cache locality?** Yes, arrays have contiguous memory, leading to fewer cache misses.
98. **What is "False Sharing" in concurrent queues?** When front and rear pointers share a cache line, causing performance drops.
99. **How to make a queue thread-safe in Python?** Use `queue.Queue`.
100. **Why master Deques?** They are the "Swiss Army Knife" of linear data structures, solving sliding window and bidirectional scheduling problems effortlessly.
