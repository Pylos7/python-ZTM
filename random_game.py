import sys
from random import randint

num1 = int(sys.argv[1])

num2 = int(sys.argv[2])

random_number = randint(num1, num2)

guess = int(input(f"Hello World! Guess a number between {num1} and {num2}: "))



while random_number != guess:
    guess = int(input("You are unlucky! try again! "))
else:
    print("You are a genius!")
    
