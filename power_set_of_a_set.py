''' Given an input list, generate all possible powerset of the list '''


# The iterative solution
def powerset(array):
    subset = [[]]

    for idx in range(len(array)):
        for set in subset.copy():
            newElem = set + [array[idx]]
            subset.append(newElem)
    return subset


# The recursive solution

def powerset(array, idx=None):
    if len(array) < 1:
        return [[]]
    if idx is None:
        idx = len(array) - 1
    elif idx < 0:
        return [[]]
        
    currentElement = array[idx]
    subsets = powerset(array, idx-1)

    for i in range(len(subsets)):
        newElem = subsets[i] + [currentElement]
        subsets.append(newElem)
        
    return subsets
