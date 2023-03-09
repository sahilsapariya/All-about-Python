"""
    It is a devide and conqure algorithm.

    It picks an element as a pivot and partitions the given array around the picked pivot. 

    The key process in quickSort is a partition(). 
    The target of partitions is, given an array and an element x of an array as the pivot, 
    put x at its correct position in a sorted array and put all smaller elements (smaller than x) before x, 
    and put all greater elements (greater than x) after x. All this should be done in linear time.

    Partitioning:
        We start from the leftmost element and keep track of the index of smaller (or equal to) elements as i. 
        While traversing, if we find a smaller element, we swap the current element with arr[i]. 
        Otherwise, we ignore the current element.

    Time Complexity:
        Best case : O(nLogn)
        Worst case : O(n²)
"""

def partition(array : list[int], low : int, high : int) -> int:

    # Here choose the right most element as pivot element
    pivot = array[high]

    # Pointer for greater element
    i = low - 1

    # Traversing through all elements and comparing each with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            
            i += 1
            # Swaping element at i with at j
            (array[i], array[j]) = (array[j], array[i])

    # swaping the pivot element with greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quickSort(array : list[int], low : int, high : int):
    if low < high:

        pi = partition(array, low, high)

        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


if __name__ == "__main__":
    a = [453,819,32,65,0,144,357,62,-5,4,-1,-7,144]
    print("Before sorting : ", a)

    quickSort(a, 0, len(a) - 1)

    print("Sorted array : ", a)


# output:
# Before sorting :  [453, 819, 32, 65, 0, 144, 357, 62, -5, 4, -1, -7, 144]
# Sorted array :  [-7, -5, -1, 0, 4, 32, 62, 65, 144, 144, 357, 453, 819]