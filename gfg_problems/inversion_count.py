"""
    The inversion count problem from GfG using merge sort and a counter.
"""


def mergeSort(arr, left, right, counter):
    mid = left + (right-left) // 2
    if left<mid<right:
        counter = mergeSort(arr, left, mid, counter)
        counter = mergeSort(arr, mid, right, counter)
        counter = merge(arr, left, mid, right, counter)
    return counter

def merge(arr, l, m, r, counter):
    print(f" Merging: {l}, {m}, {r}")
    L = arr[l:m]
    R = arr[m:r]
    
    i = j = 0
    k = l
    print(L, R)
    while i<len(L) and j<len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
            counter += len(L) - i
            print(f" Inversion {L}, {R}, {counter}")
        k += 1
        
    while i<len(L):
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j<len(R):
        arr[k] = R[j]
        j += 1
        k += 1
        
    return counter


if __name__ == "__main__":
    arr = [2, 3, 4, 5, 1, 1]
    counter = 0
    print(f" Before: {arr} ")
    counter = mergeSort(arr, 0, len(arr), counter)
    print(f" After: {arr}, {counter} ")