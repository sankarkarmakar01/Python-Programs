def fibonacci(n):
    """Recursive function to return the nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def display_fibonacci_series(terms):
    """Function to display Fibonacci series up to n terms"""
    if terms <= 0:
        print("Please enter a positive integer")
    else:
        print("Fibonacci sequence:")
        for i in range(terms):
            print(fibonacci(i), end=" ")

# Get input from user
num_terms = int(input("How many terms? "))

# Display the Fibonacci series
display_fibonacci_series(num_terms)