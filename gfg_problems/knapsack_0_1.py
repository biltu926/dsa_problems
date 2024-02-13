# W = The weight of the sack.
# wt = A list of weights of the items.
# val = A list of the values of the items.
# n = Total number of items.

def knapSack(W, wt, val, n):
        # An empty 2-d matrix for the DP
        matrix = [[0 for i in range(W+1)] for j in range(n+1)] 

        # Fill up the matrix as per the logic.
        for i in range(1, n+1):
            for j in range(1, W+1):
                capWithoutItem = matrix[i-1][j]
                
                if wt[i-1] <= j:
                    capWithItem = val[i-1] + matrix[i-1][j-wt[i-1]]
                else:
                    capWithItem = 0
                    
                capacity = max(capWithoutItem, capWithItem)
                matrix[i][j] = capacity
                
    
        # The bottom right element in the matrix holds the result
        return matrix[len(matrix)-1][len(matrix[0])-1]
        
        
if __name__ == "__main__":
    print(knapSack(10, [5,4,6,3], [10,40,30,50], 4))
