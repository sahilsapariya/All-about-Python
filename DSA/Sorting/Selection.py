"""
    Selection sort is a simple and efficient sorting algorithm that
    works by repeatedly selecting the smallest (or largest) element
    from the unsorted portion of the list and moving it to the sorted portion of the list. 

    The algorithm repeatedly selects the smallest (or largest) element
    from the unsorted portion of the list and swaps it with the first element of the unsorted portion.

    This process is repeated for the remaining unsorted portion of the list until the entire list is sorted.
"""


def SelectionSort(A : list[int]) -> list[int]:
    # Traverse through all array elements
    for i in range(len(A)):
        
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        A[i], A[min_idx] = A[min_idx], A[i]

    return A

# Driver code to test above
A = [64, 25, 12, 22, 11]
print ("Sorted array : ", SelectionSort(A))



# Output:
# Sorted array :  [11, 12, 22, 25, 64]