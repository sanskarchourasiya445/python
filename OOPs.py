# OBJECT ORIENTED PROGRAMMING (OOPS) IN PYTHON
# Covers: # Class, Object, Constructor, Methods 
# Inheritance, Polymorphism, Encapsulation, Abstraction 
# Static Method, Class Method, Magic Methods

# CLASS & OBJECT
class Student:
    college = "ABC University"     # class variable (shared by all objects)

    def __init__(self, name, roll_no):
        self.name = name           # instance variable
        self.roll_no = roll_no

    def display(self):
        # instance method
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

    @classmethod
    def change_college(cls, new_college):
        # modifies class variable
        cls.college = new_college

    @staticmethod
    def info():
        # does not use class or instance variables
        print("Student class represents a college student")


# creating objects
s1 = Student("Sanskar", 101)
s2 = Student("Rahul", 102)

s1.display()
print("College:", Student.college)

Student.change_college("XYZ Institute")
print("Updated College:", Student.college)

Student.info()

print("-" * 50)

# INHERITANCE (Single + Multilevel)

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)      # calling parent constructor
        self.emp_id = emp_id

    def show_id(self):
        print(f"Employee ID: {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_department(self):
        print(f"Department: {self.department}")


# object of child-most class
m = Manager("Amit", 5001, "IT")
m.introduce()
m.show_id()
m.show_department()

print("-" * 50)

# METHOD OVERRIDING
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        # overriding parent method
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# same method name, different behavior
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()

print("-" * 50)

# ENCAPSULATION

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        # controlled access to private data
        return self.__balance


acc = BankAccount("Sanskar", 2000)
acc.deposit(1000)
acc.withdraw(500)
print("Balance:", acc.get_balance())

print("-" * 50)

# ABSTRACTION
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        # implementing abstract method
        return self.length * self.breadth


rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())

print("-" * 50)

# POLYMORPHISM (Duck Typing)

class Car:
    def start(self):
        print("Car starts")


class Bike:
    def start(self):
        print("Bike starts")


def start_vehicle(vehicle):
    # any object with start() works
    vehicle.start()


start_vehicle(Car())
start_vehicle(Bike())

print("-" * 50)

# MAGIC / DUNDER METHODS
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # controls print(object)
        return f"Book: {self.title}"

    def __len__(self):
        # controls len(object)
        return self.pages


b = Book("Python Basics", 250)
print(b)
print("Total pages:", len(b))

print("-" * 50)

# OPERATOR OVERLOADING
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # overload + operator
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")


p1 = Point(2, 3)
p2 = Point(4, 5)
# OBJECT ORIENTED PROGRAMMING (OOPS) IN PYTHON
# Demonstrates all major OOPS concepts using runnable code


# =========================
# CLASS & OBJECT
# =========================
class Student:
    college = "ABC University"     # class variable (shared by all objects)

    def __init__(self, name, roll_no):
        self.name = name           # instance variable
        self.roll_no = roll_no

    def display(self):
        # instance method
        print(f"Name: {self.name}, Roll No: {self.roll_no}")

    @classmethod
    def change_college(cls, new_college):
        # modifies class variable
        cls.college = new_college

    @staticmethod
    def info():
        # does not use class or instance variables
        print("Student class represents a college student")


# creating objects
s1 = Student("Sanskar", 101)
s2 = Student("Rahul", 102)

s1.display()
print("College:", Student.college)

Student.change_college("XYZ Institute")
print("Updated College:", Student.college)

Student.info()

print("-" * 50)


# =========================
# INHERITANCE (Single + Multilevel)
# =========================
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am {self.name}")


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)      # calling parent constructor
        self.emp_id = emp_id

    def show_id(self):
        print(f"Employee ID: {self.emp_id}")


class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department

    def show_department(self):
        print(f"Department: {self.department}")


# object of child-most class
m = Manager("Amit", 5001, "IT")
m.introduce()
m.show_id()
m.show_department()

print("-" * 50)


# =========================
# METHOD OVERRIDING
# =========================
class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        # overriding parent method
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


# same method name, different behavior
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()

print("-" * 50)


# =========================
# ENCAPSULATION
# =========================
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        # controlled access to private data
        return self.__balance


acc = BankAccount("Sanskar", 2000)
acc.deposit(1000)
acc.withdraw(500)
print("Balance:", acc.get_balance())

print("-" * 50)


# =========================
# ABSTRACTION
# =========================
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        # implementing abstract method
        return self.length * self.breadth


rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())

print("-" * 50)


# =========================
# POLYMORPHISM (Duck Typing)
# =========================
class Car:
    def start(self):
        print("Car starts")


class Bike:
    def start(self):
        print("Bike starts")


def start_vehicle(vehicle):
    # any object with start() works
    vehicle.start()


start_vehicle(Car())
start_vehicle(Bike())

print("-" * 50)


# =========================
# MAGIC / DUNDER METHODS
# =========================
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        # controls print(object)
        return f"Book: {self.title}"

    def __len__(self):
        # controls len(object)
        return self.pages


b = Book("Python Basics", 250)
print(b)
print("Total pages:", len(b))

print("-" * 50)


# =========================
# OPERATOR OVERLOADING
# =========================
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # overload + operator
        return Point(self.x + other.x, self.y + other.y)

    def display(self):
        print(f"({self.x}, {self.y})")


p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2     # calls __add__()

p3.display()
