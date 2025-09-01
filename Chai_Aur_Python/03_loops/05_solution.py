# Problem: Given a string, find the first non-repeated character.

input_str = input("Enter the string: ")

for i in input_str:
    print(i)
    if input_str.count(i) == 1:
         print("Char is:", i)
         break