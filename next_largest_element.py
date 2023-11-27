def nextLargerElement(arr,n):
        
        stack = [arr[n-1]]
        top = 0
        result = [0] * n
        result[n-1] = -1
        
        for i in range(n-2, -1, -1):
            if arr[i] < stack[top]:
                result[i] = stack[top]
                stack.append(arr[i])
                top += 1
            else:
                while top >= 0 and stack[top] <= arr[i]:
                    stack.pop(top)
                    top -= 1
                if top < 0:
                    result[i] = -1
                else:
                    result[i] = stack[top]
                    
                stack.append(arr[i])
                top += 1
                
        return result
        

if __name__ == "__main__": 
    result = nextLargerElement([6, 8, 0, 1, 3], 5)
    print(result)