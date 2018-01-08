'''Sample Class creation'''

class Pet(object):
	'Common base class for all pets'
	petCount = 0

	def __init__(self, name, species):
		self.name = name
		self.species = species
		Pet.petCount += 1	# Increment for each pet at creation-time

	def getName(self):
		return self.name

	def getSpecies(self):
		return self.species

	def __str__(self):
		return "%s is a %s." % (self.name, self.species)

pet01 = Pet("Polly", "Parrot")
pet02 = Pet("Noah", "Dog")


print("I have %d pets." % Pet.petCount)
print(pet01)
print(pet02)
