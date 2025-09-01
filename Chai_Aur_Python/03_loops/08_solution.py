# Problem: Check if a number is prime.

number = int(input("Enter the number: "))

if number == 0 or number == 1:
    print("Prime")
else:
    for i in range(2,number):
        if number%i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")