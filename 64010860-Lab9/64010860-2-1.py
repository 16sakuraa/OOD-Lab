
def isitsort(num,i):
    maxIndex = len(num)-1
    if i==maxIndex:
        return True
    elif num[i]>num[i+1]:
        return False
    else:
        return isitsort(num,i+1)

def findMin(A, n):
     

    if (n == 1):
        return A[0]
    return min(A[n - 1], findMin(A, n - 1))

def findMax(A, n):
 
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMax(A, n - 1))


def straightselectsort(num,left,right):
    maxIndex = len(num)-1
    if isitsort(num,0):
        return num
    else:
        indexMax = index(findMax(num,))

        print('swap '+str(num[maxIndex-right])+' <-> '+str(num[left])+' : ',end='')
        dummy = num[maxIndex-right]
        num[maxIndex-right]=num[left]
        num[left]= dummy
        print(num)


    if right<maxIndex:
        return straightselectsort(num,left,right+1)
    elif right==maxIndex:
        return straightselectsort(num,left+1,0)


num = [int(e) for e in input('Enter Input : ').split()]
print(straightselectsort(num,0,0))

