class Node:
        data: str # este type hint solo sirve para que el desarrollador humano sepa que tipo de data va a recibir, si hacemos node = Node(25) Python igual lo va a crear 
        next: "Node" # Esto es forward reference, indica que estoy creando un tipo que aun no ha terminado de definirse y lo que espero que siga en next es un Node 

        def __init__(self, data, next = None):
                self.data = data
                self.next = next

# Si quitamos los type hints igual funcionaria, porque lo que define los nodos es el constructor y el head tambien en sus clases usando .self, si creamos linkedlist primero podria dar error porque Python no sane que es Node, aunque tambien podriamos decir head: "Node" dentro de LinkedList asi Python no tiene que resolver Node mientras se definde la clase Node 

class LinkedList:
        head: Node # Aqui la clase node ya fue definida anteriormente, por eso se escribe Node y no "Node"

        def __init__(self, head):
                self.head = head

        def print_structure(self):
                current_node = self.head

                while current_node is not None:
                        print(current_node.data)
                        current_node = current_node.next



node_3 = Node("C")
node_2 = Node("B", node_3)
node_1 = Node("A", node_2)

linked_list = LinkedList(node_1) # Si quisiera conservar ambas en memoria podria cambiar el nombre de la variable a linked_list_2 por ejemplo

print(linked_list.head.next.data) # termina en "B" porque head referencia a node_1, node_1.next referencia a node_2, y node_2.data vale "B".


current_node = Node("current node", node_2) 
linked_list = LinkedList(current_node) # ahora la variable linked_list apunta a otro obj tipo linked_list en este caso al objeto current_node y en la linea 29 linked_list deja de apuntar al obj node_1 aunque depues hace el print de "B" porque existion un tiempo en memoria antes de la reasignacion
current_node = linked_list.head   
# current_node = current_node.next

linked_list.print_structure()
