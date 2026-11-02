class Person:
        pass


class Bus:

        def __init__(self, max_passengers):
                self.current_passengers = []
                self.max_passengers = max_passengers

        def add_new_passenger(self, new_passenger):
                if len(self.current_passengers) >= self.max_passengers:
                        print("Bus is full.")
                        return self.current_passengers


                else:
                        self.current_passengers.append(new_passenger)

        def remove_passengers (self):
                if self.current_passengers:
                        remove = self.current_passengers.pop()
                        print("Passenger left the bus.")
                else:
                        print("The bus is empty.")



person_1 = Person()
print(person_1)
person_2 = Person()
print(person_2)
person_3 = Person()
print(person_3)
person_4 = Person()
print(person_4)
person_5 = Person()
print(person_5)

my_bus = Bus(4)
my_bus.add_new_passenger(person_1)
my_bus.add_new_passenger(person_2)
my_bus.add_new_passenger(person_3)
my_bus.add_new_passenger(person_4)
my_bus.add_new_passenger(person_5)

print(my_bus.current_passengers)

