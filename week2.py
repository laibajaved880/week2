
# String methods
text = "  PCAP Certification  "
print("Original:", text)
print("Stripped:", text.strip())
print("Uppercase:", text.upper())
print("Replace:", text.replace("PCAP", "Python"))

# List methods
numbers = [3, 1, 4, 1, 5, 9]
numbers.append(2)  # Add element
numbers.sort()     # Sort list
print("Sorted numbers:", numbers)
print("Sliced list:", numbers[1:4])

# Basic try-except block
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Custom exception
class ValueTooHighError(Exception):
    pass

def check_value(n):
    if n > 100:
        raise ValueTooHighError("Value exceeds maximum limit")

try:
    check_value(150)
except ValueTooHighError as e:
    print("Custom error:", e)

# Basic OOP with inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Polymorphism in action
animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(f"{animal.name} says {animal.speak()}")

# Lambda and list comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]  # List comprehension
even = filter(lambda x: x % 2 == 0, numbers)  # Lambda + filter

print("Squared numbers:", squared)
print("Even numbers:", list(even))

# File I/O operations
with open('example.txt', 'w') as f:
    f.write("Hello from Python!\nThis is a file I/O example.")

with open('example.txt', 'r') as f:
    print("\nFile content:")
    print(f.read())

# OS module
import os
print("\nCurrent directory:", os.getcwd())
print("Files in directory:", os.listdir())