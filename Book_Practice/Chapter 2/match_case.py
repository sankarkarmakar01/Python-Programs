def match_example(value):
    match value:
        case 1:
            print("You entered number 1.")
        case 2:
            print("You entered number 2.")
        case "hello":
            print("You entered the string 'hello'.")
        case _:
            print("You entered something else.")
 
# Call the function with different values
match_example(1)       # Output: You entered number 1.
match_example(2)       # Output: You entered number 2.
match_example(3)       # Output: You entered something else.
match_example("hello") # Output: You entered the string 'hello'.
match_example("world") # Output: You entered something else.