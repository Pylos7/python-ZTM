# Generators are simple functions which return an iterable set of items, one at a time, in a special way.

range(10) 
list(range(10))

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)