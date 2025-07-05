def divide_by_zero(x):
    return 20/ x

try:
    print(divide_by_zero(10))
    print(divide_by_zero(0))
    print(divide_by_zero('aaaa'))

except ZeroDivisionError :
    print("You cannot divide by zero")
except NameError:
    print("Variable x is not defined")
except TypeError:
    print("You cannot divide a string by an integer")