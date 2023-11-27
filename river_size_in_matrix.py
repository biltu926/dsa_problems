
def traverseMatrix(matrix, visited, sizes, stack, currSize):
    while stack:
        i, j = stack.pop(len(stack) - 1)
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        if matrix[i][j] == 1:
            currSize += 1
            for child in childNodes(i, j, matrix, visited):
                i, j = child
                if not visited[i][j]:
                    node=[i,j]
                    stack.append(node)
            currSize = traverseMatrix(matrix, visited, sizes, stack, currSize)
    return currSize


def childNodes(i, j, matrix, visited):
    children = []
    if i<len(matrix)-1:
        if not visited[i+1][j]:
            children.append([i+1, j])
    if i>0:
        if not visited[i-1][j]:
            children.append([i-1, j])
    if j<len(matrix[0])-1:
        if not visited[i][j+1]:
            children.append([i, j+1])
    if j>0:
        if not visited[i][j-1]:
            children.append([i, j-1])
            
    return children


def riverSizes(matrix):
    if matrix:
        # array to store the sizes of the rivers
        sizes = []
        # an auxiliary matrix to keep track of the visited nodes.
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if visited[i][j]:
                    continue
                if matrix[i][j] == 1:
                    size = traverseMatrix(matrix, visited, sizes, [[i,j]], 0)
                    sizes.append(size)
    return sizes
