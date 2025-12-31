# A tuple is an ordered, immutable collection.

t = (10, 20, 30, 20)

# Accessing
print(t[0])
print(t[-1])

# Slicing
print(t[1:3])

# Count & Index
print(t.count(20))   # how many times value appears
print(t.index(30))   # index of value

# Length
print(len(t))

# Tuple unpacking
a, b, c, d = t
print(a, b, c, d)

# Convert tuple to list
lst = list(t)
lst.append(40)
t = tuple(lst)
print(t)
