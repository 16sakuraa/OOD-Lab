def Min(A, n):
     
    if (n == 1):
        return A[0]
    return min(A[n - 1], Min(A, n - 1))

numList = [int(e) for e in input('Enter Input : ').split()]
n = len(numList)
print('Min : '+str(Min(numList,n)))