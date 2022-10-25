/*
Problem statement:
Lisa just got a new math workbook. A workbook contains exercise problems, grouped into chapters. Lisa believes a problem to be special if its index (within a chapter) is the same as the page number where it's located. The format of Lisa's book is as follows:
There are  chapters in Lisa's workbook, numbered from  to .
The  chapter has  problems, numbered from  to .
Each page can hold up to  problems. Only a chapter's last page of exercises may contain fewer than  problems.
Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
The page number indexing starts at .
Given the details for Lisa's workbook, can you count its number of special problems?
Example 
 

Lisa's workbook contains  problems for chapter , and  problems for chapter . Each page can hold  problems.
The first page will hold  problems for chapter . Problem  is on page , so it is special. 
Page  contains only Chapter , Problem , so no special problem is on page . 
Chapter  problems start on page  and there are  problems. Since there is no problem  on page , there is no special problem on that page either. 
There is  special problem in her workbook.

Link to the problem: https://www.hackerrank.com/challenges/lisa-workbook/copy-from/297724060

*/


class Result {
    public static int workbook(int n, int k, List<Integer> arr) {
    
    int pageNumber = 0;
    int problemIndex = 0;
    int pageCapacity = 1;
    int index = 1;
    int special = 0;
    
    while(problemIndex < arr.size()){
        int probs = arr.get(problemIndex);
        pageCapacity = 1;
        pageNumber += 1;
        for(index=1; index<=probs; index++){
            if(pageCapacity > k){
                pageNumber += 1;
                pageCapacity = 1;
                if(pageNumber == index) special += 1;
            }
            else if(pageNumber == index) special += 1;
            pageCapacity += 1;
        }
        problemIndex += 1;
    }
    return special;
}
}