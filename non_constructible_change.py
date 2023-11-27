"""
Given an array of positive integers representing the values of coins in your possession,
write a function that returns the minimum amount of change (the minimum sum of money) that
you cannot create. The given coins can have any positive integer value and aren't necessarily
unique.

For example, if you are given coins=[1, 2, 5], the minimum amount of change that you can't
create 4. If you're given no coins, the minimum amount of change that you can't create is 1.
"""

def nonConstructibleChange(coins):
    change = 0

    coins = sorted(coins)
    
    for i in range(len(coins)):
        if change + 1 < coins[i]:
            return change + 1
        change += coins[i]
        
    return change + 1
