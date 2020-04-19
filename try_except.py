# Try Except Block

a, b = 1,0

try:
    print(a/b)    # exception raised when b is 0
except ZeroDivisionError:
    print("Exception: Division by zero.")
else:
    print("No exceptions raised.")
finally:
    print("Best practice is to always use Try/Except block.")