# Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

animal = input("Enter the animal(Dog/Cat): ")
age = int(input("Enter the age: "))


if animal == "Dog" and age < 2:
    print("Puppy food")
elif animal == "Cat" and age > 5:
    print("Senior cat food")
