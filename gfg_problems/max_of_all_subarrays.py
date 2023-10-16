"""
Problem link: https://practice.geeksforgeeks.org/problems/maximum-of-all-subarrays-of-size-k3101/1?page=1&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

"""

def max_of_subarrays(arr, n, k):
    
    result = []
    dq = []
    
    for i in range(n):
        if dq and dq[0] == i-k:
            dq.pop(0)
        
        while dq and arr[dq[len(dq)-1]] <= arr[i]:
            dq.pop()
            
        dq.append(i)
        
        if i>=k-1:
            result.append(arr[dq[0]])
            
    return result