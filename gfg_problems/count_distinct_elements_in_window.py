"""
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Problem link: https://practice.geeksforgeeks.org/problems/count-distinct-elements-in-every-window/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab

Technique: Sliding window with Hash map.

"""

class Solution:
    def countDistinct(self, A, N, K):
        result = []
        hmap = {}
        c = 0

        for i in range(K):
            if A[i] not in hmap:
                hmap[A[i]] = 1
                c += 1
            else:
                hmap[A[i]] += 1
    
        result.append(c)
                
        
        for j in range(1, N-K+1):
            if hmap[A[j-1]] == 1:
                hmap[A[j-1]] -= 1
                c -= 1
            elif hmap[A[j-1]] > 1:
                hmap[A[j-1]] -= 1
                
            if A[j+K-1] in hmap and hmap[A[j+K-1]] > 0:
                hmap[A[j+K-1]] += 1
            elif A[j+K-1] not in hmap or hmap[A[j+K-1]] == 0:
                hmap[A[j+K-1]] = 1
                c += 1
                
            result.append(c)

        return result