# Problem: Compute the factorial of a number using a while loop.

number = int(input("Enter the number: "))
fact = 1

while number > 0:
    fact *= number
    number -= 1

print(f"Factorial is: {fact}")
