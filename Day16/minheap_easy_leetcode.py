import heapq

# ==========================================
# MIN HEAP EASY LEETCODE PROBLEMS
# ==========================================

# Problem 1: Kth Largest Element in a Stream (LeetCode 703)
# Difficulty: Easy
# Description: Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Approach: Maintain a Min-Heap of size k. The smallest element in the heap (root) 
# will always be the kth largest element seen so far.

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val):
        heapq.heappush(self.min_heap, val)
        # If heap size exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        # The root of the heap is the kth largest element
        return self.min_heap[0]




class KthSmallest:

    def __init__(self, k, nums):
        self.k = k
        self.max_heap = []

        for num in nums:
            self.add(num)

    def add(self, val):
        # Store negative values to simulate a max heap
        heapq.heappush(self.max_heap, -val)

        # Keep only k smallest elements
        if len(self.max_heap) > self.k:
            heapq.heappop(self.max_heap)

        # Root of max heap = kth smallest element
        return -self.max_heap[0]
