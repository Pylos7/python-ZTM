# Error Handling

while True:
    try:
        age = int(input("What is your age? "))
        10/age
        raise Exception("Hey cut it out")
    except ZeroDivisionError:
        print("Please enter a number greater than zero")
        break # break out of the loop
    else:
        print("Thank you")
        break # break out of the loop
    finally:
        print("OK, I am finally done")
print("Can you hear me?")