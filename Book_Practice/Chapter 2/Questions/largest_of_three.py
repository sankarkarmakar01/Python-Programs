# Take 3 positive integers input and print the greatest of them.

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a > b and a > c:
    print(f"{a} is largest")
elif b > a and b > c:
    print(f"{b} is largest")
else:
    print(f"{c} is largest")