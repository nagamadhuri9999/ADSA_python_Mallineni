"""
Day 13: 50+ Basic Linked List Problems & Solutions
This file contains the fundamental operations and 50 extra practice problems
for mastering singly linked lists.
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ==========================================
# 1. Fundamental Calculations
# ==========================================

def get_min(head: Node) -> int:
    if not head: return float('inf')
    min_val = head.val
    while head:
        min_val = min(min_val, head.val)
        head = head.next
    return min_val

def get_max(head: Node) -> int:
    if not head: return float('-inf')
    max_val = head.val
    while head:
        max_val = max(max_val, head.val)
        head = head.next
    return max_val

def get_sum(head: Node) -> int:
    total = 0
    while head:
        total += head.val
        head = head.next
    return total

def get_product(head: Node) -> int:
    if not head: return 0
    product = 1
    while head:
        product *= head.val
        head = head.next
    return product

def get_avg(head: Node) -> float:
    if not head: return 0.0
    total, count = 0, 0
    while head:
        total += head.val
        count += 1
        head = head.next
    return total / count

def get_middle(head: Node) -> Node:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ==========================================
# Extra 50 Basic Problems
# ==========================================

# 1. Length of Linked List (Iterative)
def length_iterative(head: Node) -> int:
    count = 0
    while head:
        count += 1
        head = head.next
    return count

# 2. Length of Linked List (Recursive)
def length_recursive(head: Node) -> int:
    if not head: return 0
    return 1 + length_recursive(head.next)

# 3. Search an Element (Iterative)
def search_iterative(head: Node, key: int) -> bool:
    while head:
        if head.val == key: return True
        head = head.next
    return False

# 4. Search an Element (Recursive)
def search_recursive(head: Node, key: int) -> bool:
    if not head: return False
    if head.val == key: return True
    return search_recursive(head.next, key)

# 5. Get Nth Node
def get_nth_node(head: Node, index: int) -> int:
    count = 0
    while head:
        if count == index: return head.val
        count += 1
        head = head.next
    return -1 # Not found

# 6. Get Nth Node from End
def get_nth_from_end(head: Node, n: int) -> int:
    main_ptr = ref_ptr = head
    for _ in range(n):
        if not ref_ptr: return -1
        ref_ptr = ref_ptr.next
    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    return main_ptr.val if main_ptr else -1

# 7. Count occurrences of a key
def count_key(head: Node, key: int) -> int:
    count = 0
    while head:
        if head.val == key: count += 1
        head = head.next
    return count

# 8. Detect Cycle
def has_cycle(head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: return True
    return False

# 9. Find length of Cycle
def cycle_length(head: Node) -> int:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            temp = slow.next
            length = 1
            while temp != slow:
                temp = temp.next
                length += 1
            return length
    return 0

# 10. Remove Duplicates from Sorted List
def remove_duplicates_sorted(head: Node) -> Node:
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

# 11. Remove Duplicates from Unsorted List
def remove_duplicates_unsorted(head: Node) -> Node:
    if not head: return head
    seen = {head.val}
    curr = head
    while curr.next:
        if curr.next.val in seen:
            curr.next = curr.next.next
        else:
            seen.add(curr.next.val)
            curr = curr.next
    return head

# 12. Swap nodes without swapping data (given keys x and y)
def swap_nodes(head: Node, x: int, y: int) -> Node:
    if x == y: return head
    prevX = None; currX = head
    while currX and currX.val != x:
        prevX = currX; currX = currX.next
    prevY = None; currY = head
    while currY and currY.val != y:
        prevY = currY; currY = currY.next
    if not currX or not currY: return head
    if prevX: prevX.next = currY
    else: head = currY
    if prevY: prevY.next = currX
    else: head = currX
    currX.next, currY.next = currY.next, currX.next
    return head

# 13. Pairwise swap nodes
def pairwise_swap(head: Node) -> Node:
    temp = head
    while temp and temp.next:
        temp.val, temp.next.val = temp.next.val, temp.val
        temp = temp.next.next
    return head

# 14. Move last element to front
def move_last_to_front(head: Node) -> Node:
    if not head or not head.next: return head
    sec_last = None
    last = head
    while last.next:
        sec_last = last
        last = last.next
    sec_last.next = None
    last.next = head
    head = last
    return head

# 15. Intersection of two sorted linked lists
def intersect_sorted(head1: Node, head2: Node) -> Node:
    dummy = Node()
    tail = dummy
    while head1 and head2:
        if head1.val == head2.val:
            tail.next = Node(head1.val)
            tail = tail.next
            head1 = head1.next
            head2 = head2.next
        elif head1.val < head2.val:
            head1 = head1.next
        else:
            head2 = head2.next
    return dummy.next

# 16. Intersection point of two linked lists (Y-shaped)
def get_intersection_node(headA: Node, headB: Node) -> Node:
    if not headA or not headB: return None
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a

# 17. Delete alternate nodes
def delete_alternate(head: Node) -> Node:
    curr = head
    while curr and curr.next:
        curr.next = curr.next.next
        curr = curr.next
    return head

# 18. Alternating split of a list
def alternating_split(head: Node):
    a_dummy = Node(); b_dummy = Node()
    a_tail = a_dummy; b_tail = b_dummy
    curr = head; toggle = True
    while curr:
        if toggle:
            a_tail.next = curr
            a_tail = a_tail.next
        else:
            b_tail.next = curr
            b_tail = b_tail.next
        curr = curr.next
        toggle = not toggle
    a_tail.next = None; b_tail.next = None
    return a_dummy.next, b_dummy.next

# 19. Check if Identical
def is_identical(head1: Node, head2: Node) -> bool:
    while head1 and head2:
        if head1.val != head2.val: return False
        head1 = head1.next
        head2 = head2.next
    return head1 is None and head2 is None

# 20. Reverse a linked list (Iterative)
def reverse_iterative(head: Node) -> Node:
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

# 21. Reverse a linked list (Recursive)
def reverse_recursive(head: Node) -> Node:
    if not head or not head.next: return head
    rest = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

# 22. Reverse in groups of given size (K)
def reverse_k_group(head: Node, k: int) -> Node:
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1
    if count == k:
        curr = reverse_k_group(curr, k)
        while count > 0:
            next_temp = head.next
            head.next = curr
            curr = head
            head = next_temp
            count -= 1
        head = curr
    return head

# 23. Delete nodes which have a greater value on right side
def delete_lesser_nodes(head: Node) -> Node:
    head = reverse_iterative(head)
    curr = head
    max_so_far = head.val if head else float('-inf')
    while curr and curr.next:
        if curr.next.val < max_so_far:
            curr.next = curr.next.next
        else:
            curr = curr.next
            max_so_far = curr.val
    return reverse_iterative(head)

# 24. Segregate even and odd nodes
def segregate_even_odd(head: Node) -> Node:
    even_dummy, odd_dummy = Node(), Node()
    even, odd = even_dummy, odd_dummy
    curr = head
    while curr:
        if curr.val % 2 == 0:
            even.next = curr
            even = even.next
        else:
            odd.next = curr
            odd = odd.next
        curr = curr.next
    even.next = odd_dummy.next
    odd.next = None
    return even_dummy.next

# 25. Add two numbers represented by linked lists (digits reversed)
def add_two_numbers(l1: Node, l2: Node) -> Node:
    dummy = Node()
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next

# 26. Sort a linked list of 0s, 1s and 2s
def sort_012(head: Node) -> Node:
    cnt = [0, 0, 0]
    curr = head
    while curr:
        cnt[curr.val] += 1
        curr = curr.next
    curr = head
    for i in range(3):
        while cnt[i] > 0:
            curr.val = i
            cnt[i] -= 1
            curr = curr.next
    return head

# 27. Print reverse of a linked list
def print_reverse(head: Node):
    if not head: return
    print_reverse(head.next)
    print(head.val, end=" ")

# 28. Remove loop in Linked List
def remove_loop(head: Node) -> Node:
    slow = fast = head
    has_loop = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_loop = True
            break
    if has_loop:
        slow = head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
        else:
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None
    return head

# 29. Add 1 to a number represented as linked list
def add_one(head: Node) -> Node:
    head = reverse_iterative(head)
    curr = head
    carry = 1
    while curr:
        total = curr.val + carry
        curr.val = total % 10
        carry = total // 10
        if not curr.next and carry:
            curr.next = Node(carry)
            carry = 0
        curr = curr.next
    return reverse_iterative(head)

# 30. Check if a linked list is a palindrome
def is_palindrome(head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    left, right = head, prev
    while right:
        if left.val != right.val: return False
        left = left.next
        right = right.next
    return True

# 31. Insert in a sorted linked list
def insert_sorted(head: Node, key: int) -> Node:
    new_node = Node(key)
    if not head or head.val >= key:
        new_node.next = head
        return new_node
    curr = head
    while curr.next and curr.next.val < key:
        curr = curr.next
    new_node.next = curr.next
    curr.next = new_node
    return head

# 32. Delete a node given only its pointer
def delete_node_pointer(node: Node):
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next

# 33. Swap Kth node from beginning with Kth node from end
def swap_kth(head: Node, k: int) -> Node:
    n = length_iterative(head)
    if k > n: return head
    if 2*k - 1 == n: return head # Same node
    x = head; x_prev = None
    for _ in range(k-1):
        x_prev = x
        x = x.next
    y = head; y_prev = None
    for _ in range(n-k):
        y_prev = y
        y = y.next
    if x_prev: x_prev.next = y
    else: head = y
    if y_prev: y_prev.next = x
    else: head = x
    x.next, y.next = y.next, x.next
    return head

# 34. Rotate Linked List by K places
def rotate_list(head: Node, k: int) -> Node:
    if not head or k == 0: return head
    n = length_iterative(head)
    k %= n
    if k == 0: return head
    curr = head
    for _ in range(n - k - 1):
        curr = curr.next
    new_head = curr.next
    curr.next = None
    last = new_head
    while last.next:
        last = last.next
    last.next = head
    return new_head

# 35. Delete N nodes after M nodes
def delete_n_after_m(head: Node, m: int, n: int) -> Node:
    curr = head
    while curr:
        for _ in range(m - 1):
            if curr: curr = curr.next
        if not curr: return head
        temp = curr.next
        for _ in range(n):
            if temp: temp = temp.next
        curr.next = temp
        curr = temp
    return head

# 36. Find fractional node (n/k th node)
def fractional_node(head: Node, k: int) -> Node:
    frac = None
    i = 0
    curr = head
    while curr:
        if i % k == 0:
            if not frac: frac = head
            else: frac = frac.next
        i += 1
        curr = curr.next
    return frac

# 37. Delete the middle node
def delete_middle(head: Node) -> Node:
    if not head or not head.next: return None
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head

# 38. Remove elements with specific value
def remove_elements(head: Node, val: int) -> Node:
    dummy = Node(0, head)
    curr = dummy
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return dummy.next

# 39. Delete all occurrences of a key in doubly linked list (Assuming DLL Node has prev)
# (Skipped for strictly singly LL focus, substituting with SLL alternative)
# 39. Insertion at Specific Position
def insert_at_pos(head: Node, val: int, pos: int) -> Node:
    if pos == 0: return Node(val, head)
    curr = head
    for _ in range(pos - 1):
        if curr: curr = curr.next
    if curr:
        curr.next = Node(val, curr.next)
    return head

# 40. Delete at Specific Position
def delete_at_pos(head: Node, pos: int) -> Node:
    if pos == 0 and head: return head.next
    curr = head
    for _ in range(pos - 1):
        if curr: curr = curr.next
    if curr and curr.next:
        curr.next = curr.next.next
    return head

# 41. Reverse Alternate K Nodes
def reverse_alternate_k(head: Node, k: int) -> Node:
    curr = head
    count = 0
    while curr and count < k:
        curr = curr.next
        count += 1
    if count == k:
        curr = head
        prev = None
        count = 0
        while curr and count < k:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            count += 1
        if head:
            head.next = curr
        count = 0
        while curr and count < k - 1:
            curr = curr.next
            count += 1
        if curr:
            curr.next = reverse_alternate_k(curr.next, k)
        return prev
    return head

# 42. Split a Circular Linked List into two halves (Assumes Circular)
# 43. Flatten a multi-level linked list (Skipped multi-level structs for purely basic)
# 42. Check if list has even or odd number of nodes
def is_even_length(head: Node) -> bool:
    fast = head
    while fast and fast.next:
        fast = fast.next.next
    return fast is None

# 43. Move first element to last
def move_first_to_last(head: Node) -> Node:
    if not head or not head.next: return head
    first = head
    head = head.next
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = first
    first.next = None
    return head

# 44. Get Last Node
def get_last_node(head: Node) -> Node:
    if not head: return None
    while head.next:
        head = head.next
    return head

# 45. Find modular node (last node whose index is divisible by k)
def modular_node(head: Node, k: int) -> Node:
    if k <= 0: return None
    mod_node = None
    i = 1
    curr = head
    while curr:
        if i % k == 0:
            mod_node = curr
        i += 1
        curr = curr.next
    return mod_node

# 46. Find max sum of two consecutive nodes
def max_sum_consecutive(head: Node) -> int:
    if not head or not head.next: return 0
    max_sum = float('-inf')
    curr = head
    while curr.next:
        max_sum = max(max_sum, curr.val + curr.next.val)
        curr = curr.next
    return max_sum

# 47. Sum of last N nodes
def sum_last_n(head: Node, n: int) -> int:
    main_ptr = ref_ptr = head
    for _ in range(n):
        if not ref_ptr: return 0
        ref_ptr = ref_ptr.next
    while ref_ptr:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next
    total = 0
    while main_ptr:
        total += main_ptr.val
        main_ptr = main_ptr.next
    return total

# 48. Print alternate nodes
def print_alternate(head: Node):
    curr = head
    while curr:
        print(curr.val, end=" ")
        if curr.next:
            curr = curr.next.next
        else:
            break

# 49. Find N/Kth node without computing length
def find_n_kth_node(head: Node, k: int) -> Node:
    frac_node = None
    i = 1
    curr = head
    while curr:
        if i % k == 0:
            if not frac_node: frac_node = head
            else: frac_node = frac_node.next
        i += 1
        curr = curr.next
    return frac_node

# 50. Keep only unique elements (Remove duplicates strictly)
def remove_all_duplicates_sorted(head: Node) -> Node:
    dummy = Node(0, head)
    prev = dummy
    curr = head
    while curr:
        if curr.next and curr.val == curr.next.val:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            prev.next = curr.next
        else:
            prev = prev.next
        curr = curr.next
    return dummy.next

# Test suite executing basics to demonstrate functionality
if __name__ == "__main__":
    def create_list(arr):
        dummy = Node()
        curr = dummy
        for val in arr:
            curr.next = Node(val)
            curr = curr.next
        return dummy.next

    head = create_list([10, 20, 30, 40, 50])
    
    print("Testing Fundamental Linked List Calculations...")
    print("List: 10 -> 20 -> 30 -> 40 -> 50")
    print("Min:", get_min(head))
    print("Max:", get_max(head))
    print("Sum:", get_sum(head))
    print("Product:", get_product(head))
    print("Average:", get_avg(head))
    print("Middle Node:", get_middle(head).val)
    print("Length:", length_iterative(head))
