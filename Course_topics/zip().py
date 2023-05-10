# map, filter, zip, and reduce

# Zip function

# Zip function is used to combine two lists into a list of tuples.
# zip(iterable, ...)
# zip() will create pairs of elements when passed two lists, and will stop at the end of the shorter list.

my_list = [1,2,3]
your_list = (10,20,30)
their_list = (5,4,3)

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list, their_list)))
print(my_list)