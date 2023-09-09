'''
Given two unsorted arrays A of size N and B of size M of distinct elements, the task is to find all pairs from both arrays whose sum is equal to X.

Note: All pairs should be printed in increasing order of u. For eg. for two pairs (u1,v1) and (u2,v2), if u1 < u2 then
(u1,v1) should be printed first else second.

Example 1:

Input:
A[] = {1, 2, 4, 5, 7}
B[] = {5, 6, 3, 4, 8} 
X = 9 
Output: 
1 8
4 5 
5 4
Explanation:
(1, 8), (4, 5), (5, 4) are the
pairs which sum to 9.

Problem link: https://practice.geeksforgeeks.org/problems/find-all-pairs-whose-sum-is-x5808/1?page=1&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

'''

class Solution:
    def allPairs(self, A, B, N, M, X):
        hMap = {}
        result = []
        for i in range(N):
            hMap[str(X - A[i])] = A[i]

        
        for j in range(M):
            if str(B[j]) in hMap:
                result.append(( hMap[str(B[j])], B[j] ))

        result = sorted(result, key=lambda x:x[0])
        
        return result