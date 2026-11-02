class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def print_structure(self):
        self.print_node(self.root)

    def print_node(self, current_node):
        if current_node is not None:
            print(current_node.data)

            self.print_node(current_node.left)
            self.print_node(current_node.right)


node_a = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("F")
node_g = Node("G")

node_a.left = node_b
node_a.right = node_c

node_b.left = node_d
node_b.right = node_e

node_c.left = node_f
node_c.right = node_g

tree = BinaryTree(node_a)

print("Binary Tree:")
tree.print_structure()