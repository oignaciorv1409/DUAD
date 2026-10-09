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
                if self.head is None:
                        self.head = new_node
                        return
                
                current_node = self.head

                if current_node is None:
                        print("La fila est vacia")
                        return

                while current_node.next is not None:
                        current_node = current_node.next

                current_node.next = new_node


        def dequeue(self):
                if self.head is not None:
                        self.head = self.head.next



#                def enqueue(self, new_node):
#                        current_node = self.head
#                       next_node = current_node.next

#                        while next_node is not None:
#                               current_node = next_node
#                              next_node = current_node.next

#                     current_node.next = new_node









# 2. Ahora si hacemos: 

# Crear los tickets
ticket_1 = Node("A001")
ticket_2 = Node("A002")
ticket_3 = Node("A003")
ticket_4 = Node("A004")

# Conectar los nodos
ticket_1.next = ticket_2
ticket_2.next = ticket_3
ticket_3.next = ticket_4

bank_queue = Queue(ticket_1)

print("\n--- FILA INICIAL ---")
bank_queue.print_structure()

print("\n--- ATENDEMOS A001 ---")
bank_queue.dequeue()
bank_queue.print_structure()

print("\n--- ATENDEMOS A002 ---")
bank_queue.dequeue()
bank_queue.print_structure()

print("\n--- LLEGA A005 ---")
bank_queue.enqueue(Node("A005"))
bank_queue.print_structure() # head → A003 → A004 → A005 → None

print("\n--- ATENDEMOS A003 ---")
bank_queue.dequeue()
bank_queue.print_structure()

print("\n--- ATENDEMOS A004 ---")
bank_queue.dequeue()
bank_queue.print_structure()

print("\n--- ATENDEMOS A005 ---")
bank_queue.dequeue()
bank_queue.print_structure() # aqui self.head → None, entonces current_node → None, y el while no se ejecuta. No imprime nada. La fila está vacía.





# -------------------------------------------- # stack queue (pila), Last in, first out (LIFO) 

# Metodo push() ---> Agrega arriba 
# aqui modificamos new_node.next = self.head para que el nuevo nuodo sea el primero que entra en el stack y luego hay que cambiar el head 



def push(self, new_node):
        new_node.next = self.head
        self.head = new_node

# Metodo pop()  ----> Quita arriba 
# aqui self.head = self.head.next para que el head apunte al siguiente nodo y se elimine el primero que entró en el stack.

def pop(self, new_node):
        if self.head is not None:
                self.head = self.head.next




# resumen so far, queue entra por el final y sale poor el head, stack etra por el head o inicio y sale por el head tambien 



# ------------------------------------ Double ended queue o Deque()

# new_node → A001 → A002 → A003 → None
# self.head → A002
# para agregar al inicio del Deque, la lógica es prácticamente la misma que push() en Stack:

def deque_push_front(self, new_node):
        new_node.next = self.head
        self.head = new_node

# Ahora vamos con agregar al final del Deque.
# se parece muchísimo a enqueue() de Queue.

def deque_push_back(self, new_node):
        if self.head is None:
                self.head = new_node
                return
        
        current_node = self.head

        while current_node.next is not None:
                current_node = current_node.next

        current_node.next = new_node

# Agregar por el front → lógica parecida a push()
# Quitar por el front → lógica parecida a pop() o dequeue()
# Agregar por el end → lógica parecida a enqueue()

# Quitar por el end → aquí necesitamos recorrer hasta el penúltimo nodo si tenemos head

def deque_pop_back(self): 
        if self.head is None:
                return
        
        if self.head.next is None: # Si solo hay un nodo, lo eliminamos y dejamos la cabeza en None
                self.head = None
                return
        
        current_node = self.head
        while current_node.next.next is not None: # while solo se usa cuando ya sabemos que existen al menos dos nodos.
                current_node = current_node.next
        
        current_node.next = None