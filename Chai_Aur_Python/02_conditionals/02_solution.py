# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

day = input("Enter the day: ")
age = int(input("Enter your age: "))

price = 12 if age >= 18 else 8

if day == "Wednesday" or day == "wednesday":
    price -= 2
    
print(f"Ticket price for you is ${price}")
