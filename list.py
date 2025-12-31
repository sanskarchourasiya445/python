# A list is an ordered, mutable collection
# that can store different data types.

nums = [10, 20, 30, 40]

# Accessing elements
print(nums[0])
print(nums[-1])

# Slicing
print(nums[1:3])

# Adding elements
nums.append(50)          # add at end
nums.insert(1, 15)       # add at index
print(nums)

# Removing elements
nums.remove(20)          # remove by value
nums.pop()               # remove last element
nums.pop(1)              # remove by index
print(nums)

# Length
print(len(nums))

# Sorting
nums.sort()              # ascending
nums.sort(reverse=True)  # descending
print(nums)

# Reverse
nums.reverse()
print(nums)

# Searching
print(nums.index(30))    # index of element
print(nums.count(30))    # frequency

# Copy
new_nums = nums.copy()
print(new_nums)

# Clear
nums.clear()
print(nums)
