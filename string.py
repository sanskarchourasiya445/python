# PYTHON STRING METHODS 

#String Creation
s = "  Hello Python World  "
print(s)

#Indexing & Slicing
print(s[2])        # character at index 2
print(s[-1])       # last character
print(s[2:7])      # slicing
print(s[:5])       # from start
print(s[6:])       # till end

#Case Methods (VERY COMMON)
text = "python programming"
print(text.upper())      # PYTHON PROGRAMMING
print(text.lower())      # python programming
print(text.title())      # Python Programming
print(text.capitalize()) # Python programming
print(text.swapcase())   # PYTHON PROGRAMMING

#Strip Methods (Used a LOT)
name = "   Sanskar   "
print(name.strip())      # removes both sides spaces
print(name.lstrip())     # removes left spaces
print(name.rstrip())     # removes right spaces

#Replace
sentence = "I love Python"
print(sentence.replace("Python", "Coding"))

#Join & Alignment
langs = ["Python", "Java", "C++"]
joined = ", ".join(langs)
print(joined)

print("Python".center(10, "-"))  # --Python--
print("Python".ljust(10, "-"))   # Python----
print("Python".rjust(10, "-"))   # ----Python

# Searching & Checking
msg = "learn python fast"
print(msg.find("python"))     # returns index
print(msg.count("n"))         # count occurrences
print(msg.startswith("learn"))
print(msg.endswith("fast"))

print("123".isdigit())        # True
print("abc".isalpha())        # True
print("abc123".isalnum())     # True
print(" ".isspace())          # True

#String Formatting
name = "Sanskar"
age = 20
# f-string
print(f"My name is {name} and I am {age} years old")
# format()
print("My name is {} and I am {} years old".format(name, age))


