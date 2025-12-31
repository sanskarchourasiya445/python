# A dictionary stores data in key-value pairs.

student = {
    "name": "Sanskar",
    "age": 20,
    "course": "Python"
}

# Accessing values
print(student["name"])
print(student.get("age"))

# Adding / Updating
student["age"] = 21
student["city"] = "Bhopal"
print(student)

# Removing
student.pop("course")
print(student)

# Keys, Values, Items
print(student.keys())
print(student.values())
print(student.items())

# Looping
for key in student:
    print(key, ":", student[key])

# Check key existence
print("name" in student)

# Copy
new_student = student.copy()
print(new_student)

# Clear
student.clear()
print(student)
