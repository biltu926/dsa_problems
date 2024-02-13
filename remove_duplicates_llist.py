
def removeDuplicatesFromLinkedList(linkedList):
    hMap = {}
    p = linkedList
    hMap = {
            str(linkedList.value): 1
            }
    
    while p.next:
        if str(p.next.value) in hMap.keys():
            p.next = p.next.next
        else:
            p = p.next
            hMap[str(p.value)] = 1
            
    return linkedList
