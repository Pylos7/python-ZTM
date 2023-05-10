# Iterable
# Iterate
# Generator

def generator_function(num):
    for i in range(num):
        yield i*2 # yield is a keyword that is used like return, except the function will return a generator.



g = generator_function(100)

next(g) # next() is a built-in function that allows us to iterate through the items of a generator.
next(g)
print(next(g)) # 2

# for item in generator_function(1000):
#     print(item)