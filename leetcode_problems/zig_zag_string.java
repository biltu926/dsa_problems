/*
Problem statement:
                    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Link to the problem: https://leetcode.com/problems/zigzag-conversion/
*/


class Solution {
    public String convert(String s, int numRows) {
        String result = "";
        int len = s.length();
        
        if(numRows == 1)
            return(s);
        
        //First row
        for(int i=0; i<len; i=i+2*(numRows-1))
            result = result + s.charAt(i);
        
        //Middle rows
        int index = 1;
        boolean direction = false;
        while(index<numRows-1){
            int i = index;
            direction = false;
            while(i<len){
                if(!direction && i<=len-1){
                    result = result + s.charAt(i);
                    i = i + 2*(numRows-1-index);
                    direction = true; // go down.
                }
                if(direction && i<=len-1){
                    result = result + s.charAt(i);
                    i = i + 2*(index);
                    direction = false; // go up.
                }
            }
            index = index+1;
        }
        
        // Last row
        for(int i=numRows-1; i<len; i=i+2*(numRows-1))
            result = result + s.charAt(i);
    return(result);
    }
}