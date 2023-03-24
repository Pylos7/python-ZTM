import time

# Decorator

# Decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

def my_decorator(func):
    def wrap_func():
        print('**********')
        func()
        print('**********')
    return wrap_func

@my_decorator # This is the same as saying hello = my_decorator(hello)
def hello():
    print('Helllooooo')

@my_decorator
def bye():
    print('See ya later')

hello()

# Decorator with arguments - This is a bit more complicated
def my_timer(func):
    def wrap_func():
        t1 = time.time()
        func()
        t2 = time.time()
        print(f'It took {t2-t1} s')
    return wrap_func

@my_timer
def calc_square():
     print("Square")

calc_square()

