'''

Given an array of integers, write a function that moves all instances of that integer
in the array to the end of the array and returns the array.

The function should be performing this in place.
 
'''

def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1

    while i<j:
        if array[i] == toMove and array[j] != toMove:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        elif array[i] == toMove and array[j] == toMove:
            j -= 1
        elif array[i] != toMove:
            i += 1
            
    return array


