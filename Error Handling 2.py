# Error Handling 2

def sum(num1, num2):
    try:
        return num1 / num2
    except (TypeError, ZeroDivisionError) as err: # Usefull for multiple errors
        print(err)
    
print(sum(1, 0))