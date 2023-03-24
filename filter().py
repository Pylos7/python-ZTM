# map, filter, zip, and reduce

# Filter function

# filter(function, iterable)
# Only if the function returns True will the element of the list be kept.

my_list = [1,2,3]

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list)