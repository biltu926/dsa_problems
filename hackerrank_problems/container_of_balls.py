'''

David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.
David wants to perform some number of swap operations such that:
Each container contains only balls of the same type.
No two balls of the same type are located in different containers.

Link to the problem: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem?isFullScreen=false

'''


def organizingContainers(container):
    # Write your code here
    container_ordered = [0] * 100
    balls_ordered = [0] * 100

    for i in range(len(container)):
        container_ordered[i] = sum(container[i])

    for i in range(len(container)):
        for j in range(len(container)):
            balls_ordered[j] += container[i][j]

    if sorted(container_ordered) == sorted(balls_ordered):
        return "Possible"

    return "Impossible"
