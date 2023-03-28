"""
    Bucket Sort is a sorting algorithm that divides 
    the unsorted array elements into several groups called buckets.

    Each bucket is then sorted by using any of the suitable sorting algorithms 
    or recursively applying the same bucket algorithm. 
    (Here I have used insertion sort)

    Finally, the sorted buckets are combined to form a final sorted array.

    Time complexity: 
        → best case:    O(n)
        → worst case:   O(n²)

    Space complexity:   O(n)
"""

from math import floor

def BucketSort(a : list[int]) -> list[list[int]]:

    n = len(a)
    b = [[] for _ in range(n)]

    # each element is placed according to it's bucket.
    for i in a:
        b[floor(n * i)].append(i)

    # sorting all the buckets using insertion sort 
    for l in b:
        for i in range(1, len(l)):
            while l[i-1] > l[i] and i > 0:
                l[i-1], l[i] = l[i], l[i-1]
                i -= 1

    # combining all the buckets and return it.
    temp = []
    for l in b:
        for i in l:
            temp.append(i)
    return temp


# Driver code
if __name__ == "__main__":
    a = [0.79,0.13,0.65,0.64,0.39,0.20,0.89,0.53,0.42,0.06,0.94]
    print("Before sorting : ", a)

    a = BucketSort(a)
    print("After sorting : ", a)


# output:

# Before sorting :  [0.79, 0.13, 0.65, 0.64, 0.39, 0.2, 0.89, 0.53, 0.42, 0.06, 0.94]
# After sorting :  [0.06, 0.13, 0.2, 0.39, 0.42, 0.53, 0.64, 0.65, 0.79, 0.89, 0.94]