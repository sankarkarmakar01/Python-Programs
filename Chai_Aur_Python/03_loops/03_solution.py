# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

number = int(input("Enter the number: "))

for i in range(1,11):
    mul = number * i
    print(f"{number} x {i} = {mul}")
