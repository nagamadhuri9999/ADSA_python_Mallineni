class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_start(self, value):
        new_node = Node(value)

        if self.head is not None:
            self.head.prev = new_node
            new_node.next = self.head

        self.head = new_node

    # Insert at end
    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Delete from beginning
    def delete_start(self):
        if self.head is None:
            print("List is empty")
            return

        print(f"Deleted: {self.head.data}")

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next
        self.head.prev = None

    # Delete from end
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print(f"Deleted: {self.head.data}")
            self.head = None
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        print(f"Deleted: {temp.data}")

        temp.prev.next = None

    # Display forward
    def display_forward(self):
        temp = self.head

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Display backward
    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("None")


# Driver Code
dll = DoublyLinkedList()

dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)
dll.insert_start(5)

print("Forward:")
dll.display_forward()

print("Backward:")
dll.display_backward()

dll.delete_start()
dll.display_forward()

dll.delete_end()
dll.display_forward()