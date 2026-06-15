# Day 10 Practice Problems: Introduction to Linked Lists
# Fill in the TODOs in each problem. Check the bottom of the snippet for the solution.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# ==========================================
# Problems 1-10: Basic Setup & Traversal
# ==========================================

def problem_1_create_node():
    # TODO: Create a Node holding the value 42 and print its data.
    pass

    # --- SOLUTION ---
    # node = Node(42)
    # print(node.data)


def problem_2_link_two_nodes():
    # TODO: Create two nodes (val 10, val 20). Link the first to the second.
    pass

    # --- SOLUTION ---
    # n1 = Node(10)
    # n2 = Node(20)
    # n1.next = n2


def problem_3_create_linked_list():
    # TODO: Initialize an empty LinkedList object. Check if its head is None.
    pass

    # --- SOLUTION ---
    # ll = LinkedList()
    # print(ll.head is None)


def problem_4_manual_list_creation():
    # TODO: Create a LinkedList, set head to Node(1), link head.next to Node(2).
    pass

    # --- SOLUTION ---
    # ll = LinkedList()
    # ll.head = Node(1)
    # ll.head.next = Node(2)


def problem_5_traverse_and_print():
    # TODO: Given a LinkedList `ll`, write a while loop to print all node data.
    pass

    # --- SOLUTION ---
    # current = ll.head
    # while current is not None:
    #     print(current.data)
    #     current = current.next


def problem_6_count_nodes():
    # TODO: Given a LinkedList `ll`, traverse it and return the total number of nodes.
    pass

    # --- SOLUTION ---
    # current = ll.head
    # count = 0
    # while current is not None:
    #     count += 1
    #     current = current.next
    # return count


def problem_7_search_node():
    # TODO: Write a function that returns True if `target` exists in the LinkedList.
    pass

    # --- SOLUTION ---
    # def search(ll, target):
    #     current = ll.head
    #     while current:
    #         if current.data == target: return True
    #         current = current.next
    #     return False


def problem_8_get_tail():
    # TODO: Traverse to the last node of the list and return its data. Return None if empty.
    pass

    # --- SOLUTION ---
    # def get_tail_data(ll):
    #     if not ll.head: return None
    #     current = ll.head
    #     while current.next: # Stop AT the last node
    #         current = current.next
    #     return current.data


def problem_9_sum_nodes():
    # TODO: Return the sum of all node values in a LinkedList of integers.
    pass

    # --- SOLUTION ---
    # def sum_list(ll):
    #     total = 0
    #     current = ll.head
    #     while current:
    #         total += current.data
    #         current = current.next
    #     return total


def problem_10_find_max():
    # TODO: Return the maximum value in a LinkedList.
    pass

    # --- SOLUTION ---
    # def find_max(ll):
    #     if not ll.head: return None
    #     max_val = ll.head.data
    #     current = ll.head.next
    #     while current:
    #         if current.data > max_val: max_val = current.data
    #         current = current.next
    #     return max_val


# ==========================================
# Problems 11-20: Insertions & Modifications
# ==========================================

def problem_11_insert_at_head():
    # TODO: Add a method to LinkedList class: `def insert_head(self, data):`
    pass

    # --- SOLUTION ---
    # def insert_head(self, data):
    #     new_node = Node(data)
    #     new_node.next = self.head
    #     self.head = new_node


def problem_12_insert_at_tail():
    # TODO: Add a method to LinkedList class: `def insert_tail(self, data):`
    pass

    # --- SOLUTION ---
    # def insert_tail(self, data):
    #     new_node = Node(data)
    #     if not self.head:
    #         self.head = new_node
    #         return
    #     current = self.head
    #     while current.next:
    #         current = current.next
    #     current.next = new_node


def problem_13_insert_after_node():
    # TODO: Given a specific Node object `prev_node` and `data`, insert a new node right after it.
    pass

    # --- SOLUTION ---
    # def insert_after(prev_node, data):
    #     if not prev_node: return
    #     new_node = Node(data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node


def problem_14_delete_head():
    # TODO: Remove the head node from the LinkedList and return its data.
    pass

    # --- SOLUTION ---
    # def delete_head(self):
    #     if not self.head: return None
    #     val = self.head.data
    #     self.head = self.head.next
    #     return val


def problem_15_delete_tail():
    # TODO: Traverse to the end and remove the last node. (Hint: stop at the SECOND to last node).
    pass

    # --- SOLUTION ---
    # def delete_tail(self):
    #     if not self.head: return None
    #     if not self.head.next:
    #         val = self.head.data
    #         self.head = None
    #         return val
    #     current = self.head
    #     while current.next.next: # Stop at second to last
    #         current = current.next
    #     val = current.next.data
    #     current.next = None
    #     return val


def problem_16_build_from_list():
    # TODO: Given a Python list `[1, 2, 3]`, build a LinkedList holding these values in order.
    pass

    # --- SOLUTION ---
    # def build_ll(arr):
    #     ll = LinkedList()
    #     for val in reversed(arr): # Insert at head is O(1)
    #         ll.insert_head(val)
    #     return ll


def problem_17_convert_to_list():
    # TODO: Traverse a LinkedList and append all values into a standard Python list, returning it.
    pass

    # --- SOLUTION ---
    # def to_list(ll):
    #     res = []
    #     current = ll.head
    #     while current:
    #         res.append(current.data)
    #         current = current.next
    #     return res


def problem_18_clear_list():
    # TODO: Remove all nodes from the LinkedList (in Python, just remove the head reference!).
    pass

    # --- SOLUTION ---
    # def clear(self):
    #     self.head = None # Garbage collector handles the rest


def problem_19_replace_value():
    # TODO: Traverse the list and replace all occurrences of `old_val` with `new_val`.
    pass

    # --- SOLUTION ---
    # def replace(ll, old_val, new_val):
    #     current = ll.head
    #     while current:
    #         if current.data == old_val:
    #             current.data = new_val
    #         current = current.next


def problem_20_print_formatted():
    # TODO: Print the list exactly like "1 -> 2 -> 3 -> None".
    pass

    # --- SOLUTION ---
    # def print_ll(ll):
    #     current = ll.head
    #     while current:
    #         print(f"{current.data} -> ", end="")
    #         current = current.next
    #     print("None")


if __name__ == "__main__":
    print("Welcome to Day 10 Practice Problems!")
