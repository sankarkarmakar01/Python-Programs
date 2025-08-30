def greet():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occoured....")
    finally:
        print("Hello, I am finally")
        
greet()