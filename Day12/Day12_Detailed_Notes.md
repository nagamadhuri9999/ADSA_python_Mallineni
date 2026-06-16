# Day 12: Circular Queues and Deques

## 1. Circular Queues (Ring Buffer)
A circular queue is an extended version of a regular queue where the last position is connected back to the first position to make a circle. It is also called a **Ring Buffer**.

### Why do we need it?
In a standard array-based queue, once the queue becomes full, we cannot insert the next element even if there is space at the front of the queue (due to `dequeue` operations). Circular queues solve this problem by wrapping around to the beginning.

### Key Concepts
- `front`: Points to the front item.
- `rear`: Points to the last item.
- **Modulo Arithmetic**: The key to the wrap-around is using modulo division: `(index + 1) % capacity`.

### Operations
1. **enQueue(value)**: Insert an element into the circular queue.
   - Check if the queue is full.
   - `rear = (rear + 1) % capacity`
   - Insert the element at `queue[rear]`.
2. **deQueue()**: Delete an element from the circular queue.
   - Check if the queue is empty.
   - Retrieve the element at `queue[front]`.
   - `front = (front + 1) % capacity`
3. **Front()**: Get the front item from the queue.
4. **Rear()**: Get the last item from the queue.

### Time Complexity
- All operations: O(1)

## 2. Deques (Double Ended Queues)
A Deque is a linear data structure that allows insertion and deletion of elements from both ends (front and rear).

### Types of Deques
- **Input Restricted Deque**: Insertion is done only at one end, while deletion can be done from both ends.
- **Output Restricted Deque**: Deletion is done only at one end, while insertion can be done from both ends.

### Python Implementation
In Python, `collections.deque` provides an O(1) time complexity for append and pop operations from both ends.

```python
from collections import deque

d = deque()
d.append(1)        # Insert at right
d.appendleft(2)    # Insert at left
d.pop()            # Remove from right
d.popleft()        # Remove from left
```

### Applications
- Palindrome Checking.
- Sliding Window Maximum (LeetCode Hard).
- Multi-processor scheduling.

## 3. Linked List Implementations
While arrays provide a fixed-size approach (or dynamically resizing approach), we can also build these structures using Linked Lists to achieve fully dynamic sizing.

### Circular Queue using Circular Linked List
- We maintain a `rear` pointer that points to the last inserted node.
- The next pointer of `rear` always points to the `front` node (`rear.next = front`).
- **enQueue**: Add a new node after `rear`, then update `rear` to point to this new node, and connect the new node's next to `front`.
- **deQueue**: Update `rear.next` to point to `front.next`, effectively dropping the current front node.

### Deque using Doubly Linked List
- We maintain both `front` and `rear` pointers.
- Each node has a `prev` and `next` pointer.
- **insertFront**: Create a new node, point its `next` to current `front`, and `front.prev` to the new node. Update `front` pointer.
- **insertLast**: Create a new node, point its `prev` to current `rear`, and `rear.next` to the new node. Update `rear` pointer.
- **deleteFront / deleteLast**: Disconnect the nodes and move the respective pointers.
- Time Complexity for all these operations remains O(1) without any need to shift elements or handle modulo arithmetic.
