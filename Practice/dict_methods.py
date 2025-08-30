thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x = thisdict["model"]
x = thisdict.get("model")
print(x)

x = thisdict.keys()
print(x)

x = thisdict.values()
print(x)

x = thisdict.items()
print(x)


print(thisdict)

thisdict.update({'year':2000})
print(thisdict)

thisdict.update({"greet":"Hello"})
print(thisdict)

thisdict.pop("greet")
print(thisdict)

thisdict.popitem()
print(thisdict)


car = {
  "brand": "Ford",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)
print(car)