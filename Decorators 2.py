import time

# Decorator Pattern

# Decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrap_func

@my_decorator # This is the same as saying hello = my_decorator(hello)
def hello(greeting, emoji="=("):
    print(greeting, emoji)


hello("Hi there")

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

