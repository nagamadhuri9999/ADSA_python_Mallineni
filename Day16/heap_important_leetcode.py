import heapq
from collections import Counter

# ==========================================
# IMPORTANT HEAP LEETCODE PROBLEMS
# ==========================================

# 1. Kth Largest Element in an Array (LeetCode 215) - Medium
# Approach: Use a Min-Heap of size k.
def findKthLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]

# 2. Top K Frequent Elements (LeetCode 347) - Medium
# Approach: Count frequencies, then use a Min-Heap of size k based on frequencies.
def topKFrequent(nums, k):
    count = Counter(nums)
    min_heap = []
    for num, freq in count.items():
        # Store as tuple (frequency, element)
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for freq, num in min_heap]

# 3. Last Stone Weight (LeetCode 1046) - Easy
# Approach: Use a Max-Heap to constantly smash the two heaviest stones.
def lastStoneWeight(stones):
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)
    while len(max_heap) > 1:
        s1 = -heapq.heappop(max_heap)
        s2 = -heapq.heappop(max_heap)
        if s1 != s2:
            heapq.heappush(max_heap, -(s1 - s2))
    return -max_heap[0] if max_heap else 0

# 4. Merge K Sorted Lists (LeetCode 23) - Hard
# Approach: Use a Min-Heap. Push the head of each linked list. 
# Pop the smallest, attach to result, and push its next node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # To handle ties in values when pushing to heap, we use the list index 'i'
    # since ListNode doesn't support direct comparison in python3.
    min_heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
            
    dummy = ListNode(0)
    curr = dummy
    
    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
            
    return dummy.next

# Helper methods to build and print linked lists for testing
def build_linked_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    return " -> ".join(res)

# 5. Find Median from Data Stream (LeetCode 295) - Hard
# Approach: Use two heaps. A Max-Heap for the smaller half, Min-Heap for the larger half.
class MedianFinder:
    def __init__(self):
        # max_heap stores the smaller half (invert values)
        self.small = []
        # min_heap stores the larger half
        self.large = []

    def addNum(self, num):
        # Push to max heap first
        heapq.heappush(self.small, -num)
        
        # Make sure every element in small is <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
            
        # Balance sizes: small can have at most 1 more element than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0

