"""
    Find i-th bit -> check whether its 0 or 1
"""


def extractIthBit(num, i):
    mask = 1 << i
    num = num & mask

    if num > 0:
        return 1
    return 0

print(extractIthBit(13, 1))
print(extractIthBit(13, 2))

# output:

# 0
# 1