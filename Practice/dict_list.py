thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for i in thisdict:
    print(i)
    print(thisdict[i])
    print(i," : ",thisdict[i])

print("---------------")

for i in thisdict.keys():
    print(i)
    
print("---------------")

for i in thisdict.values():
    print(i)

print("---------------")

for i,j in thisdict.items():
    print(i,j)