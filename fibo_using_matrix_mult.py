
def mult(a, b):
    result = [[0 for _ in range(len(b))] for _ in range(len(a))]
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                result[i][j] += a[i][k] * b[k][j]
                
    for i in range(len(result)):
        for j in range(len(result[0])):
            a[i][j] = result[i][j]
    
def power(F, n):
    if n <= 1:
        return
    M = [[1,1], [1,0]]
    
    power(F, n//2)
    mult(F, F)
    
    if n%2 != 0:
        mult(F, M)

def fibo(n):
    if n == 0:
        return 0
    F = [[1,1], [1,0]]
    
    power(F, n-1)
    return F[0][0]
            
if __name__ == "__main__":
    r = fibo(1000)
    print(r)

    
