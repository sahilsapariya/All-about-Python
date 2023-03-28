# Declaring the empty dict by two ways
dict1 = dict()
dict2 = {}

a = [1, 2, 3, 4, 5]
dict = {
    "Name": "Minato",
    "Nick-name": "Yellow Flash",
    "post": "Hokage",
    "Missons": 999,
    "stars": a,
}
print(dict)

# Creting the element of dictionary
a = [1, 2, 3, 4, 5]
dict2["stars"] = a
print(dict2)

print(type(dict.keys()))
print(dict.values())

# appending one dict to another
d1 = {
    "name": "tomy",
    "email": "tomy@gmail.com"
}
d2 = {
    "contact": 7984564562
}
print(d1)
print(d2)

# method 1
d1.update(d2)
print(d1)

print(d1["name"])


# method 2  using the concept of kwargs.
d3 = {**d1, **d2}
print(d3)