# list declaration
a = list()
b = []

# 'append()' method to add elements in list
# let say we want to add "Apple" in list a.

a.append("Apple")
print(a)    # ["Apple"]

# appending the 1 to 10 numbers in list.
numbers = []
for i in range(11):
    numbers.append(i)
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# we can add different types of data type elements in same list
l = [1, 'A', 5.5, "Tech Tribe"]
print(l)    # [1, 'A', 5.5, "Tech Tribe"]

# now, we want to update element at index 1
l[1] = 99.36
print(l)    # [1, 99.36, 5.5, "Tech Tribe"]

# merging two lists into new list z
x = [1, 2, 3]
y = [9, 8, 7]
z = x + y
print(z)    # [1, 2, 3, 9, 8, 7]