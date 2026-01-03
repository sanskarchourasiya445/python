# File handling is used to store, read, and manage data permanently.

# Writing to a file
file = open("data.txt", "w")     # w = write (creates file if not exists)
file.write("Hello Python\n")
file.write("File Handling Basics\n")
file.close()

# Reading from a file
file = open("data.txt", "r")     # r = read
content = file.read()
print(content)
file.close()

# Append to a file
file = open("data.txt", "a")     # a = append
file.write("This line is appended\n")
file.close()

# Read line by line
file = open("data.txt", "r")
for line in file:
    print(line.strip())
file.close()

# Using with statement
with open("data.txt", "r") as file:
    data = file.read()
    print(data)

# Writing list data to file
items = ["Python\n", "Java\n", "C++\n"]

with open("languages.txt", "w") as file:
    file.writelines(items)


# Reading file into list
with open("languages.txt", "r") as file:
    lines = file.readlines()
    print(lines)

# File Modes Reference
# r  -> read
# w  -> write
# a  -> append
# r+ -> read & write
