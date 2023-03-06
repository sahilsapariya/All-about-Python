"""
    Find whether a number is EVEN or ODD
        2 methods - % (modulo operator)
                    & (bitwise AND operator)

    eg. 20
            1 0 1 0 0   == 20
        &   0 0 0 0 1   == 1
        -------------
            0 0 0 0 0   == even     else odd

    Though first method i.e. using Modulo operator 
    will be more efficient
    
"""

def evenOddAnd(num):
    if num & 1 == 1:
        return f"{num} is odd"
    return f"{num} is even"

print(evenOddAnd(20))
print(evenOddAnd(21))


# output:

# 20 is even
# 21 is odd