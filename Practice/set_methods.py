thisset = {"apple", "banana", "cherry"}
print(thisset)

thisset.add("orange")
print(thisset)

set2 = {"coconut"}

thisset.update(set2)
print(thisset)


thisset.remove("coconut")
print(thisset)

thisset.discard("apple")
print(thisset)

thisset.pop()
print(thisset)

thisset.clear()
print(thisset)

# del thisset
# print(thisset)
