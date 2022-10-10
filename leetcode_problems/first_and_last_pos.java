/*
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Problem link:
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
*/


class Solution {
    public int[] recurr(int start, int end, int[] arr, int target, int[] result){
        if(start==end){
            if(arr[start] == target && start<result[0])
                result[0] = start;
            if(arr[start] == target && start>result[1])
                result[1] = start;
            return result;
        }
        if(start>end){
            return result;
        }
        int mid = (end+start)/2;
        if(arr[mid] == target){
            if(result[0]<0)
                result[0] = mid;
            if(mid<result[0])
                result[0] = mid;
            if(mid>result[1])
                result[1] = mid;
            recurr(start, mid, arr, target, result);
            recurr(mid+1, end, arr, target, result);
        }
        else if(arr[mid]>target){
            recurr(0, mid, arr, target, result);
        }
        else if(arr[mid]<target){
            recurr(mid+1, end, arr, target, result);
        }
        return result;
    }
    public int[] searchRange(int[] nums, int target) {
        int length = nums.length;
        int[] result = new int[] {-1, -1};
        if(length == 1 && target == nums[0])
            {
                result[0] = 0;
                result[1] = 0;
                return result;
            }
        result = recurr(0, length-1, nums, target, result);
        if(result[0]<0 && result[1]>=0)
            result[0] = result[1];
        else if(result[0]>=0 && result[1]<0)
            result[1] = result[0];
        return result;
    }
}