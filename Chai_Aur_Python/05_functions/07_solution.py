# Problem: Write a function that takes variable number of arguments and returns their sum.

def add(*args):
    return sum(args)

print(add(1,2))
print(add(1,2,3,4,5))
