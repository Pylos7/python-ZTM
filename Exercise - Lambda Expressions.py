# Exercise: Lambda Expressions

# Square the numbers in the list using map and lambda
my_list = [5, 4, 3]
new_list = list(map(lambda number: number**2, my_list))
print(new_list)

# List Sorting
# Sort by the second item in the tuple
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print(a)

