# python uses the concept of shallow copy 
# so this will automatically reflects the changes in original list

def mergeSort(a):
    if len(a) > 1:

        # finding the mid of the list
        mid = len(a) // 2

        # dividing the list into two part from the mid,
        # one is left part and one is right
        L = a[:mid]
        R = a[mid:]

        # divide the list
        mergeSort(L)
        mergeSort(R)

        # conqure the list
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1
        
        # check if there is no remaining data in lists
        while i < len(L):
            a[k] = L[i]
            i += 1
            k += 1
        
        while j < len(R):
            a[k] = R[j]
            j += 1
            k += 1


if __name__ == "__main__":
    a = [453,819,32,65,0,144,357,62,-5,4,-1,-7,144]
    print("Before sorting : ", a)

    mergeSort(a)

    print("Sorted array : ", a)
