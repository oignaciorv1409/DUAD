def my_decorator(func):
        def wrapper(*args):
                print(f'Parameters: {args}')

                result = func(*args)

                print(f'Print math operation result: {result}')
                return result
        
        return wrapper


@my_decorator
def sum_number(a, b):
        return a + b 


sum_number(5,10)

