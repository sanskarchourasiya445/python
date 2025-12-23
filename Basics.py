# Python Basics: Variables, Data Types, User Input, Statements & Expressions

# Variables
# Think of variables as little boxes where we store information
# Python automatically decides the type of information


name = "Sanskar"       # string
age = 20               # whole number (integer)
height = 170.5         # decimal number (float)
is_student = True      # True or False (boolean)


print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")
print("Student?", is_student)

# User Input
user_name = input("What's your name? ")
user_age = int(input("How old are you? "))
user_height = float(input("What's your height in cm? "))
user_student = input("Are you a student? (yes/no) ")

# Show the information back to the user
print("\nAwesome! Here's what you shared:")
print("Name:", user_name)
print("Age:", user_age)
print("Height:", user_height, "cm")
print("Student?", user_student)

# Statements & Expressions 
# Statement: a line that does something
# Expression: a line or part of code that calculates/evaluates something

total_age = age + user_age
height_diff = height - user_height

print("\nSome quick calculations:")
print("Combined age:", total_age)
print("Height difference:", height_diff)
print("Am I older than you?", age > user_age)
