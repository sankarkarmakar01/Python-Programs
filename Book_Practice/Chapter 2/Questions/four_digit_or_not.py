#  Take positive integer input and tell if it is a four digit number or not.

num = int(input("Enter a number:"))

list1 = list()

while num != 0:
    rem = int(num%10)
    list1.append(rem)
    num = num//10

if len(list1) == 4:
    print("The number is four digits")
else:
    print("The number is not four digits")