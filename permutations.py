
def permute(A, subarr, left, right, k):
    if left == right:
        for i in range(len(A)):
            if abs((i+1) - A[i]) != k:
                break
        if i == len(A)-1 and abs(A[i] - (i+1)) == k:
            subarr.append(list(A))
    
    for i in range(left, right):
        A[left], A[i] = A[i], A[left]
        permute(A, subarr, left + 1, right, k)
        A[left], A[i] = A[i], A[left]



def foo(nums):
    # Declaring result variable
    x = len(nums);
    res = [];
    
    k = 1
    # Calling permutations for the first
    # time by passing l
    # as 0 and h = nums.size()-1
    permute(nums, res, 0, x, k);
    return res;
        
if __name__ == "__main__":
    A = [1,2]
    subarr = []
    subarr = foo(A)
    print(subarr)