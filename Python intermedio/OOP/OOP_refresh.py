class Car:
        wheels = 4
        speed = 300
        pass

        def show_speed(self):
                print(self.speed)

my_car = Car()

my_car.wheels
my_car.show_speed()



class Pokemon:
        pass

pikachu = Pokemon()
bulbasaur = Pokemon()


class Dog:
        # estos son atributos (informacion) -> Que es el objeto? Que informacion tiene el objetvo? 
        name = ""
        age = ""
        legs = 4
        color = "" 

# Esto son metodos (funcionalidades) -> Que puede hacer el objeto? Que acciones hace un perro (obj)?
        def bark(self):
                print("Woof!")

        def show_name(self, name):
                self.name = name
                print(self.name)


dog_1 = Dog()
dog_1.bark()  # --> Los metodos son como funciones comunes pero dependen directamente de su objeto. entonces lo llamamos desde el objeto no desde barck()
dog_1.show_name("Max")
print(dog_1.name)


class NewPerson: 
        name = ""
        age = ""
        race = ""
        country = ""

        def __init__(self, name, age, race, country):
                self.name = name 
                self.age = age
                self.race = race
                self.country = country

                print(self.name)
                print(self.age)
                print(self.race)
                print(self.country)

person_1 = NewPerson("Gaby", 52, "Hispanic", "Costa Rica")
person_2 = NewPerson("Oscar", 53, "Hispanic", "Costa Rica")
person_3 = NewPerson("Josue", 26, "Hispanic", "Costa Rica")
person_4 = NewPerson("Ignacio", 30, "Hispanic", "Costa Rica")



print(person_1.name)
print(person_4.name)



class BankAccount:
        def __init__(self, owner):
                self.owner = owner 
                self.balance = 0

account_1 = BankAccount("Oscar Ignacio")

