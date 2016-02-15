# Thousands format
def product(x, y):
    return x * y
print ("{:,}".format(product(14,236)))


# Two decimal places
pi = 3.1415926
print("{:.2f}".format(pi))


# Using .format
madlib = "I {verb} the {object} off the {place}.".format(verb="took", object="cheese", place="table")
print(madlib)
