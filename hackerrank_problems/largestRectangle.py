'''
Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. Your task is to find the largest solid area in which the mall can be constructed.

There are a number of buildings in a certain two-dimensional landscape. Each building has a height, given by . If you join  adjacent buildings, they will form a solid rectangle of area .

Example

A rectangle of height  and length  can be constructed within the boundaries. The area formed is .

Function Description

Complete the function largestRectangle int the editor below. It should return an integer representing the largest rectangle that can be formed within the bounds of consecutive buildings.

largestRectangle has the following parameter(s):

int h[n]: the building heights
Returns
- long: the area of the largest rectangle that can be formed within the bounds of consecutive buildings

Input Format

The first line contains , the number of buildings.
The second line contains  space-separated integers, each the height of a building.

Problem link: https://www.hackerrank.com/challenges/largest-rectangle/problem?isFullScreen=true

'''


def largestRectangle(h):
    stack = []
    top = -1
    leftSmaller = [-1] * len(h)
    rightSmaller = [-1] * len(h)
    maxArea = 1
    
    for i in range(len(h)):
        if top < 0:
            stack.append(i)
            top += 1
            leftSmaller[i] = 0
        else:
            if h[i] <= h[stack[top]]:
                while top>=0 and h[i] <= h[stack[top]]:
                    stack.pop()
                    top -= 1
                if top>=0:
                    leftSmaller[i] = stack[top] + 1
                else:
                    leftSmaller[i] = 0
                stack.append(i)
                top += 1
            elif h[i] > h[stack[top]]:
                leftSmaller[i] = stack[top] + 1
                stack.append(i)
                top += 1
    
    while top>=0:
        print(top, stack)
        stack.pop()
        top -= 1

    
    for i in range(len(h)-1, -1, -1):
        print(i)
        if top<0:
            stack.append(i)
            top += 1
            rightSmaller[i] = len(h) - 1
            print(rightSmaller)
        else:
            if h[i] <= h[stack[top]]:
                while top>=0 and h[i] <= h[stack[top]]:
                    stack.pop()
                    top -= 1
                if top>=0:
                    rightSmaller[i] = stack[top] - 1
                else:
                    rightSmaller[i] = len(h) - 1
                stack.append(i)
                top += 1
            elif h[i] > h[stack[top]]:
                rightSmaller[i] = stack[top] - 1
                stack.append(i)
                top += 1
                
    
    for i in range(len(h)):
        maxArea = max(maxArea, h[i] * (rightSmaller[i] - leftSmaller[i] + 1) )
    
    return maxArea