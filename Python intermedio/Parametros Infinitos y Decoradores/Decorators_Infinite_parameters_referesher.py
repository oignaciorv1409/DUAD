# Parametros infinitos *args 

#Hasta el momento hemos visto funciones como: 

def add_numbers(number_1, number_2):
        return number_1 + number_2

# Eso significa que en la funcion va a pasar exactamente lo que la funcion espera, en este caso 2 numeros.
add_numbers(5, 10)

# Pero que pasa si queremos pasarle mas numeros a la funcion, para eso existen los parametros infinitos, que nos permiten pasarle a la funcion cualquier cantidad de parametros. Sin saber de antemano cuántos números llegarán?
5, 10, 20, 50, 100, 300

# Para eso usamos *args, como una forma de aceptar una cantidad variable de argumentos usando * delante del parámetro.

#Ejemplo:

def show_numbers(*args):
        print(args)


show_numbers(10, 20, 30, 40)

#Python recoge todos los numeros (argumentos) y los empaqueta en una tupla (*args)


# ¿Qué significa realmente el *?
# El * es un operador que desempaqueta los argumentos de una tupla o lista. En este caso, el * le dice a Python "Todos los argumentos posicionales adicionales que lleguen, agrúpalos aquí."

# Y como podemos recorrer esa tupla? Con un bucle for, por ejemplo:

def show_numbers(*args):
        for number in args:
                print(number)

# show_numbers(10, 20, 30, 40)

# --------------------------------------------------- PRACTICA PEQUEñA ---------------------------------------------------

def show_products(*args):
        print(args) # Pythin empaqueta todos los productos en una tupla dentro de la tupla args. Por eso imprime la tupla completa. 

        for product in args:
                print(product) # Imprime cada producto por separado, recorriendo la tupla con un bucle for, tomando cada elemento por vuelta. 

show_products(
        "Coca Cola", 
        "Pepsi", 
        "Fanta", 
        "Sprite"
        )

# La idea clave es: *args -> Junta muchos argumentos posicionales -> Los guarda en una Tupla -> Luego podemos recorrer esa Tupla. 
# args imprimiria una tupla vacia si no se pasa ningun argumento en show_products() y el ciclo For no tendria nada que recorrer. Pero si se pasan argumentos, los guarda en la tupla args.


# ---------------------------------------------------------- PARAMETRO NORMAL +  *args ----------------------------------------------------------------------------------------------------------------------------------

#EJEMPLO:

def register_order(customer, *args):
        print(f"Customer: {customer}")

        for product in args:
                print(f"Product: {product}")


register_order(
        "Ignacio",  # Ignacio --> customer. Python primero llena el parámetro normal. El primer argumento no entra en args, porque Python ya lo utilizó para llenar customer.
        "Burger",
        "Fries",
        "Coke",
)

# Tambien podemos poner un parametro normal despues de *args. Pero al llamar la funcion tenemos que escribir el nombre de ese parametro.

def register_order(*args, table):
        print(args)
        print(table)

register_order(
        "Burger",
        "Fries",
        "Coke",
        table=5  # Parametro normal. Los parámetros que aparecen después de *args deben pasarse por nombre.
)


# Porque si hicieramos: 

# register_order("Burger", "Fries", "Coke", 5) # Python no sabría si ese 5 es otro elemento de args o el valor del parámetro table. Por eso, los parámetros que aparecen después de *args deben pasarse por nombre.


# ----------------------------------------------------- PRACTICA PEQUEñA ---------------------------------------------------

def create_sale(employee, *products, register):
        print(f"Employee: {employee}")
        print(f"Products: {products}")
        print(f"Register: {register}")


create_sale(
        "Sarah",
        "Burger",
        "Fries",
        "Coke",
        register=2
)

# Employee: Sarah | Products: ('Burger', 'Fries', 'Coke') | Register: 2



# ----------------------------------------------------------------------------------------------- KWARGS ----------------------------------------------------------------------------------------------------------------------------------

# Si *args es "Recoge muchos argumentos sin nombre y guárdalos en una tupla", **kwargs es "Recoge muchos argumentos con nombre y guárdalos en un diccionario".

def show_user(**kwargs):
        print(kwargs)


show_user(
        name="Sarah",
        age=28,
        role="Admin"
)

# Aqui Python recoge:  name="Sarah" | age=28 | role="Admin" y los convierte en un dict: 

kwargs = {
        "name": "Sarah",
        "age": 28,
        "role": "Admin"
}


# ------------------------------------------------------ PRACTICA PEQUEñA ---------------------------------------------------

def create_employee(name, **kwargs):
        print(f"Name: {name}")
        print(f"kwargs: {kwargs}")
        print (f"Role: {kwargs['role']} | Department: {kwargs['department']} | Active: {kwargs['active']}")


create_employee(
        "Sarah",
        role="Manager",
        department="Sales",
        active=True
)

# name = Sarah | kwargs = {'role': 'Manager', 'department': 'Sales', 'active': True}
# print (f"Role: {kwargs['role']} | Department: {kwargs['department']} | Active: {kwargs['active']}")



# ------------------------------------------------- Args + Kwargs ------------------------------------------------------------------------------------------------------------------------

# Ejemplo de un sistema POS 

def create_order(employee, *products, **details):  # parámetro normal primero, después *args, y **kwargs al final.
        print(f"Employee: {employee}")
        print(f"Products: {products}")
        print(f"Details: {details}")        


create_order(
        "Sarah",
        "Burger",
        "Fries",
        "Coke",
        table=5,
        payment="Card",
        takeaway=False
)


# ------------------------------------- DECORADORES ----------------------------------------------------------------------------------


# Los decoradores son como funciones que agregan o modifican comportamientos de otra funciones, ejecutando la logica anes o deues de ellas. 

# Ejemplo de decorador pequeño y sin clases: 

def my_decorator(func):  # Aqui func recibe la funcion original (esta es la parte mas rara y que confunde)  En este caso func ---> say_hello()
        def wrapper():
                print("Before the function")

                func() # --> Aqui se ejecuta la funcion original, que en este caso es say_hello()

                print("After the function")

        return wrapper # "En lugar de usar directamente la función original, usa esta nueva función wrapper que la rodea."


# Luego: 

@my_decorator # "Aplica my_decorator a la función que viene justo debajo."
def say_hello():
        print("Hello!")


# Ejecutamos la funcion say_hello() y vemos que el decorador my_decorator() se ejecuta antes y despues de la funcion say_hello().

say_hello()


# Mentalmente, decorador --> wrapper --> logica extra --> funcion original --> logica extra --> fin del wrapper --> fin del decorador.

# Llamamos a say_hello como si fuera una función normal. Pero como tiene @my_decorator, ya no apunta directamente a la función original.

# En su lugar, apunta a la función wrapper que está dentro de my_decorator.

# wrapper() En realidad, cuando escribimos say_hello(), Python termina ejecutando wrapper(). wrapper es la función que ahora "envuelve" a say_hello.

# print("Before...") wrapper() ejecuta primero logica extra ANTES de la función original. Luego llama a func(), que es la función original say_hello().

# say_hello() Python entra finalmente en el codigo original de say_hello()

# print("Hello!") Se ejecuta la logica original de la funcion say_hello()

# regresa al wrapper, Cuando say_hello termina, Python vuelve exactamente al punto donde estaba dentro de wrapper, justo después de func().

# print("After...") wrapper() continua y ejecuta logica extra DESPUES de la función original. Luego termina wrapper() y regresa a my_decorator().


# --------------------------------------------- Decorador que recibe parametros ------------------------------------------------------------------------------------------------------------------------

class User:
        def __init__(self, role):
                self.role = role


def admin_only(func):
        def wrapper(user, *args): # Python realmente entra primero en wrapper (RECIBIENDO o EMPAUETANDO argumentos)
                if user.role != "Admin": # "Antes de crear el producto, voy a revisar si este usuario tiene permiso"
                        raise ValueError("Only admins can use this function.")

                return func(user, *args) # "Ahora sí, ejecuta la función original" (EVIANDO O DESEMPAQUETANDO argumentos)

        return wrapper

# Decoramos una funcion: 

@admin_only # "Esta función tiene una validación antes de ejecutarse"
def create_product(user, product_name):
        print(f"Product {product_name} created!")


# Creamos un usuario con rol "Admin"

my_user = User("Admin")

create_product(my_user, "Burger")  # "Quiero ejecutar create_product", entra en la función original


# --------------------------------------------- @property ------------------------------------------------------------------------------------------------------------------------


class Student:
        def __init__(self, spanish_score, english_score):
                self.spanish_score = spanish_score # 2. las notas se guardan como atributos
                self.english_score = english_score

                self.average_score = (
                        self.spanish_score + self.english_score
                ) / 2   # 3. Luego se calcula el promedio en el constructor UNA VEZ y se guarda  como atributo del objeto 


student = Student(80, 80) # 1. creamos un estudiante 

# 4. Pero despues hacemos: 
student.spanish_score = 50
# esto genera que la nota cambie pero average_score no se actualiza, porque ya se calculó en el constructor y no se recalcula.


# AQUI ES DONDE entra @property, en lugar de guardar el promedio, podemos calcularlo cada vez que se accede a el, para que siempre esté actualizado.

class Student:
        def __init__(self, spanish_score, english_score):
                self.spanish_score = spanish_score
                self.english_score = english_score

        @property
        def average_score(self): # Sin @property, sería simplemente un método y tendríamos que hacer: student.average_score()
                return (
                        self.spanish_score + self.english_score
                ) / 2

student_2 = Student(80, 80)
print(student_2.average_score) # 80.0

student_2.spanish_score = 50
print(student_2.average_score) # 65.0, ahora el promedio se recalcula

# entonces, self.average_score = 80 --> Guarda un valor --> Ese valor permanece ahi hasta que alguien lo cambie / Analogia: Una foto, muestra las cosas como estaban cuando se tomo la foto

# @property no GUARDA el resultado como un atributo normal --> Cuando llamamos el metodo sudent.average_score --> calcula el valor en el momento  / Analogia: Una camara en VIVO, cada vez que se mira, muestra como estan las cosas AHORA

# por FUERA, student.average_score parece ATRIBUTO, pero por dentro es un metodo con logica propia 

# Importante: @property debe usarse solo para obtener/calcular informacion, no para metodos que modifican informacion



# --------------------------------------------------------------- @classmethod -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# una forma de crear métodos que pueden llamarse directamente desde la clase, sin tener que crear primero una instancia.

# Ejemplo: 

# Una funcion normal dentro de la clase User:

class User:
        def __init__(self, email):
                self.email = email

        def show_email(self):
                print(self.email)

# Para usar show_email(), necesitamos primero un objeto:

user = User("test@gmail.com")
user.show_email()



# ---------- Ahora con @classmethod la idea cambia.

class User:
        @classmethod
        def say_hello(cls): # Ese cls es parecido  a self, pero no son lo mismo.
                print("Hello from User")

# POdemos hacer: User.say_hello()

# Sin esto: user = User(...) (sin crear un objeto)

# Ejemplo: 

class Person:
        def __init__(self, first_name, last_name):
                self.first_name = first_name
                self.last_name = last_name

class User:
        def __init__(self, email, password, person):
                self.email = email
                self.password = password
                self.person = person

        @classmethod # --> classmethod crea primero el Person y después devuelve una instancia de User
        def create_user(cls, first_name, last_name, email, password):
                person = Person(first_name, last_name)

                return cls(email, password, person)


# Ahora podemos crear usuarios de esta forma: 

user = User.create_user(
        "Sarah",
        "Connor",
        "sconnor@gmail.com",
        "321"
)


# ----------------------------- Practica ------------------------------------------------------------------------

class Product:
        def __init__(self, name, price, discount):
                self.name = name
                self.price = price
                self.discount = discount

        @property
        def final_price(self):
                discount_amount = self.price * self.discount / 100
                return self.price - discount_amount


        
        @classmethod
        def create_without_discount(cls, name, price):
                return cls(name, price, 0)

product_1 = Product.create_without_discount(
        "Mouse",
        50,
)

product_2 = Product(
        "Keyboard", 100, 15
)

print(f'Product price is: {product_1.final_price}')
print(f'Product price with discount is: {product_2.final_price}')