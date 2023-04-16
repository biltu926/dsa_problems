'''
You are the benevolent ruler of Rankhacker Castle, and today you're distributing bread. 
Your subjects are in a line, and some of them already have some loaves. 
Times are hard and your castle's food stocks are dwindling, 
so you must distribute as few loaves as possible according to the following rules:
Every time you give a loaf of bread to some person , 
you must also give a loaf of bread to the person immediately in front of or behind them in the line (i.e., persons  or ).
After all the bread is distributed, each person must have an even number of loaves.
Given the number of loaves already held by each citizen, find and print the minimum number of loaves you must distribute to satisfy the two rules above. If this is not possible, print NO.


Problem link: https://www.hackerrank.com/challenges/fair-rations/problem?isFullScreen=true
'''

def fairRations(B):
    shifts = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i+1] += 1
            shifts += 2

    for i in range(len(B)):
        if B[i] % 2 != 0:
            return 'NO'
    return str(shifts)
