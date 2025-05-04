set1 = {"a", "b", "c"}
set2 = {1, 2, 3,"a"}

# set3 = set1.union(set2)
set3 = set1 | set2
print(set3)

# set4 = set1.intersection(set2)
set4 = set1 & set2
print(set4)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)
set3 = set1 - set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

# set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2
print(set3)

fruits = {"apple", "banana", "cherry"}

fruits.discard("banana")
print(fruits)