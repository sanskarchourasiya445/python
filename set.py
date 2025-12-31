# A set is an unordered collection of unique elements.

s = {10, 20, 30}

# Adding elements
s.add(40)
print(s)

# Removing elements
s.remove(20)     # error if not found
s.discard(100)   # no error
print(s)

# Pop (removes random element)
s.pop()
print(s)

# Length
print(len(s))

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))          # all elements
print(a.intersection(b))   # common elements
print(a.difference(b))     # a - b
print(a.symmetric_difference(b))

# Check membership
print(2 in a)

# Clear
a.clear()
print(a)
