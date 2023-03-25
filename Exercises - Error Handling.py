# Error Handling
while True:
    try:
        age = int(input("What is your age? "))
        print(age)
    except ValueError:
        print("Please enter a number")
    except ZeroDivisionError:
        print("Please enter a number greater than zero")
    else:
        print("Thank you")
        break
    finally:
        print("OK, I am finally done")