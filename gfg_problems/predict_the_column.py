""" Problem statement: https://www.geeksforgeeks.org/problems/predict-the-column/1
"""

class Solution:
    def columnWithMaxZeros(self,arr,N):
        
        aux = [0] * N
        
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    aux[j] += 1
                    

        maxZeroes = max(aux)
        
        if maxZeroes <= 0:
            return -1
        
        for i in range(N):
            if aux[i] == maxZeroes:
                return i
            
        
        return -1