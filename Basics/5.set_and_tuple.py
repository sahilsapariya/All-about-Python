# Tuple: A Tuple is a collection of Python objects separated by commas. 
#       In some ways, a tuple is similar to a list in terms of 
#       indexing, nested objects, and repetition but a tuple is immutable, 
#       unlike lists that are mutable.

_name = ("sahil",)
_surname = ("sapariya",)

_fullname = _name + _surname

print(_fullname)    # ('sahil', 'sapariya')

# we cannot add add or remove or update the tuple.

# Here tuple() is constructor of tuple class. and it takes only one arguments.
# that's why we added double brackets.

thistuple = tuple(("apple",))
print(thistuple)    # ('apple',)

thistuple = tuple(("apple"))
print(thistuple)    # ('a', 'p', 'p', 'l', 'e')



# Set:  A Set is an unordered collection data type that is 
#       iterable, mutable, and has no duplicate elements. 
#       Python’s set class represents the mathematical notion of a set.

thisset = set()

thisset.add(1)
thisset.add(2)
print(thisset)  # {1, 2}

thisset.remove(1)
print(thisset)  # {2}

thisset = set((1, 1, 2, 3, 4, 4, 5, 5, 5, 10))
print(thisset)  # {1, 2, 3, 4, 5, 10}

thisset.update((10, 11))    # update() will take union of input set with thisset
                            # and assign it to thisset
print(thisset)  # {1, 2, 3, 4, 5, 10, 11}