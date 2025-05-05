a = input("Enter the number:")
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except ValueError:
    print("Invalid Code...")
# except:
#     print("Invalid Code...")
# except Exception as e:
#     print(e)
    
print("End...")