# Implementing our own for loop

def spacial_for(iterable):
    iterator = iter(iterable) # This is the same as iterable.__iter__()
    while True:
        try:
            print(iterator)
            print(next(iterator)*2)
        except StopIteration:
            break

spacial_for([1,2,3])

# Implementing our own range function

class MyGen(): # Creating a class that will act as a generator - our own range function
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen(0, 100)
for i in gen:
    print(i)