"""
Link to the problem: https://practice.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1


"""
class Solution:
	def pushZerosToEnd(self,arr, n):
        z_start = 0

        for i in range(n):
            if arr[i] == 0:
                z_start = i
                break
                
        for j in range(n):
            if arr[z_start] != 0:
                break
            if arr[j] > 0 and arr[z_start] == 0:
                if j>z_start:
                    arr[j], arr[z_start] = arr[z_start], arr[j]
                    z_start += 1