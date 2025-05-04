# Take an integer input and tell if it is positive or negative or zero

number = int(input("Enter the number:"))

if number == 0:
    print("The number is zero")
elif number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("It is not a number...")