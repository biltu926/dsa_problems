'''


Example 1:

Input:
r = 4, c = 4
matrix[][] = {{1, 2, 3, 4},
           {5, 6, 7, 8},
           {9, 10, 11, 12},
           {13, 14, 15,16}}
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10

Link to the problem: https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1?utm_source=geeksforgeeks&utm_medium=article_practice_tab&utm_campaign=article_practice_tab

'''

class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        left, right, top, bottom = 0, c- 1, 0, r - 1

        result = []

        while len(result) < r * c:
            for i in range(left, right + 1):
                result.append(matrix[left][i])
            top += 1

            if len(result) >= r * c:
                break

            for j in range(top, bottom + 1):
                result.append(matrix[j][right])
            right -= 1

            if len(result) >= r * c:
                break

            for k in range(right, left - 1, -1):
                result.append(matrix[bottom][k])
            bottom -= 1

            if len(result) >= r * c:
                break

            for l in range(bottom, top - 1, -1):
                result.append(matrix[l][left])
            left += 1

        return result