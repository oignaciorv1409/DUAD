from datetime import date

class User:
        def __init__(self, date_of_birth):
                self.date_of_birth = date_of_birth

        @property
        def age(self):
                today = date.today()
                age = today.year - self.date_of_birth.year

                if (today.month, today.day) < (
                        self.date_of_birth.month, 
                        self.date_of_birth.day
                ):
                        age -= 1

                return age

def check_adult(func):
        def wrapper(user):
                if user.age < 18:
                        raise ValueError(
                                f'User is under (18) adult legal age. Access Denied.'
                        )

                save_age = func(user)
                return save_age

        return wrapper

@check_adult
def access_adult_only(user):
        return "Acess granted!"

# ----------------------------- test

adult_user = User(date(1996, 9, 14))
print(access_adult_only(adult_user))


minor_user = User(date(2010, 12, 14))
try:
        print(access_adult_only(minor_user))
except ValueError as error:
        print(error)




#user = User(date(2000, 9, 14))
#print(user.age) #Age = 26

#user_2 = User(date(2000, 12, 14))
#print(user_2.age) # returns 26 but user 2 hasn't turned 26 years yet. 





