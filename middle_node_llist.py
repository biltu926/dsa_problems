'''
Find and return the middle node of the linked list
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    ptr = linkedList
    rptr = linkedList
    nodeCount = 1
    count = 0
    
    while ptr.next:
        ptr = ptr.next
        nodeCount += 1

    if nodeCount == 1:
        return linkedList
    else:
        while rptr.next:
            if count == (nodeCount // 2):
                return rptr
            count += 1
            rptr = rptr.next
    
    return None

