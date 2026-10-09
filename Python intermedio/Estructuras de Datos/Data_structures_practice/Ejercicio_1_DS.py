class Node:
        def __init__(self, data, next=None):
                self.data = data
                self.next = next


class Stack:
        def __init__(self):
                self.top = None

        def push(self, new_node):
                new_node.next = self.top
                self.top = new_node

        def pop(self):
                if self.top is None:
                        return None

                removed_node = self.top
                self.top = self.top.next
                removed_node.next = None

                return removed_node

        def print_structure(self):
                current_node = self.top

                while current_node is not None:
                        print(current_node.data)
                        current_node = current_node.next


stack = Stack()

stack.push(Node("A001"))
stack.push(Node("A002"))
stack.push(Node("A003"))
stack.push(Node("A004"))

print("Stack inicial:")
stack.print_structure()

stack.pop()

print("\nDespués de pop:")
stack.print_structure()