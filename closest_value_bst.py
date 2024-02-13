''' Given a BST, and a target find out the closest value present in the BST '''

def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(closest - target) > abs(tree.value - target):
        closest = tree.value

    if target < tree.value:
        return findClosestValueHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueHelper(tree.right, target, closest)
    else:
        return closest
        
    
def findClosestValueInBst(tree, target):
    closest = float("inf")
    return findClosestValueHelper(tree, target, closest)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

