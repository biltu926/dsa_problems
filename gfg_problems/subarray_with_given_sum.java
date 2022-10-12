'''
Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
In case of multiple subarrays, return the subarray which comes first on moving from left to right.

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.

Link to the problem:
https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1?page=1&sortBy=submissions

'''

class Solution
{
    //Function to find a continuous sub-array which adds up to a given number.
    static ArrayList<Integer> subarraySum(int[] arr, int n, int s) 
    {
        int len = arr.length;
        int sum = 0;
        int start = 0;
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        for(int i=0; i<len; i++){
            sum = sum + arr[i];
            while(sum>s && start<i){
                sum = sum - arr[start];
                start = start + 1;
            }
            if(sum == s){
                result.add(start+1);
                result.add(i+1);
                return result;
            }

        }
        
        result.add(-1);
        return result;
        }
            
}