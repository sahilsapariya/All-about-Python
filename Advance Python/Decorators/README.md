# Python Decorators

Python Decorators allow you to modify the behavior of functions
and methods. They are a way to extend the functionality of a function 
or method without modifying its source code.

Decorators is a function that takes another function as argument and
returns a new function that modifies the behavior of the original function.
The new function is often referred to as a 'decoratd function'. 

Basic syntax of decorators:

```python    
@decorator_function
def my_function():
    pass
```

The @decorator_function notation is just a shorthand for the following code:

```python
def my_function():
    pass
my_function = decorator_function(my_function)
```

### Application of Decorators

Decorators are often used to add functionality to function and methods, such as logging, memoization and access control.

