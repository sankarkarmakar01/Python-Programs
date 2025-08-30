a = 10 # global variable

def my_function():
    a = 20 # local variable
    name = "Sankar"
    print("Inside function:", a)
    
print(a)
# print(name) # This will raise an error because 'name' is not defined in the global scope
my_function()