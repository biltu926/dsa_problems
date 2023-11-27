"""
Write a function that takes in a non-empty array of integers that are sorted in ascending order
and returns a new array of the same length with the squares of the original integers also sorted
in asecnding order.

"""


def sortedSquaredArray(array):
    aux = [0] * len(array)
    start = 0
    end = len(array) - 1
    k = len(aux) - 1
    
    while start<=end:
        if abs(array[start]) > abs(array[end]):
            aux[k] = array[start] * array[start]
            start += 1
        else:
            aux[k] = array[end] * array[end]
            end -= 1
        k -= 1

    return aux