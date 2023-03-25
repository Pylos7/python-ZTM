
from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'It took {t2-t1} seconds')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(100000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(100000000)):
        i*5

long_time()
long_time2()




# Generators are simple functions which return an iterable set of items, one at a time, in a special way.
# They are memory efficient and fast.


def gen_function(num):
    for i in range(num):
        yield i

for item in gen_function(100):
    print(item)