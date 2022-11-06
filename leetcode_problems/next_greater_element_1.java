/*
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.



Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.


https://leetcode.com/problems/next-greater-element-i/description/

*/

class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] result = new int[nums1.length];
        Arrays.fill(result, -1);
        ArrayList<Integer> stack = new ArrayList<Integer>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int lenFirst = nums1.length;
        int lenSecond = nums2.length;
        int top = 0;
        stack.add(top, lenSecond-1);

        for(int j=lenSecond-2; j>=0; j--)
        {
            if(top>0 && nums2[stack.get(top)]>nums2[j]){
                map.put(nums2[j], nums2[stack.get(top)]);
            }
            else{
                if(top>=0){
                    while(top>=0 && nums2[stack.get(top)]<nums2[j])
                        {
                            stack.remove(top);
                            top -= 1;
                        }
                }
            }
            if(top>=0){
                map.put(nums2[j], nums2[stack.get(top)]);
            }
            top += 1;
            stack.add(top, j);
        }
        for(int i=0; i<lenFirst; i++){
            if(map.get(nums1[i]) != null)
                result[i] = map.get(nums1[i]);
        }
        return result;
    }
}