"""
Day 12: Linked List Implementations of Circular Queue and Deque
"""

# ==========================================
# 1. Circular Queue using a Circular Linked List
# ==========================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        # In a circular linked list queue, we only need to keep track of the rear node.
        # The front node is always rear.next
        self.rear = None
        self.count = 0

    def enQueue(self, value: int) -> bool:
        new_node = Node(value)
        if self.isEmpty():
            self.rear = new_node
            self.rear.next = self.rear # Points to itself
        else:
            # new_node points to the front
            new_node.next = self.rear.next
            # old rear points to new_node
            self.rear.next = new_node
            # update rear to be the new_node
            self.rear = new_node
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        # If there's only one node
        if self.rear == self.rear.next:
            self.rear = None
        else:
            # The new front is the old front's next
            front = self.rear.next
            self.rear.next = front.next
            
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.next.value

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.rear is None
        
    def getSize(self) -> int:
        return self.count

# ==========================================
# 2. Deque using a Doubly Linked List
# ==========================================

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DequeDoublyLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def insertFront(self, value: int) -> bool:
        new_node = DoubleNode(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        new_node = DoubleNode(value)
        if self.isEmpty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear: # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear: # Only one element
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        self.count -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.value

    def isEmpty(self) -> bool:
        return self.front is None

if __name__ == "__main__":
    print("Testing Circular Queue (Linked List)...")
    cq = CircularQueueLinkedList()
    cq.enQueue(10)
    cq.enQueue(20)
    cq.enQueue(30)
    print("Front:", cq.Front(), "Rear:", cq.Rear()) # 10, 30
    cq.deQueue()
    print("Front after 1 deQueue:", cq.Front()) # 20
    
    print("\nTesting Deque (Doubly Linked List)...")
    dq = DequeDoublyLinkedList()
    dq.insertLast(1)
    dq.insertLast(2)
    dq.insertFront(0)
    print("Front:", dq.getFront(), "Rear:", dq.getRear()) # 0, 2
    dq.deleteLast()
    print("Rear after 1 deleteLast:", dq.getRear()) # 1
