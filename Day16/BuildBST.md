# Day 16: Build a Binary Search Tree (BST)

## Problem Statement
Build a Binary Search Tree from a given set of elements.

### Example
**Input elements**: `[5, 3, 7, 2, 4, 6, 8]`

**Resulting BST**:
```text
        5
       / \
      3   7
     / \ / \
    2  4 6  8
```
**In-order**: `2, 3, 4, 5, 6, 7, 8`

---

## Python Logic

```python
values = list(map(int, input().split()))

class Node:
    def __init__(self, value):
        self.data = value 
        self.left = None 
        self.right = None 

root = None 

def insert(root, value):
    if root is None:
        root = Node(value)
    elif value < root.data:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root 

for i in values[:len(values)-1]:
    root = insert(root, i)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

inorder(root)
```

---

## Interactive Visualization

To understand how the recursive calls dynamically build the tree node by node, explore the interactive visualization link:

> **[Recursive Tree Explorer (Build BST)](https://recursive-tree-explorer.lovable.app)**
