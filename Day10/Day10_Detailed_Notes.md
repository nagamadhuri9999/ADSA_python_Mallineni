# Day 10 Detailed Notes: Introduction to Linked Lists

Welcome to Day 10! We are transitioning from simple contiguous data structures (Arrays/Lists) to dynamic, node-based structures. Today, we conquer **Linked Lists**.

---

## 1. Linked Lists vs Arrays

In an Array, elements are stored right next to each other in memory (contiguous). This makes it very fast to access elements by index (`arr[5]`), but very slow to insert elements at the beginning, because every other element must be shifted to the right.

A **Linked List** is different. Elements (called **Nodes**) are scattered randomly in memory. Each node holds its data AND a "pointer" (or reference) to the next node in the list.

### Pros and Cons
| Feature | Arrays | Linked Lists |
| :--- | :--- | :--- |
| **Access by Index** | Fast `O(1)` | Slow `O(n)` |
| **Insert at Beginning** | Slow `O(n)` | Fast `O(1)` |
| **Memory Allocation** | Contiguous (fixed size chunks) | Dynamic (creates nodes as needed) |

---

## 2. The Node Structure

To build a Linked List, we must first build a **Node**. In Python, we use Object-Oriented Programming (Classes) for this.

```python
class Node:
    def __init__(self, data):
        self.data = data    # The value the node holds
        self.next = None    # The pointer to the next node
```

When you create a node: `node1 = Node(5)`, it contains `5` and its `next` pointer points to `None` (meaning it's the end of the line).

---

## 3. Building a Singly Linked List

A Singly Linked List is a chain of nodes where each node points only to the **next** node. We manage the whole list by keeping track of the very first node, called the **Head**.

```python
class LinkedList:
    def __init__(self):
        self.head = None   # The list is initially empty
```

### Visualizing the Chain

```mermaid
graph LR
    A["Head"] --> B["[Data: 10 | Next]"]
    B --> C["[Data: 20 | Next]"]
    C --> D["[Data: 30 | Next]"]
    D --> E["None"]
```

---

## 4. Basic Operations

### A. Traversal (Printing the List)
To walk through a Linked List, we start at the `head` and use a temporary pointer (`current`) to hop from node to node until we hit `None`.

```python
def display(self):
    current = self.head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
```
- **Time Complexity:** O(n)

### B. Insertion at the Head
Inserting at the beginning is incredibly fast. We just make a new node, point it to the current head, and then update the head!

```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head  # 1. Point new node to the old head
    self.head = new_node       # 2. Update head to be the new node
```
- **Time Complexity:** O(1) Constant Time!

### C. Insertion at the Tail (End)
To insert at the end, we have to traverse the whole list to find the last node, then point its `next` to our new node.

```python
def insert_at_end(self, data):
    new_node = Node(data)
    
    if self.head is None:      # If the list is empty
        self.head = new_node
        return
        
    current = self.head
    while current.next is not None:  # Stop AT the last node
        current = current.next
        
    current.next = new_node    # Link the last node to the new node
```
- **Time Complexity:** O(n) Linear Time. *(Note: If we kept a `tail` pointer in our class, this could be O(1)!)*
