"""
    Insertion sort is a simple sorting algorithm 
    that works similar to the way you sort playing cards in your hands.

    The array is virtually split into a sorted and an unsorted part.

    The array is virtually split into a sorted and an unsorted part.

    Characteristics of Insertion Sort:
        → This algorithm is one of the simplest algorithm with simple implementation
        → Basically, Insertion sort is efficient for small data values
        → Insertion sort is adaptive in nature, 
          i.e. it is appropriate for data sets which are already partially sorted.
"""

def insertionSort(arr : list[int]) -> list[int]:
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key
    
    return arr
 
# Driver code to test above
arr = [12, 11, 13, 5, 6]
print("Sorted array : ", insertionSort(arr))

# output:
# Sorted array :  [5, 6, 11, 12, 13]