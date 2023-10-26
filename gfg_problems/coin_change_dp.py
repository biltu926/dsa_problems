""""
The coin change dynamic programming problem.
Problem link: https://practice.geeksforgeeks.org/problems/coin-change2448/1?page=2&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

Teh solution below does not pass all the test cases due to the longer execution time.

"""

class Solution:
    def combination(self, arr, index, target, subset, opCount, hmap):
        sum_ = 0
        
        key = '_'.join(str(i) for i in subset)
        
        if key in subset:
            return opCount
        
        for i in subset:
            sum_ += i
        
        if sum_ == target:
            opCount += 1
            return opCount
        
        if sum_ > target:
            return opCount
        
        if index >= len(arr):
            return opCount
            
        opCount = self.combination(arr, index, target, subset + [arr[index]], opCount, hmap)
        opCount = self.combination(arr, index + 1, target, subset, opCount, hmap)
        
        return opCount
        
    def count(self, coins, N, Sum):
        opCount = 0
        target = Sum
        subset = []
        opCount = self.combination(coins, 0, target, subset, opCount, {})
        return opCount