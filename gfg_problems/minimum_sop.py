'''

You are given two arrays, A and B, of equal size N.
The task is to find the minimum value of A[0] * B[0] + A[1] * B[1] + .... + A[N-1] * B[N-1],
where shuffling of elements of arrays A and B is allowed.


Example 1:

Input:
N = 3
A[] = {3, 1, 1}
B[] = {6, 5, 4}
Output:
23
Explanation:
1*6+1*5+3*4 = 6+5+12
= 23 is the minimum sum

Link to the problem: https://practice.geeksforgeeks.org/problems/minimize-the-sum-of-product1525/1?page=1&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions
'''

# The time complexity of the following algorithm is O(NlogN).
# The all possible permutations approach for both the arrays, and then finding the sop will have a
# complexity of O(N!^2) which is extremely high compared to the former approach.

class Solution:
    def minValue(self, a, b, n):
        sop = 0
        if a and b:
            a = sorted(a)
            b = sorted(b, reverse=True)
            for i in range(n):
                sop += a[i] * b[i]
        return sop


