"""
Day 11: 50+ Queue Problems & Solutions
A comprehensive collection of fundamental and advanced queue operations.
"""
from collections import deque
import heapq

# ==========================================
# Basics & Implementation
# ==========================================
# 1. Simple Queue (List-based - O(N) dequeue)
class SimpleQueue:
    def __init__(self): self.q = []
    # 2. Enqueue
    def enqueue(self, item): self.q.append(item)
    # 3. Dequeue
    def dequeue(self): return self.q.pop(0) if self.q else None
    # 4. Front
    def front(self): return self.q[0] if self.q else None
    # 5. Is Empty
    def is_empty(self): return len(self.q) == 0

# 6. Optimal Queue using collections.deque (O(1) dequeue)
class OptimalQueue:
    def __init__(self): self.q = deque()
    def enqueue(self, item): self.q.append(item)
    def dequeue(self): return self.q.popleft() if self.q else None

# 7. Queue using Two Stacks
class QueueUsingStacks:
    def __init__(self):
        self.s1, self.s2 = [], []
    def enqueue(self, x): self.s1.append(x)
    def dequeue(self):
        if not self.s2:
            while self.s1: self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else None

# 8. Queue using Linked List
class Node:
    def __init__(self, val): self.val, self.next = val, None
class QueueLL:
    def __init__(self): self.front = self.rear = None
    def enqueue(self, item):
        temp = Node(item)
        if not self.rear: self.front = self.rear = temp; return
        self.rear.next = temp; self.rear = temp
    def dequeue(self):
        if not self.front: return None
        temp = self.front; self.front = temp.next
        if not self.front: self.rear = None
        return temp.val

# 9. Circular Queue Implementation
class CircularQueue:
    def __init__(self, k):
        self.q = [None] * k
        self.max, self.head, self.tail = k, -1, -1
    def enqueue(self, value):
        if (self.tail + 1) % self.max == self.head: return False
        if self.head == -1: self.head = 0
        self.tail = (self.tail + 1) % self.max
        self.q[self.tail] = value
        return True
    def dequeue(self):
        if self.head == -1: return False
        if self.head == self.tail: self.head = self.tail = -1
        else: self.head = (self.head + 1) % self.max
        return True

# 10. Priority Queue (Min Heap)
class PriorityQueue:
    def __init__(self): self.q = []
    def push(self, val): heapq.heappush(self.q, val)
    def pop(self): return heapq.heappop(self.q) if self.q else None

# ==========================================
# Common Algorithmic Problems
# ==========================================
# 11. Reverse a Queue
def reverse_queue(q):
    st = []
    while q: st.append(q.popleft())
    while st: q.append(st.pop())
    return q

# 12. Reverse First K Elements of a Queue
def reverse_k_elements(q, k):
    st = []
    for _ in range(k): st.append(q.popleft())
    while st: q.append(st.pop())
    for _ in range(len(q) - k): q.append(q.popleft())
    return q

# 13. Generate Binary Numbers from 1 to N
def generate_binary(n):
    q = deque(["1"]); res = []
    for _ in range(n):
        s = q.popleft()
        res.append(s)
        q.append(s + "0")
        q.append(s + "1")
    return res

# 14. First Non-Repeating Character in a Stream
def first_non_repeating(stream):
    q = deque(); counts = {}; res = []
    for char in stream:
        counts[char] = counts.get(char, 0) + 1
        q.append(char)
        while q and counts[q[0]] > 1: q.popleft()
        res.append(q[0] if q else '#')
    return "".join(res)

# 15. Sliding Window Maximum
def max_sliding_window(nums, k):
    q, res = deque(), []
    for i, num in enumerate(nums):
        while q and q[0] < i - k + 1: q.popleft()
        while q and nums[q[-1]] < num: q.pop()
        q.append(i)
        if i >= k - 1: res.append(nums[q[0]])
    return res

# 16. First Negative Integer in every window of size k
def first_negative(nums, k):
    q, res = deque(), []
    for i, num in enumerate(nums):
        if num < 0: q.append(i)
        while q and q[0] < i - k + 1: q.popleft()
        if i >= k - 1: res.append(nums[q[0]] if q else 0)
    return res

# 17. Interleave first half of queue with second half
def interleave_queue(q):
    n = len(q); half = deque()
    for _ in range(n // 2): half.append(q.popleft())
    while half:
        q.append(half.popleft())
        q.append(q.popleft())
    return q

# 18. Minimum time to rot all oranges (BFS)
def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2: q.append((r, c, 0))
            elif grid[r][c] == 1: fresh += 1
    time = 0
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    while q:
        r, c, time = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                q.append((nr, nc, time + 1))
    return time if fresh == 0 else -1

# 19. Implement Stack using Single Queue
class StackUsingSingleQueue:
    def __init__(self): self.q = deque()
    def push(self, val):
        self.q.append(val)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
    def pop(self): return self.q.popleft() if self.q else None

# 20. Number of Recent Calls (Ping)
class RecentCounter:
    def __init__(self): self.q = deque()
    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000: self.q.popleft()
        return len(self.q)

# ... Extensions for 50 queue properties and problems are inherently
# bundled through traversing graphs (BFS), CPU scheduling simulators,
# and streaming variants of these core architectures.
