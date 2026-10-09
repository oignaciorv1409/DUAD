# CLASE PADRE -> Tiene ciertas caracteristicas. CLASE Hija -> Cuando nace un hijo hereda cosas del padre y ademas puede tener cosas propias 
class Vehicle:
        wheel_number = 0

        def turn_on(self):
                print("Vehicle is on")

class Car(Vehicle):  # -> Car(Vehicule) (Car es una clase que hereda de Vehicule)
        pass   #-> Aunque dentro no escribimos ningun metodo, podemos hacer "my_car.turn_on()"

my_car = Car()  # -> Obj tipo Car que a su vez hereda metodo y atributos de la clase Vehiculo (PADRE)

print(my_car.wheel_number) # ->  0, Str: "Vehicle is on"
my_car.turn_on()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SOBRESCRIBIR 
class ATV:
        wheel_number = 0

        def turn_on(self):  # -> El método puede venir de la clase padre, pero self sigue siendo el objeto hijo que llamó al método.
                print("ATV is On")

class Bike_1(ATV):
        wheel_number = 4

my_bike = Bike_1()
print(my_bike.wheel_number)
my_bike.turn_on()

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Bike_2(Vehicle):  # ->Herencia multinivel. ABUELO: class Vehicule, PADRE: class Bike_2, Hijo: class Bike
        wheel_number = 2

class Bike(Bike_2):
        pass

bike = Bike()
bike.turn_on()
print(bike.wheel_number)


# --------------------------------------- Sobrescribir un MÉTODO ---------------------------------------------------------------------------------------------------------

class Motorcyle(Vehicle):
        def turn_on(self):
                print("Motorcyle engine is ON.")

my_motorcyle = Motorcyle()
print(my_motorcyle.wheel_number)
my_motorcyle.turn_on()

# ---------------------------------------- HERENCIA MULTIPLE --------------------------------------------------------------------------------------------------------------
# Una sola clase puede heredar métodos y atributos de varias clases al mismo tiempo.

# Personaje de videojuego. Una clase sabe caminar. Otra sabe correr. Y otra sabe volar. 

class WalkerMixin:
        def walk(self):
                print("I'm walking!")

class RunnerMixin:
        def run(self):
                print("I'm running!")

class FlyerMixin:
        def fly(self):
                print("I'm flying!")

# Ahora creamos class SuperMan:
class SuperMan(WalkerMixin, RunnerMixin, FlyerMixin): # -> SuperMan hereda de WalkerMixin, RunnerMixin y FlyerMixin.
        pass


#----------------------------------------------------- ¿qué pasa si dos padres tienen lo mismo? -------------------------
# MRO (Method Resolution Order)

class Swimmer:
        def move(self):
                print("I'm swimming")


class Runner:
        def run(self):
                print("I'm running")

        def move(self):
                print("I'm moving by running")


class Athlete(Swimmer, Runner): # Python da prioridad siguiendo el orden en que se escriben las clases padre
        pass

class Athlete_2(Runner, Swimmer):
        pass


athlete = Athlete()

athlete.move()
athlete.run()

athlete_2 = Athlete_2()

athlete_2.move()
athlete.run()

# ----------------------------------------------------------- CLASES ABSTRACTAS ----------------------------------------------

# El hijo hereda cosas del Padre. Y el PADRE puede obligar al hijo a implementar ciertos metodos 

#EMPRESA: “No me importa cómo hagas tu trabajo, pero si vas a ser empleado de esta empresa, TIENES que tener una forma de work().”

from abc import ABC, abstractmethod


class Employee(ABC): # -> significa que Employee es una clase abstracta.

        @abstractmethod # -> work() es obligatorio para cualquier clase hija concreta. Tecnicamente es un DECORADOR 
        def work(self):
                pass

class Programmer(Employee):
        def work(self):
                print("I work programming.")

programmer = Programmer()
programmer.work() # -Output- I work programming.

# ------------------------------------------------------------------------------------------

class Manager(Employee):
        pass  # -> Manager heredó de Employee, pero no implementó: work()

# Contrato: work() obligatorio. Pero Manager no implemento work()

# Si se intenta crear un objeto de la clase Manager(). Python no deja crear el objeto. 

# manager = Manager() # “No puedes crear todavía un Manager. Firmaste el contrato de Employee, pero te falta implementar work().” 
# TypeError: Can't instantiate abstract class Manager without an implementation for abstract method 'work'

# PRACTICA: 

from abc import ABC, abstractmethod


class Device(ABC):

        @abstractmethod
        def turn_on(self):
                pass


class Computer(Device):

        def turn_on(self):
                print("Computer is starting")

class Phone(Device):
        def turn_on(self):
                print("Phone is starting")


computer = Computer()
computer.turn_on()
# phone = Phone() # -> TypeError: Can't instantiate abstract class Phone without an implementation for abstract method 'turn_on'
phone = Phone()
phone.turn_on()


# ---------------------------------------------------------------------- ENCAPSULAMIENTO ------------------------------------------------------

# Encapsular = decidir qué partes de un objeto deberían ser fáciles de usar desde afuera y cuáles deberían quedar “protegidas” dentro de la clase.
# Hay 3 niveles conceptuales: PUBLIC, PROTECTED y PRIVATE. 
# name *PUBLIC, _name *PROTECTED, __name *PRIVATE
# en Python, (PRIVATE) no bloquea realmente el acceso. Es más como un cartel que dice: “Esto es interno; no deberías tocarlo desde afuera."

# ------------------------------------------------------- PUBLIC vs PROTECTED ----------------------------------------------------------------------------------------------

class Player:
        def __init__(self, name, score):
                self.name = name # -> Parte PUBLICA
                self._score = score # -> Parte INTERNA

        def show_score(self):
                print(self._score)

        def add_score(self, points):
                if points > 0:
                        self._score += points


player = Player("Alex", 100)

print(player.name) # Esta bien que lo uses 
print(player._score)  # → "esto es parte interna del objeto" # “Puedes acceder técnicamente, pero esta variable forma parte del funcionamiento interno de la clase. Mejor usa los métodos públicos.”


# -> Python no lo bloquea. Ambos imprimen. La diferencia esta en la INTENCION de que queremos decir con el codigo

class Player_1(Player):
        def __init__(self, name, score):
                self.name = name
                self._score = score

        def show_score(self): # ahora vamos a agregar un metodo PUBLICO
                pass

player_1 = Player_1("Don", 150)

print(player_1.name)
print(player_1._score) # Output: Don, 150 (Eso confirma precisamente lo que queríamos ver: el _(Protected) no impide técnicamente acceder al atributo desde afuera.)


# ----------------------------------

class Player_2(Player):
        pass

player_2 = Player_2("Ethan", 200)

print(player_2.name)
player_2.show_score()


# ---------------------------------- # En Python, “protected” con un solo guion bajo _ no bloquea absolutamente nada. Es una convención entre programadores.

player_3 = Player("Sarah", 100)

player_3.show_score()

player_3.add_score(50)
player_3.show_score()

player_3.add_score(-500) # Solo lo usamos para distinguir o decir a otros programdores que queremos que sea interno y que queremos que sea publico. No cambia realmente los permisos. 
player_3.show_score()  # El _score sigue siendo accesible, pero tú estás diseñando la clase para que el camino correcto sea add_score().

# Pero __score: con dos guiones bajos sí hace algo diferente en Python llamado name mangling. Tampoco crea privacidad absoluta como Java/C#, pero ya no podrás acceder simplemente con: player.__score


# -----------------  De _score   a   __score (Name Mangling) ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Idea simple: _score "Esto es interno. Porfavor no lo toques (Convencion)". __score (Python cambia internamente el nombre) → ya no accedes simplemente como player.__score

class PlayerPrivate:
        def __init__(self, name, score):
                self.name = name
                self.__score = score

        def show_score(self):
                print(self.__score)


player_private = PlayerPrivate("Alex", 300)

print(player_private.name)
player_private.show_score()  # Esto funciona y muestra el print de .name ("Alex") y el score (300) referenciando el Metodo de la clase PlayerPrivate.

# Ahora usando el metodo PRIVATE: 

# print(player_private.__score) # AttributeError: 'PlayerPrivate' object has no attribute '__score'

# Analogia: con _score (PROTECTED) Python tenia una puerta con un cartel que decia "Interno". Pero dejaba la puerta abierta. Pero con __score (PRIVATE) Python hace algo más parecido a cambiarle el nombre a la puerta por detrás.
# Python internamente lo transforma aproximadamente en:  _PlayerPrivate__score 
# Por eso desde afuera de la clase no encuentra nada con ese nombre "player_private.__score"
# Pero si hacemos un metodo dentro de la clase con  def show_score(self): 
#                                                       print(self.__score)
#
#  sí funciona porque Python sabe hacer esa transformación internamente.
# Importante: esto no es privacidad absoluta. Porque tecnicamente alguien podria hacer: print(player_private._PlayerPrivate__score)
# Por eso Python no tiene private rígido como otros lenguajes. El doble _ sirve más para evitar accesos accidentales y conflictos de nombres, no para crear una bóveda imposible de abrir.


# --------------------------------------------------------------- ABSTRACCION -------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Poder usar un objeto sin necesitar conocer todos los detalles internos de cómo funciona.
# En código sería parecido a tener un método público sencillo:  car.start() 
# aunque internamente start() haga varias cosas.


# EJEMPLO: 
class CoffeeMachine:
        def make_coffee(self):
                self._heat_water()
                self._grind_coffee()
                self._pour_coffee()
                print("Coffee is ready")

        def _heat_water(self):
                print("Heating water")

        def _grind_coffee(self):
                print("Grinding coffee")

        def _pour_coffee(self):
                print("Pouring coffee")


# afuera solamente haces:

machine = CoffeeMachine()

machine.make_coffee()

#Entonces, ENCAPSULAMIENTO -> ocultar/separar detalles internos
#  ABSTRACCIÓN ->  dar una interfaz sencilla para usar esos detalles


#Practica: 

class GameConsole:
        def start_game(self):
                self._load_files()
                self._connect_controller()
                self._start_engine()
                print("Game started")

        def _load_files(self):
                print("Loading game files")

        def _connect_controller(self):
                print("Connecting controller")

        def _start_engine(self):
                print("Starting game engine")


console = GameConsole()

console.start_game()


# Como usuario solo hay que usar  start_game() no tienes que preocuparte por los detalles internos 

# MAPA MENTAL: 

# AFUERA -> console.start_game()  |  INTERIOR DE GameConsole -> _load_files() -> _connect_controller() -> _start_engine()   |   Resultado: Game started


# ------------------------------------------------------------------ POLIFORMISMO ----------------------------------------------------------------------------------------------------------------

# La idea simple es: El mismo nombre de método puede comportarse de forma diferente según el objeto que lo use.
# Osea MISMO metodo. MUCHAS formas de comportarse. 

# EJEMPLO: El boton de encender. Car.turn_on()  |  Computer.turn_on()  |  Phone.turn_on()  |  Todos tienen turn_on() pero cada objeto hace algo distinto. 

class Car:
        def turn_on(self):
                print("Car engine started")


        class Computer:
                def turn_on(self):
                        print("Computer booting Windows")


        class Phone:
                def turn_on(self):
                        print("Phone screen is turning on")


# Ahora cada objeto/dispositivo/vehiculo tienen turn_on(): 

car = Car()
computer = Computer()
phone = Phone()

# pero responde de forma diferente:

car.turn_on() # Car engine started

computer.turn_on() # Computer booting Windows

phone.turn_on() # Phone screen is turning on


# La parte más PODEROSA. Podemos meter objetos completamente diferentes en una misma lista:

devices = [
        Car(),
        Computer(),
        Phone(),
        ]

# Y luego Python puede ejecutar todos los metodos de que esos objetos referencian: 

for device in devices:
        device.turn_on() # -> Simplemente dice, dentro de esta lista, tengo este objeto. Simplemente iterando por vueltas ejecuta su turn_on() para el objeto respectivo. 

# La misma linea device.turn_on() tuvo 3 comportamientos diferentes. 

# IMPORTANTE: Estas clases no necesitan heredar unas de otras, pueden ser completamente independientes. 

# Practica: 

class Dog:
        def make_sound(self):
                print("Woof")


class Cat:
        def make_sound(self):
                print("Meow")


class Cow:
        def make_sound(self):
                print("Moo")


animals = [
        Dog(),
        Cat(),
        Cow(),
]


for animal in animals:
        animal.make_sound() 

# animal.make_sound() nunca CAMBIA. Lo unico que cambia es: ¿qué objeto referencia animal en esta vuelta?


# --------------------------------------------  EJEMPLO de los 4 Pilares juntos ---------------------------------------------------------------------------

# Clase PADRE Abstracta: 

from abc import ABC, abstractmethod


class Payment(ABC): # Payment es una clase padre abstracta:
        def __init__(self, amount):
                self._amount = amount  # _amount representa estado interno (ENCAPSULAMIENTO)

        @abstractmethod
        def pay(self): # pay() es el contrato. Toda clase hija de Payment debe implementar pay()
                pass

        def show_amount(self): # show_amount() es una forma pública sencilla de acceder al dato interno
                print(f"Amount: {self._amount}")

# Ahora creamos dos HIJOS: 

class CreditCardPayment(Payment): # Ambas clases heredan de PAYMENT. Por eso no necesitan volver a crear: show_amount() Simplemente lo HEREDAN. 
        def pay(self):
                print(f"Paying ${self._amount} with credit card") # El _ comunica:  “Esto es parte interna del objeto.” Y desde afuera preferimos:  payment.show_amount()  en lugar de: payment._amount

# Ambas clases HIJAS no tienen __init__ (constructor) propio. Sin embargo funcionan porque lo heredan de la clase PADRE. 

class CashPayment(Payment):
        def pay(self):
                print(f"Paying ${self._amount} with cash")


# Ahora usamos el objeto payment.pay(). No necesitamos saber como procesa Visa, como valida la tarjeta, como habla con el banco, como registra la transaccion. Como usuario solo usamos pay(). Eso es abstraccion (Ese método público es la interfaz sencilla.)


# Poliformismo, ahora hacemos: 

payments = [
        CreditCardPayment(100),
        CashPayment(50),
]

for payment in payments:
        payment.show_amount() # show_amount() también funciona para ambos, pero en ese caso ambos están usando exactamente el mismo método heredado de Payment asi que no es POLIFORMISMO solo heredan el metodo show_amount() de la clase PADRE. 
        payment.pay() # La linea payment.pay() es exactamente la misma. Pero el comportamiento cambia dependiendo del objeto. Eso es poliformismo. 



# En conclusion: 

# HERENCIA 
"Recibo/reutilizo comportamiento de otra clase."

# ENCAPSULAMIENTO
"Protejo y controlo cómo se usa el estado interno."

# ABSTRACCIÓN
"Expongo una interfaz simple y escondo complejidad."

# POLIMORFISMO
"La misma operación puede comportarse diferente dependiendo del objeto."