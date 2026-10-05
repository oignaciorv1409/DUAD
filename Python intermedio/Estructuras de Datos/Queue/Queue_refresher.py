# enqueue() regla FIFO (First In, First out)

class Node: # Aquí estamos creando nuestro propio tipo de objeto llamado Node
        data: str
        next: "None" # son type hints. No crean los atributos; solamente indican qué tipo esperamos.

        def __init__(self, data, next=None): # 1. En el constructor, self representa el nodo actual específico que se está creando. Si hacemos ticket_1 = Node("A001")
                self.data = data                                                          # Durante ese __init__  Self → ticket_1, data → "A001", next → None
                self.next = next 


class Queue:
        head: Node  # TypeHint, esperamos que head sea un Node.

        def __init__(self, head): # recibe el primer nodo de la fila. Pero este self es un metodo que representa la instancia completa de Queue, osea self → el Queue completo
                self.head = head # → Primer nodo de la fila o el primer Node de esa Queue

        def print_structure(self): # self → bank_queue ( la instancia de print_structure que recibe el parametro bank_queue mediante self)
                current_node = self.head # Voy a empezar mi recorrido desde el primer nodo. Ej: A001 → A002 → A003 → None ( el Node que estoy visitando en ese momento) (sefl,head -> bank_queue.head → ticket_1)

                while current_node is not None: # Mientras todavía esté parado sobre un nodo válido, continúa.
                        print(current_node.data) # usa la información del nodo actual. Primera vuelta:  current_node → A001 = print → A001
                        current_node = current_node.next # mueve nuestra referencia al siguiente nodo de la fila:  current_node → A002


                def enqueue(self, new_node):
                        current_node = self.head

                        while current_node.next is not None:
                                current_node = current_node.next

                        current_node.next = new_node

#                def enqueue(self, new_node):
#                        current_node = self.head
#                       next_node = current_node.next

#                        while next_node is not None:
#                               current_node = next_node
#                              next_node = current_node.next

#                     current_node.next = new_node









# 2. Ahora si hacemos: 

ticket_1 = Node("AA01")
ticket_2 = Node("AA02")
ticket_3 = Node("AA03")

ticket_4 = Node("AA04") # Añadimos ticket 4 y ahora bank_queue.print_structure() hace print A001 -> A002 -> A003 -> 


ticket_1.next = ticket_2
ticket_2.next = ticket_3
ticket_3.next = ticket_4

bank_queue = Queue(ticket_1)

bank_queue.print_structure() # Eso muestra A001 -> A002 -> A003  (Ahora si queremos agregar un nuevo nodo a la fila podemos hacer enqueue() )
