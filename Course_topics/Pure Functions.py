# Functional Programming

# Pure Functions

# Pure functions are functions that return the same result if given the same arguments.
# They also do not cause any observable side effects such as network or database calls.
# Any function that relies on a random number generator cannot be pure.
# A function is not a pure function because it will return different results each time you call it with the same arguments.
# Pure functions are stable, consistent, and predictable.
# Given the same parameters, pure functions will always return the same result.
# Pure functions are also easier to test.
# Because they do not depend on any state, they are also easier to debug.

wizard = {
    "name": "Merlin",
    "power": 50
}

def multiply_by2(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list

# Side Effects

# A function results in a side effect if it does anything other than take a value in and return another value or values.
# A function that modifies a global variable or object property is a side effect.
# A function that calls any other function with a side effect is also a side effect.


print(multiply_by2([1,2,3]))