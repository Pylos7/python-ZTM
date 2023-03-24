# Lambda expressions are used to create anonymous functions that are used only once.

# Example 1
lambda param: action(param)

my_list = [1,2,3]

def multiply_by2(item): # Not a lambda expression
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    return acc + item

print(list(filter(lambda item: item % 2 != 0, my_list))) # Lambda expression