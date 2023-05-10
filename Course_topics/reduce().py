# map, filter, zip, and reduce

# Reduce function

# reduce(function, iterable[, initializer])
# reduce() continually applies the function to the sequence. It then returns a single value.
# reduce() does not exist in Python 3. Instead, use functools.reduce().
# reduce() is not a built-in function, so you need to import it from the functools module.

from functools import reduce
my_list = [1,2,3]


def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulator, my_list, 10))
print(my_list)