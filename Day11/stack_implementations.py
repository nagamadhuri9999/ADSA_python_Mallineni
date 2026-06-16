"""
Comprehensive Stack Implementations in Python
=============================================
This file demonstrates various ways to implement a Stack in Python,
including its variations and different underlying data structures.
"""

from collections import deque
from queue import LifoQueue

# ==============================================================================
# 1. Stack Implementation using Python's built-in `list`
# ==============================================================================
# Pros: Easy to use, built-in.
# Cons: Can run into speed issues as it grows (due to memory reallocation).
print("--- 1. Stack using list ---")
stack_list = []
stack_list.append('A')  # Push
stack_list.append('B')
stack_list.append('C')
print("Initial stack:", stack_list)
print("Popped:", stack_list.pop())  # Pop
print("Stack after pop:", stack_list)


# ==============================================================================
# 2. Stack Implementation using `collections.deque`
# ==============================================================================
# Pros: O(1) time complexity for append and pop operations. Best choice for stacks.
# Cons: Slightly more memory overhead than list.
print("\n--- 2. Stack using collections.deque ---")
stack_deque = deque()
stack_deque.append('X')  # Push
stack_deque.append('Y')
stack_deque.append('Z')
print("Initial stack:", stack_deque)
print("Popped:", stack_deque.pop())  # Pop
print("Stack after pop:", stack_deque)


# ==============================================================================
# 3. Stack Implementation using `queue.LifoQueue`
# ==============================================================================
# Pros: Thread-safe, great for multi-threading environments.
# Cons: Slower than deque due to thread-safety locking mechanisms.
print("\n--- 3. Stack using queue.LifoQueue ---")
stack_lifo = LifoQueue(maxsize=3)
stack_lifo.put('Apple')  # Push
stack_lifo.put('Banana')
stack_lifo.put('Cherry')
print("Is stack full?", stack_lifo.full())
print("Popped:", stack_lifo.get())  # Pop


# ==============================================================================
# 4. Stack Implementation using a Custom Linked List
# ==============================================================================
# Pros: Dynamic size, no memory reallocation needed.
# Cons: Requires writing custom classes, overhead of Node objects.
print("\n--- 4. Stack using Custom Linked List ---")
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        popped = self.head.data
        self.head = self.head.next
        return popped

    def peek(self):
        return self.head.data if self.head else None

ll_stack = LinkedListStack()
ll_stack.push(10)
ll_stack.push(20)
ll_stack.push(30)
print("Peek top element:", ll_stack.peek())
print("Popped:", ll_stack.pop())
print("Peek top after pop:", ll_stack.peek())

# ==============================================================================
# 5. Specialized Stack Types: Min Stack
# ==============================================================================
# A Stack that supports push, pop, top, and retrieving the minimum element in constant time.
print("\n--- 5. Specialized: Min Stack ---")
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

min_st = MinStack()
min_st.push(-2)
min_st.push(0)
min_st.push(-3)
print("Current Minimum:", min_st.getMin()) # Returns -3
min_st.pop()
print("Minimum after pop:", min_st.getMin()) # Returns -2
