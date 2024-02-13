'''
Longest peak: Write a function that takes in an array of integers and returns the length of the longest peak in the array.

A peak is defined as adjacent integers in the array that are strictly increasing until they reach a tip(the highest value in the peak), at which
point they become strictly decreasing. At least three integers are required to form a peak.

For example, the integers 1, 4, 10, 2 form a peak, but the integers 4, 0, 10 don't and neither do the integers 1, 2, 2, 0.
'''

def longestPeak(array):
    maxPeakLength = 0
    i = 1

    while i < len(array) - 1:
        isPeak = True if (array[i-1] < array[i]) and (array[i] > array[i+1]) else False

        if isPeak:
            leftIdx = i - 2
            rightIdx = i + 2
            
            while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
                leftIdx -= 1
            while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
                rightIdx += 1
                
            maxPeakLength = max(maxPeakLength, rightIdx - leftIdx - 1)
            
            i = rightIdx
        else:
            i += 1
            
    return maxPeakLength
