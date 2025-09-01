# Problem: Calculate the sum of even numbers up to a given number n.

n = int(input("Enter the last number of the range:"))
add = 0

for i in range(1,n+1):
    if i%2 == 0:
        add += i

print("The sum of even numbers is: ",add)
