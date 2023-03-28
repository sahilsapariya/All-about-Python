"""
    Set i-th bit -> change ith bit to 1
    clear i-th bit -> change ith bit to 0
"""

def setIthBit(num, i):
    mask = 1 << i
    num = num | mask
    return num

print(setIthBit(13, 1))
print(setIthBit(27, 2))

# output:
# 15
# 31


def clearIthBit(num, i):
    mask = 1 << i
    mask = ~mask
    num = num  & mask
    return num

print(clearIthBit(13, 2))

# output:
# 9


def changeIthBit(num, i, value):
    mask1 = 1 << i
    mask1 = ~mask1
    res = num & mask1
    mask2 = value << i
    res = res | mask2

    return res

print(changeIthBit(13, 1, 1))
print(changeIthBit(13, 2, 0))

# output:
# 15
# 9


def clearLastBits(num, i):
    """
        set the last i digit to 0
    """
    mask = (~0) << i
    num &= mask

    return num

print(clearLastBits(13, 3))

# output:
# 8

def setLastBits(num, i):
    """
        change the last i digit to 1
    """
    mask = ~0
    mask <<= i
    num |= ~mask
    return num

print(setLastBits(178, 3))

# output:
# 183

