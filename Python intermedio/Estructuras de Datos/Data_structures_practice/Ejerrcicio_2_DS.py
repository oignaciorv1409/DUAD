class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class DoubleEndedQueue:
    def __init__(self, head=None):
        self.head = head

    def push_left(self, new_node):
        new_node.next = self.head
        self.head = new_node

    def push_right(self, new_node):
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next

        current_node.next = new_node

    def pop_left(self):
        if self.head is not None:
            self.head = self.head.next

    def pop_right(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current_node = self.head

        while current_node.next.next is not None:
            current_node = current_node.next

        current_node.next = None

    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


deque = DoubleEndedQueue()

deque.push_right(Node("A002"))
deque.push_right(Node("A003"))
deque.push_right(Node("A004"))

deque.push_left(Node("A001"))

print("Deque inicial:")
deque.print_structure()

deque.pop_left()

print("\nDespués de pop_left:")
deque.print_structure()

deque.pop_right()

print("\nDespués de pop_right:")
deque.print_structure()