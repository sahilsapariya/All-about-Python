"""
    Here in array all the values occoured times 
    except for one value.
    find that unique number.

    By XORing we can eliminate the same numbers.
        eg. x ^ x = 0
            x ^ 0 = x

    Time complexity: O(n)
    Space complexity: O(1)
"""


def uniqueNumber(a):
    ans = 0
    for number in a:
        ans = ans ^ number
    return ans

duplicate_list1 = [-1,0,1,9,-2,11,0,1,0,-2,9,11]
duplicate_list2 = [-1,0,1,9,-2,11,-1,1,-2,9,11]
duplicate_list3 = [-1,0,1,9,-2,11,0,-1,-2,1,11]

print(uniqueNumber(duplicate_list1))
print(uniqueNumber(duplicate_list2))
print(uniqueNumber(duplicate_list3))