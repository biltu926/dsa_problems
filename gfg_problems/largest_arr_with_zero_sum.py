'''

Given an array having both positive and negative integers. The task is to compute the length of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.
Your Task:
You just have to complete the function maxLen() which takes two arguments an array A and n, where n is the size of the array A and returns the length of the largest subarray with 0 sum.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Link to the problem: https://practice.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1?page=1&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

'''


class Solution:
    def maxLen(self, n, arr):
        if not arr:
            return

        if len(arr) == 1:
            return 1

        map_ = {}
        subarrSum = 0
        subarrLength = 0

        for i in range(n):
            subarrSum += arr[i]
            if subarrSum == 0:
                if i > subarrLength:
                    subarrLength = i + 1
            if subarrSum in map_:
                currLength = i - map_.get(subarrSum)
                if currLength > subarrLength:
                    subarrLength = currLength
            else:
                map_[subarrSum] = i

        # print(subarrLength)
        return subarrLength