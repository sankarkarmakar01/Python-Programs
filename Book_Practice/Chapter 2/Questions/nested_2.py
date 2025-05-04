#  Take 3 positive integers input and print the greatest of them (without using multiple condition)

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
c = int(input("Enter the third number:"))

if a > b:
    if a > c:
        print(f"{a} is largest")
if b > a:
    if b > c:
        print(f"{b} is largest")
else:
    print(f"{c} is largest")
        