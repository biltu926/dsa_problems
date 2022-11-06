"""
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.

Link: https://leetcode.com/problems/sum-of-subarray-minimums/description/


The solution below did not pass the time constraint. It uses recursive
approach to find all the sub arrays, then computes the min sum.

"""

class Solution:
    def helper(self, arr, start, end, map_, mins):
        key = f'{start}_{end}'
        if key in map_:
            return mins
        if end > len(arr):
            return mins
        if start > len(arr):
            return mins
        else:
            if start != end:
                mins += min(arr[start:end])
            key = f'{start}_{end}'
            map_[key] = arr[start:end]
            mins = self.helper(arr, start, end+1, map_, mins)
            mins = self.helper(arr, start+1, start+1, map_, mins)
        return mins

    def sumSubarrayMins(self, arr: List[int]) -> int:
        mins = 0
        mins = self.helper(arr, 0, 0, {}, mins)
        return mins % (10**9 + 7)