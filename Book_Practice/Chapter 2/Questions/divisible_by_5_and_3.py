# Take positive integer input and tell if it is divisible by 5 and 3.

num = int(input("Enter a number:"))

if num%5 == 0 and num%3 == 0:
    print("Yes, it's divisible by 5 and 3.")
else:
    print("Yes, it's not divisible by 5 and 3.")