"""
Comprehensive Queue Implementations in Python
=============================================
This file demonstrates various ways to implement a Queue in Python,
including different variants like Deques, Priority Queues, and Circular Queues.
"""

from collections import deque
from queue import Queue, PriorityQueue
import heapq

# ==============================================================================
# 1. Queue Implementation using Python's built-in `list`
# ==============================================================================
# Pros: Simple to understand.
# Cons: Highly inefficient. pop(0) takes O(N) time because all other elements 
# must be shifted. DO NOT use this for large datasets.
print("--- 1. Queue using list ---")
queue_list = []
queue_list.append('A')  # Enqueue
queue_list.append('B')
queue_list.append('C')
print("Initial queue:", queue_list)
print("Dequeued:", queue_list.pop(0))  # Dequeue
print("Queue after dequeue:", queue_list)


# ==============================================================================
# 2. Queue Implementation using `collections.deque`
# ==============================================================================
# Pros: O(1) time complexity for appends and pops from both ends. The standard 
# way to implement a simple Queue in Python.
print("\n--- 2. Queue using collections.deque ---")
queue_deque = deque()
queue_deque.append('X')  # Enqueue
queue_deque.append('Y')
queue_deque.append('Z')
print("Initial queue:", queue_deque)
print("Dequeued:", queue_deque.popleft())  # Dequeue
print("Queue after dequeue:", queue_deque)


# ==============================================================================
# 3. Queue Implementation using `queue.Queue`
# ==============================================================================
# Pros: Thread-safe, excellent for multi-threading.
# Cons: Slower than collections.deque due to locking mechanisms.
print("\n--- 3. Queue using queue.Queue ---")
q = Queue(maxsize=3)
q.put('Apple')   # Enqueue
q.put('Banana')
q.put('Cherry')
print("Is queue full?", q.full())
print("Dequeued:", q.get())  # Dequeue


# ==============================================================================
# 4. Specialized: Deque (Double Ended Queue)
# ==============================================================================
# Elements can be added or removed from both the front and the back.
print("\n--- 4. Specialized: Double Ended Queue (Deque) ---")
dq = deque([1, 2, 3])
dq.append(4)       # Add to right
dq.appendleft(0)   # Add to left
print("Deque after insertions:", dq)
dq.pop()           # Remove from right
dq.popleft()       # Remove from left
print("Deque after deletions:", dq)


# ==============================================================================
# 5. Specialized: Priority Queue
# ==============================================================================
# Elements are dequeued based on their priority, not their insertion order.
print("\n--- 5. Specialized: Priority Queue ---")
# Method A: Using queue.PriorityQueue (Thread-safe)
pq = PriorityQueue()
pq.put((2, "Medium Priority Task"))
pq.put((1, "High Priority Task"))
pq.put((3, "Low Priority Task"))

print("Priority Queue (Thread-safe) popping order:")
while not pq.empty():
    print(pq.get())

# Method B: Using heapq (Not thread-safe, but faster)
print("\nPriority Queue (Using heapq):")
heap = []
heapq.heappush(heap, (2, "Task B"))
heapq.heappush(heap, (1, "Task A"))
heapq.heappush(heap, (3, "Task C"))

while heap:
    print(heapq.heappop(heap))


# ==============================================================================
# 6. Specialized: Circular Queue
# ==============================================================================
# A fixed-size queue where the end connects back to the start.
print("\n--- 6. Specialized: Circular Queue ---")
class CircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.head = self.tail = -1
        self.size = k

    def enqueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.queue[self.tail] = value
        return True

    def dequeue(self) -> bool:
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.size
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.head]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.tail]

    def isEmpty(self) -> bool:
        return self.head == -1

    def isFull(self) -> bool:
        return (self.tail + 1) % self.size == self.head

cq = CircularQueue(3)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
print("Enqueued 10, 20, 30. Is Full?", cq.isFull())
print("Front element:", cq.Front())
cq.dequeue()
cq.enqueue(40)
print("Dequeued once, Enqueued 40. Rear element is now:", cq.Rear())
