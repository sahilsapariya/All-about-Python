# Functions

# Declaring the function.
def function_name(param):
    print(param)


# Function to find factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n*factorial(n)

ans = factorial(5)
print(ans)