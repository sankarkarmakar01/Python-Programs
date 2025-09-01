# Problem: Keep asking the user for input until they enter a number between 1 and 10.

while True:
    num = int(input("Enter the number: "))
    if num not in range(1,11):
        print("Please enter the number in range of 1 to 10.")
        continue
    else:
        print("OK")
        break
