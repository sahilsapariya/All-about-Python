"""
    Explanation:
        Counting(a, n, k) will return sorted array.
            → 'a' is the array to be sorted
            → 'n' is the length of the array 'a'
            → 'k' is the maximum element of array 'a'

        1) We will make the 'count' array of size k and initialized it with 0
           It will store the occurance of the element a[i] at index count[a[i]]

        2) Modify the count array.

        3) create the another array of size n and 
           find the index of each element of original array in count array which gives the cummulative count.

        4) Return the answer.

"""
        

def Counting(a : list, n : int, k : int) -> list[int]:
    # !step 1: 
    cont = [0] * (k + 1)
    for i in range(n):
        cont[a[i]] += 1

    # !step 2:
    for i in range(1, k + 1):
        cont[i] += cont[i - 1]
    
    # !step 3:
    b = [0] * n
    for i in range(n - 1, -1, -1):
        cont[a[i]] -= 1
        b[cont[a[i]]] = a[i]

    # !step 4:
    return b



if __name__ == "__main__":
    arr = [2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
    k = max(arr)
    n = len(arr)
    ans = Counting(arr, n, k)
    print("Before sorting : ", arr)
    print("After sorting : ", ans)
    

# Output:

# Before sorting :  [2, 1, 1, 0, 2, 5, 4, 0, 2, 8, 7, 7, 9, 2, 0, 1, 9] 
# After sorting :  [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 4, 5, 7, 7, 8, 9, 9] 