# Swap two variables without using a temporary variable.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Before swapping:")
print("First number:", a)
print("Second number:", b)
a,b = b,a
print("After swapping:")
print("First number:", a)
print("Second number:", b)