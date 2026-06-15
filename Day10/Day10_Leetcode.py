# Day 10 Leetcode Problems: Introduction to Linked Lists
# These problems test your ability to traverse a Linked List.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ==================================================
# Problem 1: Leetcode 1290 - Convert Binary Number in a Linked List to Integer
# Difficulty: Easy
# ==================================================
# Given `head` which is a reference node to a singly-linked list.
# The value of each node in the linked list is either 0 or 1.
# The linked list holds the binary representation of a number.
# Return the decimal value of the number in the linked list.

def getDecimalValue(head: ListNode) -> int:
    # We traverse the linked list and shift our result bitwise
    # (or multiply by 2) for each new digit we encounter.
    
    num = 0
    current = head
    while current:
        num = num * 2 + current.val
        current = current.next
        
    return num

# Dry Run for list: 1 -> 0 -> 1 (which is binary for 5)
# num = 0
# Node(1): num = 0 * 2 + 1 = 1
# Node(0): num = 1 * 2 + 0 = 2
# Node(1): num = 2 * 2 + 1 = 5
# Return 5.


# ==================================================
# Problem 2: Leetcode 876 - Middle of the Linked List
# Difficulty: Easy
# ==================================================
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

def middleNode(head: ListNode) -> ListNode:
    # Approach 1: Count all nodes (O(n)), then traverse to count // 2.
    # Approach 2: "Tortoise and Hare" (Fast & Slow Pointers).
    # The fast pointer moves 2 steps, slow moves 1 step. 
    # When fast reaches the end, slow is exactly in the middle!
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next          # moves 1 step
        fast = fast.next.next     # moves 2 steps
        
    return slow

# Dry Run for list: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Init: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=5
# Step 3: fast.next is None. Loop ends.
# Return slow (Node 3).


if __name__ == "__main__":
    # Test Problem 1
    ll1 = ListNode(1, ListNode(0, ListNode(1)))
    print("Decimal Value (101):", getDecimalValue(ll1))
    
    # Test Problem 2
    ll2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print("Middle Node (1->2->3->4->5):", middleNode(ll2).val)
