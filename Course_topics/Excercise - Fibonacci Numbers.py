# Excercise - Fibonacci Series

# Does not keep the entire series in memory - Fast and memory efficient
def  fib(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(1000):
    print(x)

# Keeps the entire series in memory - Slow and memory inefficient
def  fib2(n):
    a = 0
    b = 1
    result = []
    for i in range(n):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result


print(fib2(100))