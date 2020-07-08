"""This program asks the user to guess a number
between 1 and 10, giving helpful hints along the way.

guesser.py, by Richard White, 2012-01-16
guesser_02.py by M. Cuevas 2015-08-17
"""

import random

def main():
	# Initialize program
	print ("Guess a number between 1 and 10.")

	randomNumber = random.randint(1, 10)

	found = False	# flag variable to track whether
					# the user guessed correctly or not

	# Guessing process
	while not found:
		# get user input
		userGuess = input("Your guess: ")

		# result if true
		if userGuess == str(randomNumber):
			print ("Correct!")
			found = True

		# result if false
		elif userGuess > str(randomNumber):
			print ("That's too high.")
		else:
			print ("That's too low.")

	# Congratulate the user
	print ("Thanks for playing!")


if __name__ == "__main__":
	main()
