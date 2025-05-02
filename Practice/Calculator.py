a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operator(+, -, *, /, %): ")

if op == '+':
    print(f"The addition of {a} and {b} is: {a + b}")
elif op == '-':
    print(f"The substraction of {a} and {b} is: {a - b}")
elif op == '*':
    print(f"The multiplication of {a} and {b} is: {a * b}")
elif op =='/':
    print(f"The division of {a} and {b} is: {a / b}")
elif op == '%':
    print(f"The module division of {a} and {b} is: {a % b}")
else:
    print("Please input valid inputs....")
