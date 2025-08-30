# Take a positive integer input and tell if it is even or odd

number = int(input("Enter any integer: "))

if number%2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")