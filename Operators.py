# Python Operators

## 🔹 1. Arithmetic Operators - used for mathematical calculations.

| Operator | Meaning |
|--------|--------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Modulus (remainder) |



## 🔹 2. Comparison Operators - used to compare two values.  
## result is always **True** or **False**.

| Operator | Meaning |
|--------|--------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

## 🔹 3. Logical Operators - used to combine conditions.

| Operator | Meaning |
|--------|--------|
| `and` | True if both conditions are True |
| `or` | True if at least one condition is True |
| `not` | Reverses the result |



## 🔹 4. Assignment Operators - used to assign and update values.

| Operator | Example |
|--------|--------|
| `=` | x = 5 |
| `+=` | x += 2 |
| `-=` | x -= 2 |
| `*=` | x *= 2 |
| `/=` | x /= 2 |

# -------- Arithmetic Operators --------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)

# -------- Comparison Operators --------
print("\nComparison Operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

# -------- Logical Operators --------
x = True
y = False

print("\nLogical Operators")
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

# -------- Assignment Operators --------
print("\nAssignment Operators")

c = a
print("Initial value of c:", c)

c += 5
print("c += 5:", c)

c -= 2
print("c -= 2:", c)

c *= 3
print("c *= 3:", c)

c /= 2
print("c /= 2:", c)
