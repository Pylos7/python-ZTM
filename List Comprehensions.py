# List Comprehensions - Types: List Comprehensions, Set Comprehensions, Dictionary Comprehensions

# List Comprehensions are a way to create lists using an expression
# The expression is usually a function, but it can be any expression
# that returns a value.

# The syntax is:
# [expression for item in list]

# The expression is evaluated for each item in the list, and the
# result is stored in a new list.

# For example, if we have a list of numbers, we can create a new list
# that contains the square of each number in the original list.

# Here is a list of numbers:
numbers = [1, 2, 3, 4, 5]

# Here is a list comprehension that creates a new list that contains
# the square of each number in the original list:
squares = [n * n for n in numbers]

# Here is the original list:
print(numbers)

# Here is the new list:
print(squares)