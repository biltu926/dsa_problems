"""
Given an array of 0s and 1s. 
Find the length of the largest subarray with equal number of 0s and 1s.

Program link: https://practice.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

"""

class Solution:
    def maxLen(self,arr, N):
        maxLen = -1
        
        for i in range(N):
            if arr[i] == 0:
                arr[i] = -1
                
        hmap = {str(arr[0]): 0}
        sum_ = arr[0]
        
        for j in range(1, N):
            sum_ = sum_ + arr[j]
            if str(sum_) == "0":
                maxLen = max(maxLen, j+1)
            else:
                if str(sum_) not in hmap:
                    hmap[str(sum_)] = j
                else:
                    maxLen = max(maxLen, j - hmap[str(sum_)])
                
        if maxLen < 0:
            maxLen = 0
        return maxLen