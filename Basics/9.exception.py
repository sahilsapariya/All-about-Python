# Syntax errors occur when the parser detects an incorrect statement.
# eg.
    # >>> print( 0 / 0 ))
    #   File "<stdin>", line 1
    #     print( 0 / 0 ))
    #                   ^
    # SyntaxError: invalid syntax



# Raising an Exception

# We can use raise to throw an exception if a condition occurs. 
# The statement can be complemented with a custom exception.

x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

# output:
# Traceback (most recent call last):
#   File "<input>", line 4, in <module>
# Exception: x should not exceed 5. The value of x was: 10


# Handling the errors with try-except 

try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')

# output:   if error/exception occurs
# Could not open file.log



# Cleaning Up After Using finally

# Imagine that you always had to implement some sort of action to clean up after executing your code.
# Python enables you to do so using the finally clause.
import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')

# Everything in the finally clause will be executed. 
# It does not matter if you encounter an exception somewhere in the try or else clauses.

# output
# Function can only run on Linux systems.
# Cleaning up, irrespective of any exceptions.