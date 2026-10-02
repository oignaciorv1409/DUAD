class Node:
        def __init__(self, data, next = None):
                self.data = data
                self.next = next

class LinkedList:
        def __init__(self, head):
                self.head = head


node_3 = Node("C")
node_2 = Node("B", node_3)
node_1 = Node("A", node_2)

linked_list = LinkedList(node_1)

print(linked_list.head.next.data) # termina en "B" porque head referencia a node_1, node_1.next referencia a node_2, y node_2.data vale "B".


current_node = Node("current node", node_2)
linked_list = LinkedList(current_node)
current_node = linked_list.head
# current_node = current_node.next

print(current_node.data)