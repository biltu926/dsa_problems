# Merge sort iterative

def merge(arr, l1, r1, l2, r2):

    arrL = arr[l1:r1+1]
    arrR = arr[l2:r2+1]

    i = 0
    j = 0
    k = l1
    
    while i < len(arrL) and j < len(arrR):
        if arrL[i] <= arrR[j]:
            arr[k] = arrL[i]
            i += 1
        else:
            arr[k] = arrR[j]
            j += 1
        k += 1
    
    while i < len(arrL):
        arr[k] = arrL[i]
        i += 1
        k += 1
        
    while j < len(arrR):
        arr[k] = arrR[j]
        j += 1
        k += 1


def mergeSort(arr, l, n):
    span = 1
    while span < n+1:
        i = 0
        while i < n+1:
            # The left block
            l1 = i
            r1 = i + span - 1
            
            # The right block
            l2 = i + span
            r2 = i + 2*span - 1
            
            if r2 > n:
                r2 = n
            if l2 > n:
                break

            merge(arr, l1, r1, l2, r2)
            
            i += 2*span
        span = 2*span


arr = [4,10,3,97,1,35]
print(arr)
mergeSort(arr, 0, len(arr)-1)
print(arr)
