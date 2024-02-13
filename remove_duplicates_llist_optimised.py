'''
 Remove duplicate nodes from a single linked list without using an auxiliary space.
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    p = linkedList

    while p.next:
        if p.next.value == p.value:
            p.next = p.next.next
        else:
            p = p.next
            
    return linkedList
