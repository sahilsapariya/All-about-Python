"""
    In this sorting algorithm,
    counting sort will be executed the number of digits of maximum number from given array.
    Time complexity: O(n  + k)
    Space complexity: O(n  + k)
"""


def Counting(a : list[int], n : int, pos : int) -> list[int]:
    cont = [0] * 10         # because the digit is in range from 0 to 9 fixed

    for i in range(n):
        cont[int(a[i]/pos) % 10] += 1   # we want pos' digit from the a[i] i.e. int(a[i]/pos) % 10

    for i in range(1, 10):      # Modifying the cont array
        cont[i] += cont[i-1]

    b = [0] * n
    for i in range(n-1, -1, -1):
        cont[int(a[i]/pos) % 10] -= 1
        b[cont[int(a[i]/pos) % 10]] = a[i]
    
    return b


def Radix(a : list[int], n : int) -> list[int]:
    m = max(a)
    pos = 1
    
    while int(m/pos) > 0:
        a = Counting(a, n, pos)
        pos *= 10
    return a


# Driver code
if __name__ == "__main__":
    arr = [432,8,530,90,88,23,11,45,677,199]
    ans = Radix(arr, len(arr))

    print("Before sorting : ", arr)
    print("After sorting : ", ans)


# Output

# Before sorting :  [432, 8, 530, 90, 88, 23, 11, 45, 677, 199]
# After sorting :  [8, 11, 23, 45, 88, 90, 199, 432, 530, 677]