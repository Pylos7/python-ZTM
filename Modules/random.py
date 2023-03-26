# Random
import random

print(random)

print(random.random())

print(random.randint(1, 10))

print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(random.choices([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=5))

print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k=5))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(my_list) # Shuffle the list
print(my_list)

print(random.uniform(1, 10))

print(random.gauss(1, 10))
