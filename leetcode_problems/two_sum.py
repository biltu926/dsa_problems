''' Description: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]. 

The solution is submitted in leetcode. Only the method is given'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        s = set()

        for i in range(len(nums)):
            if len(result) == 2:
                break

            if (target - nums[i]) in s:
                if len(result) < 1:
                    result.append(i)
                    result.append(nums.index(target - nums[i]))

            s.add(nums[i])

        return sorted(result)