def partition(arr, left, right, k):
    pivot = arr[right-1]
    i = left - 1
    j = left
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    if i < j:
        arr[i+1], arr[j] = arr[j], arr[i+1]
    return i+1

def k_th_smallest(arr, left, right, k):
    if not arr:
        print(f" Invalid array ")
    pivotIndex = partition(arr, left, right, k)
    pos = pivotIndex - left + 1
    if pos == k:
        print(arr[pivotIndex])
    elif pos < k:
        k_th_smallest(arr, pivotIndex+1, right, k-pivotIndex)
    elif pos > k:
        k_th_smallest(arr, left, pivotIndex-1, k)

if __name__ == "__main__":
    arr = [1, 9, 2, 3, 7, 4, 6]
    left = 0
    right = len(arr)
    k = 5
    print(sorted(arr))
    k_th_smallest(arr, left, right, k)
