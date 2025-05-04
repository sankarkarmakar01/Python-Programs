# Write a script to calculate the square of a user-input number.

number = int(input("Enter a number: "))

square = number ** 2
print("The square of", number, "is", square)


def square_of_number(num):
    return num ** 2