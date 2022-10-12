"""

Little Bobby loves chocolate. He frequently goes to his favorite store, Penny Auntie, to buy them. They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.
Complete the chocolateFeast function in the code stub below to return the number of chocolates Bobby can eat with a given amount of money after taking full advantage of the promotion.
Note: Little Bobby will always turn in his wrappers if he has enough to get a free chocolate.

Input Format
The first line contains an integer, , denoting the number of scenarios to analyze.
Each of the next lines contains three space-separated integers: , , and . They represent money to spend, cost of a chocolate, and the number of wrappers he can turn in for a free chocolate.

Constraints

Output Format
For each trip to Penny Auntie, print the total number of chocolates Bobby eats on a new line.

Link to the problem: https://www.hackerrank.com/challenges/chocolate-feast/problem?isFullScreen=false

"""


def chocolateFeast(n, c, m):
    bars = n // c
    wraps = bars
    
    while wraps>=m:
        new_bars = wraps//m
        wraps = wraps - (new_bars * m) + new_bars
        bars += new_bars

    return bars
        