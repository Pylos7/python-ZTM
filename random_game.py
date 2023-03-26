# Description: A simple number guessing game

import sys # to get command line arguments
from random import randint

num1 = int(sys.argv[1]) # first argument 

num2 = int(sys.argv[2])

answer = randint(num1, num2)

while True: # infinite loop
    try:
        guess = int(input(f"Guess a number between {num1} and {num2}: "))
        if num1 <= guess <= num2: # check if guess is between num1 and num2
            if guess == answer:
                print("You're a genius!")
                break
            else:
                print("Sorry, try again!")
        else:
            print(f"hey, {guess} is not between {num1} and {num2}")
    except ValueError: # if user enters a string
        print("Please enter a number!")

