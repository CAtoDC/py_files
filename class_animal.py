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


# Instantiate the Dog object (this calls the __init__ method)
d1 = Dog('Mephisto', 2)
d2 = Dog('Harper Lee', 5)

# Access the instance attributes
print(f"{d1.name} is {d1.age} and {d2.name} is {d2.age}.")

# Is Mephisto a mammal?
if d1.species == "mammal":
    print(f"{d1.name} is a (wild) {d1.species}.")

# Find the oldest animal
def get_biggest_number(self, *args):
    return max(args)

# Which dog is the oldest?
#print("The oldest dog is {} years old.".format(get_biggest_number(d1.age, d2.age)))
print(f"The oldest dog is {get_biggest_number(d1.age, d2.age)} years old.")


# call our instance methods
print(d1.description())
print(d1.speak("woof"))
print(d1.trick("chase a ball, but he doesn't bring it back."))
