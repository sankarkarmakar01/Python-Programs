myList = [1,2,3]
print(myList)

myList.append(10)
print(myList)

myList.insert(0,"Sankar")
print(myList)

list2 = [100,200]
myList.extend(list2)
print(myList)

list3 = ['a','b']

list4 = list2 + list3
print(list4)

myList.remove("Sankar")
print(myList)

myList.pop()
print(myList)

myList.pop(3) # 3 -> index
print(myList)

del myList[0]
print(myList)



newList = [100,5,99,63,77,100]

print(newList.count(100))
print(newList.index(5))

newList.reverse()
print(newList)