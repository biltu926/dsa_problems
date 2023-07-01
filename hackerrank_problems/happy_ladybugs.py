"""
Happy Ladybugs is a board game having the following properties:
The board is represented by a string, , of length . The  character of the string, , denotes the  cell of the board.
If  is an underscore (i.e., _), it means the  cell of the board is empty.
If  is an uppercase English alphabetic letter (ascii[A-Z]), it means the  cell contains a ladybug of color .
String  will not contain any other characters.
A ladybug is happy only when its left or right adjacent cell (i.e., ) is occupied by another ladybug having the same color.
In a single move, you can move a ladybug from its current position to any empty cell. 
Given the values of  and  for  games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy. For each game, return YES if all the ladybugs can be made happy through some number of moves. Otherwise, return NO. 
Example 

You can move the rightmost  and  to make  and all the ladybugs are happy. Return YES.

Link to the problem: https://www.hackerrank.com/challenges/happy-ladybugs/problem?isFullScreen=false

"""


def happyLadybugs(b):
    counter = {}
    stack = []
    
    for c in b:
        if c != "_":
            counter[c] = counter.get(c, 0) + 1
    if not counter:
        return "YES"
    
    if min(counter.values()) == 1:
        return "NO"
    elif "_" in b:
        return "YES"

    for c in b:
        if not stack:
            stack.append(c)
        elif stack[len(stack) - 1] == c:
            stack.pop(len(stack) - 1)
        else:
            stack.append(c)
            
    if len(stack) in [0, 1]:
        return "YES"
    
    return "NO"

        