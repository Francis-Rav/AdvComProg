import math

# String Operations
text = "hello world"

print("=== String Functions ===")
print(f"Original: {text}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Capitalize: {text.capitalize()}")
print(f"Title Case: {text.title()}")
print(f"Length: {len(text)}")
print(f"Replace: {text.replace('world', 'Python')}")
print(f"Split: {text.split()}")
print(f"Count 'l': {text.count('l')}")
print()

# Math Operations
number = 50

print("=== Math Functions ===")
print(f"Original number: {number}")
print(f"Absolute value: {abs(-10)}")
print(f"Round: {round(number)}")
print(f"Round to 1 decimal: {round(number, 1)}")
print(f"Square root: {math.sqrt(16)}")
print(f"Power: {pow(2, 3)}")
print(f"Max: {max(10, 20, 30)}")
print(f"Min: {min(10, 20, 30)}")
print(f"Floor: {math.floor(number)}")
print(f"Ceil: {math.ceil(number)}")
