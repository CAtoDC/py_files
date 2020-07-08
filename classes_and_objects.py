# Object Orientation Programming in Python
# From YouTube: "Python Object Oriented Programming (OOP) - For Beginners"
# Tech with Tim

x = 1
y = "hello"

# x is an instantiation of a class object of type int
#print(type(x))


# METHODS
'''
A method is a function that exists inside of a class.
Here the class is the instantiation of the object of type, string.
'''
string = "hello"
#print(string.upper())


# Create a class
class Dog:
    ''' 
    The __init__ method gets called when we instantiate the class.
    self refers to the object itself.
    An attribute of the class gets added to every instantation of the class.
    '''
    def __init__(self, name, age):
        # self.name and self.age are attributes
        self.name = name
        self.age = age

    # These are methods
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def bark(self):
        print("bark")

# Instantiate the class
d = Dog("Tim", 14)
#print(d.get_name(), "-", d.get_age())

d2 = Dog("Rufus", 5)
#print(d2.get_name(), "-", d2.get_age())


# More complex example
# Make classes interact

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

# Create some students
s1 = Student("Tim", 19, 95)
s2 = Student("Mark", 28, 98)
s3 = Student("Jill", 19, 74)

# Now let's assign the students to a course
course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)

print(course.students[1].name)

print(course.get_average_grade())


# INHERITANCE
class Pet:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old.")

    def speak(self):
        print("I don't know what I say.")

# These inherit from the parent class, Pet.
# If the child class has a method of the same name as the parent class, the child class is used.
# The super().__init__ method pulls parameters from the parent class.
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name}. I am {self.age} years old and I am {self.color}.")    

# If there is no __init__ method, the __init__ method from the parent class is used.
class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim", 19)
p.show()
p.speak()

c = Cat("Bill", 34, "brown")
c.show()
c.speak()

d = Dog("Jill", 25)
d.show()
d.speak()


# CLASS ATTRIBUTES
# Class attributes are specific to a class, not specific to an instance of a class
class Person:
    # This is a class attribute because it does not use 'self'
    # It's defined for the entire class
    # Class methods act on the class itself; they don't have access to any instance
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()
        #Person.number_of_people += 1    # This changes the total for every instance

    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Tim")
p2 = Person("Jill")

# Both of these work because number_of_people is defined for the entire class
print(p1.number_of_people)
print(Person.number_of_people)

print(Person.number_of_people_())


# STATIC METHODS
class Math:
    
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def pr():
        print("run")

print(Math.add5(5))
Math.pr()
