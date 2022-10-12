/*
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Problem link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int length = s.length();
        if(length == 0)
            return 0;
        if(length == 1)
            return 1;
        int i = 0;
        int j = 0;
        int maxLength = 1;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();

        for(i=0; i<length-1; i++){
            map.clear();
            map.put(s.charAt(i), 1);
            for(j=i+1; j<length; j++){
                if(map.containsKey(s.charAt(j))){
                    break;
                }
                else{
                    map.put(s.charAt(j), 1);
                    if(j-i+1 > maxLength){
                        maxLength = j-i+1;
                    }
                }
            }
        }
        return maxLength;
    }
}