# Take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15.

num = int(input("Enter the number: "))

if num%5 == 0:
    if num%3 == 0:
        if num%15 != 0:
            print("This number is divisible by 5 or 3 but not divisible by 15.")
# else:
#     print("Condition not satisfy")