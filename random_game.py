# Description: A simple number guessing game

import random

answer = random.randint(1, 10)

while True: # infinite loop
    try:
        guess = int(input('Guess a number between 1 and 10:  '))
        if 0 <= guess <= 11: # check if guess is between num1 and num2
            if guess == answer:
                print("You're a genius!")
                break
            else:
                print("Sorry, try again!")
        else:
            print('hey, I said 1~10')
    except ValueError: # if user enters a string
        print("Please enter a number!")
        continue
