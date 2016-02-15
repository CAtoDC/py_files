"""Created by Mark Cuevas, 08-19-2015
This program generates random numbers for the Powerball
lottery and prints them out in numeric order. The first five
numbers are drawn from 53 balls and the sixth is drawn from
42 balls. The user can decide how many sets of numbers to generate.

The chances of guessing the Powerball lottery numbers correctly
are 1 in 120,526,770.

This was taken from the challenge found here: http://openbookproject.net/pybiblio/practice/wilson/powerball.php
"""

import random

# Numbers (1-53)
arr = range(1,54)

# Powerball nums (1-42)
pbarr = range(1,43)


def main():

	print ("Official (but fruitless) Powerball number generator\n")
	# get user input
	userSet = input("How many sets of numbers would you like? ")

	# add a blank line between user input and result
	print("")

	# the user determines how many sets of numbers are required
	for x in range(0, int(userSet)):
		# use List Comprehension
		numArr = []
		for i in range(0, 5):
			# generate five random numbers from 1-53
			numArr.append(random.choice(arr))
			# sort them
			numArrSorted = sorted(numArr)

		# generate random powerball number from 1-42
		pbNumGen = random.choice(pbarr)

		# print results in one line for each set of nums
		print("Your numbers: " + str(numArrSorted) + " \t" + str(pbNumGen))


if __name__ == "__main__":
	main()
