''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

def traverse(root, map_, level):
    if not root:
        return
    if str(level) not in map_:
        #print(str(level))
        map_[str(level)] = root.data
    if root.left:
        traverse(root.left, map_, level+1)
    if root.right:
        traverse(root.right, map_, level+1)

    return

#Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    map_ = {}
    level = 0
    result = []
    traverse(root, map_, level)

    for i in range(len(map_)):
        result.append(map_.get(str(i)))

    return result
    # code here
