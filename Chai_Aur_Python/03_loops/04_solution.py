# Problem: Reverse a string using a loop.

string = input("Enter a string: ")
ans = ''

for i in string:
    ans = i + ans
    
print("Reverse string is:",ans)
