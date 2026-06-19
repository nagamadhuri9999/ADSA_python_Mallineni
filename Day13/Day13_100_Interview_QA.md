# Day 13: 100 Interview Questions and Answers on Linked Lists

## Section 1: Linked List Basics
1. **What is a Linked List?** A linear data structure where elements (nodes) are stored in non-contiguous memory locations.
2. **What does a Node contain?** Data and a pointer/reference to the next node.
3. **What is the "Head"?** A pointer to the first node of the linked list.
4. **What does the last node point to?** `Null` (or `None` in Python).
5. **How does an Array differ from a Linked List?** Arrays are contiguous and fixed-size (usually); Linked Lists are non-contiguous and dynamic.
6. **What is the time complexity to access the Nth element?** O(N) for Linked Lists, O(1) for Arrays.
7. **What is the time complexity to insert at the head?** O(1).
8. **What is the time complexity to insert at the tail (without a tail pointer)?** O(N).
9. **What is the time complexity to insert at the tail (with a tail pointer)?** O(1).
10. **Why use a Linked List over an Array?** Efficient insertions/deletions without shifting elements; dynamic size.

## Section 2: Types of Linked Lists
11. **What is a Singly Linked List (SLL)?** Nodes contain data and one pointer to the next node. Traversal is unidirectional.
12. **What is a Doubly Linked List (DLL)?** Nodes contain data, a pointer to the next node, and a pointer to the previous node.
13. **What is the advantage of a DLL?** You can traverse in both directions and delete a node easily if given only its pointer.
14. **What is the disadvantage of a DLL?** Takes more memory (extra pointer) and requires more pointer manipulations during insertions/deletions.
15. **What is a Circular Linked List (CLL)?** The last node points back to the first node instead of `Null`.
16. **Can a DLL be circular?** Yes, the last node's next points to the head, and the head's prev points to the last node.
17. **What is a "Dummy" or "Sentinel" node?** A fake node placed at the head (or tail) to simplify edge cases (like inserting into an empty list).
18. **Why are Dummy nodes heavily used in LeetCode problems?** They prevent the need for writing specific `if head is None:` logic.
19. **What is an unrolled linked list?** A variation where each node stores an array of elements instead of just one element, improving cache locality.
20. **What is a Skip List?** A layered linked list that allows for binary-search-like O(log N) lookup times.

## Section 3: Singly Linked List Operations
21. **How do you find the length of a SLL?** Traverse from head to tail, incrementing a counter. O(N).
22. **How to insert after a given node `prev_node`?** `new_node.next = prev_node.next; prev_node.next = new_node`.
23. **How to delete the head node?** `head = head.next`.
24. **How to delete a node given the previous node?** `prev_node.next = prev_node.next.next`.
25. **Can you delete a node given ONLY its pointer (not head, not prev)?** Yes, copy the data from the next node into it, then delete the next node (fails if it's the tail).
26. **How to reverse a SLL iteratively?** Maintain `prev`, `curr`, `next`. Loop: `next = curr.next`, `curr.next = prev`, `prev = curr`, `curr = next`.
27. **What is the time and space complexity of iterative reversal?** O(N) Time, O(1) Space.
28. **How to reverse a SLL recursively?** Reverse the rest of the list, then make `head.next.next = head` and `head.next = None`.
29. **What is the space complexity of recursive reversal?** O(N) due to the call stack.
30. **How do you print a SLL in reverse without modifying it?** Use recursion or a Stack.

## Section 4: Two-Pointer Techniques (Fast & Slow)
31. **What is the Fast & Slow pointer approach?** Two pointers move at different speeds (usually 1 step and 2 steps).
32. **Also known as?** Floyd's Tortoise and Hare algorithm.
33. **How to find the middle of a SLL in one pass?** Fast moves 2 steps, Slow moves 1. When Fast reaches the end, Slow is at the middle.
34. **How to detect a cycle in a SLL?** If Fast and Slow pointers ever meet, there is a cycle.
35. **How to find the starting node of a cycle?** Detect cycle. Reset one pointer to head. Move both at 1 step. Where they meet is the start.
36. **Why does the cycle start-finding math work?** The distance from head to cycle start equals the distance from the meeting point to cycle start.
37. **How to find the length of a cycle?** Once they meet, keep one pointer still and move the other by 1 until they meet again, counting steps.
38. **How to find the Nth node from the end in one pass?** Move pointer A forward by N steps. Then move A and B together. When A hits the end, B is at the Nth from end.
39. **How to check if a SLL is a palindrome?** Find middle, reverse the second half, compare both halves.
40. **Does checking a palindrome modify the list?** Temporarily yes. It should be reversed back after checking to restore the structure.

## Section 5: Merging and Sorting
41. **How to merge two sorted SLLs?** Use a dummy node. Compare heads of both lists, attach the smaller one, move its pointer. O(N+M).
42. **How to merge K sorted linked lists?** Use a Min-Heap (Priority Queue) or Divide and Conquer. O(N log K).
43. **What is the best sorting algorithm for Linked Lists?** Merge Sort.
44. **Why is Merge Sort better than Quick Sort for SLLs?** It doesn't require random access and can be done without extra O(N) space.
45. **How to implement Merge Sort on a SLL?** Find middle, split into two lists, recursively sort, then merge two sorted lists.
46. **What is the time complexity of Merge Sort on SLL?** O(N log N).
47. **Can we use Insertion Sort on a SLL?** Yes, it is very effective for small lists.
48. **How to find the intersection point of two Y-shaped SLLs?** Find lengths, advance the longer list by the difference, then move both until they meet.
49. **What is the "Two-Pointer Swap" trick for intersection?** Pointer A traverses List A then List B. Pointer B traverses List B then List A. They meet at the intersection.
50. **How to remove duplicates from a sorted SLL?** Compare `curr` and `curr.next`. If equal, bypass `curr.next`.

## Section 6: Advanced Pointer Manipulation
51. **How to remove duplicates from an unsorted SLL?** Use a Hash Set to track seen values. O(N) Time, O(N) Space.
52. **Can you remove unsorted duplicates in O(1) space?** Yes, using two nested loops, but it takes O(N^2) time.
53. **How to pairwise swap nodes?** Swap the data (easy but bad practice) OR adjust pointers: `curr.next = next.next; next.next = curr`.
54. **How to reverse in groups of K?** Check if K nodes exist. Reverse those K nodes. Recursively call for the rest.
55. **How to segregate even and odd nodes?** Create two dummy lists (even and odd), traverse and distribute nodes, then link even tail to odd head.
56. **How to rotate a SLL by K places?** Find length N. Make it circular. Break the circle at N - (K % N).
57. **How to add two numbers represented by SLLs (digits in reverse)?** Traverse both, add values + carry, create new nodes.
58. **What if the digits are in normal forward order?** Reverse both lists first, or use a Stack, or use recursion.
59. **How to clone a SLL with random pointers?** Interweave cloned nodes next to original nodes, copy random pointers, then extract the cloned list. O(N) time, O(1) space.
60. **What is the alternative to interweaving for random pointer cloning?** Use a Hash Map to map original nodes to cloned nodes. O(N) space.

## Section 7: Doubly Linked Lists
61. **How to insert at the head of a DLL?** `new.next = head; head.prev = new; head = new`.
62. **How to delete a node in a DLL given its pointer?** `node.prev.next = node.next; node.next.prev = node.prev`.
63. **How to reverse a DLL?** Swap the `next` and `prev` pointers of every node.
64. **What is an LRU Cache?** Least Recently Used cache.
65. **How is an LRU Cache implemented optimally?** Using a Hash Map + Doubly Linked List.
66. **Why a DLL for LRU Cache?** Allows O(1) deletion of a node from the middle when it is accessed (to move it to the front).
67. **Can an LRU Cache use a SLL?** No, because removing from the middle of a SLL takes O(N) without the previous pointer.
68. **What is an LFU Cache?** Least Frequently Used cache. Uses frequencies mapped to multiple DLLs.
69. **How to find the middle of a DLL?** Move one pointer from head and one from tail until they meet or cross.
70. **Why use an XOR Linked List?** It simulates a DLL using only one pointer field by storing the bitwise XOR of prev and next addresses (saves memory).

## Section 8: Edge Cases and Debugging
71. **What is the most common error when working with Linked Lists?** `NullPointerException` or `AttributeError` (trying to access `node.next` when `node` is `None`).
72. **How to prevent it?** Always check `if curr is not None` before `curr.next`.
73. **Why do we need a separate `prev` pointer during SLL traversal?** Because we cannot look backward.
74. **What happens if you lose the head pointer?** The entire linked list is lost to memory (garbage collected in Python, memory leak in C).
75. **What is a "Memory Leak" in Linked Lists?** Allocating memory for nodes but failing to free them when deleting (relevant in C/C++).
76. **How does Python handle deleted nodes?** The Garbage Collector automatically destroys objects with zero references.
77. **Why must `tail.next` be explicitly set to `None` when building a list?** Otherwise, it might point to garbage memory or create an infinite loop.
78. **What if a cycle exists and you try to print the list?** Infinite loop.
79. **How to flatten a multi-level linked list?** Treat `child` pointers like a Depth-First Search or use a Stack.
80. **What is the "Runner" technique?** Another name for the fast/slow two-pointer technique.

## Section 9: Memory and System Level
81. **Why do Linked Lists have poor Cache Locality?** Nodes are scattered in memory, causing cache misses, unlike contiguous arrays.
82. **Because of cache locality, are arrays or linked lists faster in practice?** Arrays/Lists in Python are often faster for iteration despite O(N) theoretical limits, due to CPU caching.
83. **When does Linked List definitively beat an Array?** High frequency of middle/head insertions/deletions on massive datasets.
84. **What is Dynamic Memory Allocation?** Allocating memory at runtime (Heap memory), which is how Linked List nodes are created.
85. **Can a Linked List be stored in an Array?** Yes, by keeping parallel arrays for `data` and `next_index`.
86. **Why would you store a LL in an Array?** To combine dynamic linking logic with strict contiguous memory allocation.
87. **What is the space complexity of a SLL?** O(N).
88. **What is the overhead per node?** The size of the pointer(s) (usually 8 bytes on 64-bit systems per pointer).
89. **What is a self-organizing list?** A list that reorders its elements based on access frequency (e.g., Move-to-front heuristic).
90. **Is Python's built-in `list` a Linked List?** No, it is a dynamic array.

## Section 10: General Interview Trivia
91. **What is the time complexity of building a SLL of N items?** O(N) if keeping a tail pointer.
92. **How do you find the minimum/maximum in a SLL?** O(N) full traversal.
93. **Can you binary search a Linked List?** No, because random access is O(N), ruining the O(log N) math.
94. **What structure fixes the binary search issue?** A Skip List or a Binary Search Tree.
95. **How to swap the Kth node from beginning with Kth node from end?** Find both using two passes, keep track of their previous nodes, and rewire 4 pointers.
96. **How to delete alternate nodes?** `curr.next = curr.next.next; curr = curr.next`.
97. **What is Josephus Circle?** Mathematical problem solved by a Circular Linked List eliminating every Kth node.
98. **How to flatten a linked list with `next` and `bottom` pointers?** Recursively merge the `bottom` lists using Merge Sort logic.
99. **If you have an array and a linked list of the same size, which takes more memory?** Linked List, due to the pointer overhead per element.
100. **Why are Linked Lists essential to learn?** They build the foundation for Trees, Graphs, Hash Collision resolution (Chaining), and pointer manipulation skills!
