"""
    if score greter 10 then win else loose
"""

score = 10

if score > 10:
    print("You won")
else:
    print("Better Luck Next Time")


"""
    if grade greater 90 -> A
    greater 80 -> B
    greater 70 -> C
    greater 60 -> D
    else E
"""

grade=95

if grade < 60:
    print("E")
elif grade > 60 and grade < 70:
    print("D")
elif grade > 70 and grade < 80:
    print("C")
elif grade > 80 and grade < 90:
    print("B")
else:
    print("A")

# similar to this there is switch-case statement
