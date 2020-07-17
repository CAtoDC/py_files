'''What is __name__ and how do we use it?  

Before python runs any code, it sets a few special variables;
__name__ is one of those special variables.
When python runs a file directly, it sets the __name__ variable to __main__.

Whenever we import a module, python runs that code.
'''

print ("This sentence always gets printed.")

def main():
    print ("This is being run from the first module's main method.")

# if run directly by python this will be called
# if imported, it will not
if __name__ == '__main__':
    print ("This is being run directly.")
else:
    print ("This is being run from an import statement.")
