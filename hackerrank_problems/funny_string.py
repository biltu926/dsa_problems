'''
Problem link: https://www.hackerrank.com/challenges/funny-string/problem?isFullScreen=false
'''

def funnyString(s):
    # Write your code here
    rev = []
    
    for i in range(len(s)):
        rev.append(s[len(s) - i - 1])
        
    for j in range(len(rev)-1):
        lhs = abs(ord(s[j]) - ord(s[j+1]))
        rhs = abs(ord(rev[j]) - ord(rev[j+1]))
        if lhs != rhs:
            return "Not Funny"
    
    return "Funny"