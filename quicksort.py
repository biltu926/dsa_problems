def partition(arr, low, high):
    pivot = high
    index = low
    
    for i in range(low, high+1):
        if arr[i] < arr[pivot]:
            arr[i], arr[index] = arr[index], arr[i]
            index += 1
    arr[pivot], arr[index] = arr[index], arr[pivot]
    return index


def quickSort(arr, low, high):
    if low<high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


if __name__ == "__main__":
    arr = [4,1,3,2,5]
    quickSort(arr, 0, len(arr)-1)