'''

You have an empty sequence, and you will be given  queries. Each query is one of these three types:
1 x  -Push the element x into the stack.
2    -Delete the element present at the top of the stack.
3    -Print the maximum element in the stack.
Function Description
Complete the getMax function in the editor below.
getMax has the following parameters:
- string operations[n]: operations as strings
Returns
- int[]: the answers to each type 3 query


Link to the problem: https://www.hackerrank.com/challenges/maximum-element/problem

'''


def getMax(operations):
    stack = []
    output = []
    max_stack = []

    for operation in operations:
        indicator = operation[0]
        if indicator == '1':
            value = int(operation.split(' ')[1])
            stack.append(value)
            if max_stack:
                if max_stack[len(max_stack) - 1] <= value:
                    max_stack.append(value)
            else:
                max_stack.append(value)
        elif indicator == '2':
            if stack:
                popped_value = stack[len(stack) - 1]
                stack = stack[:len(stack) - 1]
                if max_stack:
                    if max_stack[len(max_stack) - 1] == popped_value:
                        max_stack = max_stack[:len(max_stack) - 1]
        elif indicator == '3':
            if max_stack:
                output.append(max_stack[len(max_stack) - 1])

    return output

