thistuple = ("apple", "banana", "cherry")

(a,b,c) = thistuple
print(a,b,c)

(a,*b) = thistuple
print(a)
print(b)