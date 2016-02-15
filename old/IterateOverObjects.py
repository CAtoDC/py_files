class IterRegistry(type):
	"""Makes the class object iterable by using a metaclass"""
	def __iter__(cls):
		return iter(cls._registry)

class Pet(object):
	"""Common base class for all pets"""
	petCount = 0

	# Add metaclass info to allow for iteration over objects
	__metaclass__ = IterRegistry
	_registry = []

	def __init__(self, name, species):
		self._registry.append(self)	# Reference metaclass in init
		self.name = name
		self.species = species
		Pet.petCount += 1

	def getName(self):
		return self.name

	def getSpecies(self):
		return self.species

	def __str__(self):
		return "\t%s is a %s." % (self.name, self.species)	# \t adds a Tab char


# Create some pets
pet01 = Pet("Polly", "Parrot")
pet02 = Pet("Cuddles", "Cat")
pet03 = Pet("Marc Anthony", "Dog")
pet04 = Pet("Sashimi", "Fish")

# Now we can iterate through our objects
print("I have a number of pets:")
for pets in Pet:
	print (pets)

# Show the documentation for the classes
print("\nPet object:", Pet.__doc__)
print("\nIterRegistry object:", IterRegistry.__doc__)
