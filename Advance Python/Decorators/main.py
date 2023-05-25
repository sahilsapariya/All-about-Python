"""
    Python Decorators allow you to modify the behavior of functions
    and methods. They are a way to extend the functionality of a function 
    or method without modifying its source code.

    Decorators is a function that takes another function as argument and
    returns a new function that modifies the behavior of the original function.
    The new function is often referred to as a 'decoratd function'. 

"""

# ! Basic Example
def greet(func):
    def mfunc(*args, **kwargs):
        print("Good Morning")

        func(*args, **kwargs)

        print("Thanks for using this function")

    return mfunc

def hello():
    print("hello world")

# @greet
def add(a, b):
    print(a + b)

# hello()
add(1, 2)
greet(add)(1, 2)

# ! Now while printing the element of list then also print the element is positive or not.
# ! If positive then print pe else ne and if zero then print z.

numbers = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]

# def sign(func):
#     def mfunc(*args, **kwargs):
        



# def print_list(numbers):
#     for i in numbers:
#         print(i)