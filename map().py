# map, filter, zip, and reduce

# Map function
# map(function, iterable, ...)
# map() applies a function to all the items in an input_list.

my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list)