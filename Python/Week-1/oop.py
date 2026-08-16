# OOP stands for Object Orented Programming.

# Class :
class MyClass:  # To create new class, class cannot be empty, but if need to create one then use pass statement
  x = 5

# Object : 
p1 = MyClass()  # To create a object of class, mulitple objects can be created of one class
print(p1.x)

# del p1  # To delete the object

# __init__() : Every class have built-in method __init__(), which is used to assign value to object properties or to perfom any operations when thww object is being created.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Bond", 7)

print(p1.name)
print(p1.age)

# Access Properties of Object
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)

car1.brand = "Tata" # Modify properties of object
car1.model = "Nano"

print(car1.brand)
print(car1.model)

del car1.model  # Delete properties of object

# Class properties and Object properties
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance/Object property

p1 = Person("James")
p2 = Person("Bond")

p1.age = 7  # Add new property to object
p1.city = "USA"

print(p1.name)
print(p1.age)
print(p1.city)
print(p2.name)
print(p1.species)
print(p2.species)

# Class method: Methods(function) that belongs to class.

class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

  def welcome(self, name):
    print("Hello", name)

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("James Bond", 7)
p1.greet()
p1.welcome("Baby")
print(p1.get_info())

del Person.greet    # to delete the method from a class

## __str__() : method controls what is returned when the object is printed
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("James", 7)
print(p1)

 
# Encapsulation : It is used to protect data inside the class, it keeps method and data together in class while controlling how it will be accesed outside the class.
# __ used to create a private property, _ used to private preoprty intended for internal use

class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age    # Private property

  def get_age(self):    # getter method to access a private property
    return self.__age

  def set_age(self, age):   # setter method to change a private property
    if age > 0:
      self.__age = age
    else:
      print("Age must be positive")

  def __validate(self, age):    # __ used with method will create private method
    if not isinstance(age, (int, float)):
      return False
    return True

p1 = Person("James", 8)
print(p1.get_age())

p1.set_age(10)
print(p1.get_age())

p1.__validate(5)    # It will cause error, bcz it is private method

# Why Encapsulation
# Data Protection: Prevents accidental modification of data
# Validation: You can validate data before setting it
# Flexibility: Internal implementation can change without affecting external code
# Control: You have full control over how data is accessed and modified

# Inheritance : It allows to define a class that inherits all the methods and properties from another class
# Parent class: The class being inherited from(Base class), Child class : The class that inherits another class(Derived class)

class Person:   # Parent Class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

x = Person("James", "Bond")
x.printname()

class Student(Person):  # Child Class
  def __init__(self, fname, lname, year):
    Person.__init__(self, fname, lname) # or super().__init__(fname, lname), inherit all methods and properties from its parent
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("James Bond", "007", 2026)
x.printname()
x.welcome()

# Polymorphism : Same method name with mulitple use-case, commenly used in class methods
# len(), used by string to return number of characters, used for tuple to reurn number of items, used in dict to return key-value pairs.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()

# Ploymorphism with Inheritance
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# Inner class : An inner class is a class defined inside another class. The inner class can access the properties and methods of the outer class.
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()