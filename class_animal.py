class Dog(object): # object refers to parent class you are inheriting from

    # class attribute (the same for all instances)
    species = 'mammal'

    # instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def speak(self, sound):
        return "{} says {}!".format(self.name, sound)

    # instance method
    def trick(self, ability):
        return "{} can {}".format(self.name, ability)

    # instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)


# Instantiate the Dog object
mephisto = Dog('Mephisto', 2)
harper = Dog('Harper Lee', 5)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    mephisto.name, mephisto.age, harper.name, harper.age))

# Is Mephisto a mammal?
if mephisto.species == "mammal":
    print("{0} is a (wild) {1}!".format(mephisto.name, mephisto.species))

# Find the oldest animal
def get_biggest_number(self, *args):
    return max(args)

# Which dog is the oldest?
print("The oldest dog is {} years old.".format(get_biggest_number(mephisto.age, harper.age)))


# call our instance methods
print(mephisto.description())
print(mephisto.speak("woof"))
print(mephisto.trick("chase a ball, but he doesn't bring it back."))
