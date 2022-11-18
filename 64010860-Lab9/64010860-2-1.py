
def isitsort(num,i):
    maxIndex = len(num)-1
    if i==maxIndex:
        return True
    elif num[i]>num[i+1]:
        return False
    else:
        return isitsort(num,i+1)

def findMax(num,i,maxIndex,maxNumber):
    if i>maxIndex:
        return maxNumber
    else:
        if num[i]>maxNumber:
            maxNumber = num[i]
        return findMax(num,i+1,maxIndex,maxNumber)

def straightselectsort(num,maxIndex):
    if isitsort(num,0):
        return num
    else:
        bigNum = findMax(num,0,maxIndex,-1)
        if bigNum==num[maxIndex]:
            return straightselectsort(num,maxIndex-1)
        else:
            index = num.index(bigNum)
            # swap 2 <-> 5 : [2, 4, 3, 1, 5]
            print('swap '+str(num[maxIndex])+' <-> '+str(num[index])+' : ',end='')
            num[index],num[maxIndex] = num[maxIndex],num[index]
            print(num)
            return straightselectsort(num,maxIndex-1)


num = [int(e) for e in input('Enter Input : ').split()]
maxIndex = len(num)-1
print(straightselectsort(num,maxIndex))
