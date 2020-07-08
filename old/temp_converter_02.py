''' Convert Temperature from Fahrenheit to Celsius
and Celsius to Fahrenheit


Works in python 2x
'''

# temp conversion

def menu():
	print ("\n1. Celsius to Fahrenheit")
	print ("2. Fahrenheit to Celsius")
	print ("3. Exit")
	pick = int(input("Enter a choice: "))
	return pick

# Get value in F and convert to C
def toCelsius(f):
	return int((f - 32) / 1.8)

# Get value in C and convert to F
def toFahrenheit(c):
	return int((c * 1.8) + 32)


def main():
	choice = menu()

	while choice != 3:

		if choice == 1:
			# convert C to F
			c = input("Enter degrees Celsius: ")
			print (str(c) + "C = " + str(toFahrenheit(c)) + "F")

		elif choice == 2:
			# convert F to C
			f = input("Enter degrees Fahrenheit: ")
			print (str(f) + "F = " + str(toCelsius(f)) + "C")

		else:
			print ("Invalid entry")
		choice = menu()


if __name__ == "__main__":
	main()
