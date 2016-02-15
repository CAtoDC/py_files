'''Scope

Variables defined inside a function body have local scope

Variables defined outside a function body have global scope
'''

# global variable
total = 0

# define function
def sum( arg1, arg2 ):

   # local variables
   total = arg1 + arg2
   print ("Inside the function (local variable):", total)


# Now you can call sum function
sum( 10, 20 )

print ("Outside the function (global variable):", total)
