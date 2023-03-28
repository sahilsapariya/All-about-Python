"""
    → Bitwise Operators in python:
        AND             &
        OR              |
        NOT             ~
        XOR             ^
        LEFT-SHIFT      <<
        RIGHT-SHIFT     >>

"""

#   AND operation:
x = 4   # 100
y = 6   # 110
#-------------
print(x & y)    # 100


#   OR operation:
x = 10  # 1010
y = 15  # 1111
print(x | y)    # 1111


#   NOT operation:
x = 13  # 1101
print(~x) # -x -1

#   XOR operator:
"""
    same bits give output 0
    different bits give 1
    NOTE: while doing XOR of more than 2 values, Do the XOR of 2 values at a time
"""
x = 13  # 1101
y = 5   # 0101
print(x ^ y)    # 1000

#   left shift operation:
"""
    let 13 << 1, gives 26
    it means add 1 zero to the right side of binary representation of 13
        or 
    multiply the number 13 by 2¹
"""
x = 13  # 1101
y = 3   

print(x << y)   # 1101000

#   right shift operation:
"""
    let x >> n, 13 >> 1 gives 6
    it means remove n digits from the right side of binary representation of x
        or
    int(x / (2 ** n))   █   divide the x with 2 power n and convert it to the integer.     
"""
x = 13  # 1101
y = 2

print(x >> y)   # 11