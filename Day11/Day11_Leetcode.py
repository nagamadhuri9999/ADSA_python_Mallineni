"""
Day 11: Stack and Queue LeetCode Problems
=========================================
This file contains 20 classic LeetCode problems related to Stacks and Queues.
Each solution is optimized and uses Python's built-in lists or collections.deque.
"""
from collections import deque
from typing import List

# ==========================================
# 1. Valid Parentheses (LeetCode 20)
# ==========================================
def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack

# ==========================================
# 2. Min Stack (LeetCode 155)
# ==========================================
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

# ==========================================
# 3. Implement Stack using Queues (LeetCode 225)
# ==========================================
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

# ==========================================
# 4. Implement Queue using Stacks (LeetCode 232)
# ==========================================
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self.peek()
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

# ==========================================
# 5. Simplify Path (LeetCode 71)
# ==========================================
def simplifyPath(path: str) -> str:
    stack = []
    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif p and p != ".":
            stack.append(p)
    return "/" + "/".join(stack)

# ==========================================
# 6. Evaluate Reverse Polish Notation (LeetCode 150)
# ==========================================
def evalRPN(tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

# ==========================================
# 7. Daily Temperatures (LeetCode 739) - Monotonic Stack
# ==========================================
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)
    stack = [] # stores indices
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            prev_idx = stack.pop()
            ans[prev_idx] = i - prev_idx
        stack.append(i)
    return ans

# ==========================================
# 8. Largest Rectangle in Histogram (LeetCode 84)
# ==========================================
def largestRectangleArea(heights: List[int]) -> int:
    stack = [] # (index, height)
    max_area = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
    return max_area

# ==========================================
# 9. Sliding Window Maximum (LeetCode 239) - Monotonic Queue
# ==========================================
def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    output = []
    q = deque() # indices
    l = r = 0
    while r < len(nums):
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)
        if l > q[0]:
            q.popleft()
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1
        r += 1
    return output

# ==========================================
# 10. Number of Recent Calls (LeetCode 933)
# ==========================================
class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# ==========================================
# 11. Design Circular Queue (LeetCode 622)
# ==========================================
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [0] * k
        self.head = 0
        self.count = 0
        self.capacity = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.capacity

# ==========================================
# 12. Design Circular Deque (LeetCode 641)
# ==========================================
class MyCircularDeque:
    def __init__(self, k: int):
        self.q = [0] * k
        self.front = 0
        self.rear = 0
        self.size = 0
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.front = (self.front - 1) % self.k
        self.q[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.q[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.rear = (self.rear - 1) % self.k
        self.size -= 1
        return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.q[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k

# ==========================================
# 13. Remove All Adjacent Duplicates In String (LeetCode 1047)
# ==========================================
def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

# ==========================================
# 14. Remove All Adjacent Duplicates in String II (LeetCode 1209)
# ==========================================
def removeDuplicatesII(s: str, k: int) -> str:
    stack = [] # [char, count]
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
        else:
            stack.append([char, 1])
        if stack[-1][1] == k:
            stack.pop()
    return "".join(c * cnt for c, cnt in stack)

# ==========================================
# 15. First Unique Character in a String (LeetCode 387)
# ==========================================
def firstUniqChar(s: str) -> int:
    from collections import Counter
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1

# ==========================================
# 16. Moving Average from Data Stream (LeetCode 346 - Premium/Concept)
# ==========================================
class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.window_sum -= self.q.popleft()
        self.q.append(val)
        self.window_sum += val
        return self.window_sum / len(self.q)

# ==========================================
# 17. Time Needed to Buy Tickets (LeetCode 2073)
# ==========================================
def timeRequiredToBuy(tickets: List[int], k: int) -> int:
    time = 0
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)
    return time

# ==========================================
# 18. Backspace String Compare (LeetCode 844)
# ==========================================
def backspaceCompare(s: str, t: str) -> bool:
    def build(string):
        res = []
        for c in string:
            if c != '#':
                res.append(c)
            elif res:
                res.pop()
        return "".join(res)
    return build(s) == build(t)

# ==========================================
# 19. Next Greater Element I (LeetCode 496)
# ==========================================
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    next_greater = {}
    stack = []
    for num in nums2:
        while stack and stack[-1] < num:
            next_greater[stack.pop()] = num
        stack.append(num)
    
    return [next_greater.get(n, -1) for n in nums1]

# ==========================================
# 20. Next Greater Element II (LeetCode 503)
# ==========================================
def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    stack = []
    for i in range(n * 2):
        while stack and nums[stack[-1]] < nums[i % n]:
            res[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)
    return res

if __name__ == "__main__":
    print("All 20 Stack & Queue LeetCode algorithms have been initialized successfully.")
