"""

Trapped rain water problem. GfG.

"""

def trapperRainWater(arr, n):
    if n > 0:
        Lmax = [0] * n
        Rmax = [0] * n
        temp = 0
        trappedWater = 0
        
        # Populate the Lmax array
        for i in range(1, n):
            temp = max(arr[i-1], temp)
            Lmax[i] = temp
        
        print(Lmax)
        temp = arr[n-1]
        
        # Populate the Rmax array
        for i in range(n-2, -1, -1):
            print(arr[i+1], temp)
            temp = max(arr[i+1], temp)
            Rmax[i] = temp

        for i in range(1, n-1):
            amount = min(Lmax[i], Rmax[i]) - arr[i]
            if amount > 0:
                trappedWater += amount
            
        return trappedWater
