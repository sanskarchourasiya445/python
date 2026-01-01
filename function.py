# Function → reusable block of code that runs when called
# Basic function
def greet():
    print("Hello Python")

greet()

# Function with parameters
def add(a, b):
    return a + b

print(add(2, 3))

# Default parameters
def power(base, exp=2):
    return base ** exp

print(power(3))
print(power(3, 3))

# Keyword arguments
def student(name, age):
    print(name, age)

student(age=20, name="Sanskar")



# *args (multiple values)
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))

# Lambda function
square = lambda x: x * x
print(square(5))

# Return multiple values
def calc(a, b):
    return a + b, a - b

sum_, diff = calc(10, 5)
print(sum_, diff)

# Docstring
def multiply(a, b):
    """Returns product of two numbers"""
    return a * b

print(multiply(4, 5))



# Global vs Local
x = 10

def show():
    x = 5
    print(x)

show()
print(x)
