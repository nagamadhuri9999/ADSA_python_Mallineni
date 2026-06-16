# Day 12: Interview Questions on Circular Queues and Deques

### 1. What is the difference between a Queue and a Circular Queue?
**Answer:**
A standard queue is linear, and array-based implementations suffer from false overflow (if elements are dequeued, space at the front cannot be reused without shifting elements). A circular queue connects the last index back to the first index, allowing efficient reuse of empty spaces created by `dequeue` operations.

### 2. Explain how to check if a Circular Queue is full.
**Answer:**
A circular queue is full when the next position of the `rear` pointer is equal to the `front` pointer. Mathematically, it is full if `(rear + 1) % capacity == front`. Alternatively, if you maintain a `count` of elements, it is full when `count == capacity`.

### 3. What is a Deque? Where is it used?
**Answer:**
A Deque (Double Ended Queue) is a queue where elements can be added or removed from both the front and the rear. It is used in algorithms like the Sliding Window Maximum, Palindrome checking, and in systems like multi-processor scheduling (work stealing algorithm).

### 4. What is the time complexity of operations in a Circular Queue?
**Answer:**
All basic operations (`enQueue`, `deQueue`, `Front`, `Rear`, `isEmpty`, `isFull`) have a time complexity of O(1) because we are just using mathematical formulas to find the correct index without shifting any elements.

### 5. Can we implement a Queue using two Stacks? Can we implement a Stack using Queues?
**Answer:**
Yes. 
- **Queue using two Stacks:** Push elements into Stack 1. When a pop is required, if Stack 2 is empty, pop all elements from Stack 1 and push them to Stack 2. Then pop from Stack 2.
- **Stack using Queues:** Use two queues or a single queue. For a single queue, when pushing an element, enqueue it, then dequeue and enqueue all previously existing elements so the new element ends up at the front.
