'''
Link to the problem: 

'''

def twoStacks(maxSum, a, b):
    i, j, currSum, maxCount = 0, 0, 0, 0
    
    while i<len(a) and currSum + a[i] <= maxSum:
        currSum += a[i]
        i += 1
        
    if currSum > maxSum:
        i -= 1
        maxCount = max(maxCount, i)
    else:
        maxCount = max(maxCount, i)
        i -= 1

    while j < len(b) and currSum <= maxSum:
        currSum += b[j]
        j += 1
        while currSum > maxSum and i >= 0:
            currSum -= a[i]
            i -= 1
        if currSum <= maxSum:
            maxCount = max(maxCount, i + j + 1)

    return maxCount