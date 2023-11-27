"""
Given two non-empty arrays of integers, write a function that determines whether the second
array is a subsequence of the first one. 

Ex:
Array A = [22, 25, 6] is a subsequence of array B = [5, 1, 22, 25, 6, -1, 8, 10];

Note: A single number in an array and the array itself are both valid
subsequences of the array.

"""


def isValidSubsequence(array, sequence):
    if not sequence:
        return True
    head = 0

    for i in range(len(array)):
        if head<len(sequence) and array[i] == sequence[head]:
            head += 1

    if head == len(sequence):
        return True
        
    return False