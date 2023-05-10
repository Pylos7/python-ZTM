# Error Handling in Python

# 1. Syntax Errors
    # Syntax errors are perhaps the most common kind of complaint you get while you are still learning Python:
# 2. Exceptions
    # Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it.
# 3. Handling Exceptions
    # The statements try and except can be used to handle selected exceptions. A try statement may have more than one except clause, to specify handlers for different exceptions.
# 4. Raising Exceptions
    # The raise statement allows the programmer to force a specified exception to occur.
# 5. User-Defined Exceptions
    # Programmers can name their own exceptions by creating a new exception class.

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input - Please enter a number")
except ZeroDivisionError:
    print("Age cannot be 0")
else:
    print("Thank you!")