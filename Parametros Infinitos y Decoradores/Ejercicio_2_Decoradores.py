def check_number(func):
        def wrapper(*numbers):
                for n in numbers:
                        if not isinstance(n, (int, float)):
                                raise TypeError(
                                        f"Numbers: {numbers} are the wrong format. Please only enter integers/floats."
                                )

                saved_valid_numbers = func(*numbers)
                #print(saved_valid_numbers)
                return saved_valid_numbers
        
        return wrapper


@check_number
def only_integers(a, b):
        if not isinstance(a, (int)) or not isinstance(b, (int)):
                raise TypeError(
                        "This function only admits integers."
                )
        return a + b

@check_number
def int_and_float(a,b):
        return a + b

@check_number
def number_with_string(a, string):
        empty_list = []
        return empty_list 

# --------------------- Test


print(only_integers(5, 10))



try:
        print(only_integers(5, 2.5))
except TypeError as error:
        print(error)



print(int_and_float(5, 2.5))



try:
        print(number_with_string(5, "10"))
except TypeError as error:
        print(error)


