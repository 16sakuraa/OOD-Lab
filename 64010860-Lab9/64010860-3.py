
# insert 2 at index 1 : [1, 2] [3, 4]

def insertNum(numlist,inputnum,i):
    max = findMax(numlist)
    if len(inputnum)==0:
        return numlist
    elif inputnum[0] > max :
        numlist.append(inputnum[0])

        print('insert '+str(inputnum[0])+' at index '+str(numlist.index(inputnum[0]))+' : ',end='')

        inputnum.remove(inputnum[0])
        print(numlist,end=' ')
        if len(inputnum)!=0:
            print(inputnum)
    else:
        index = findSpot(numlist,inputnum[0],0)
        numlist.insert(index,inputnum[0])
        print('insert '+str(inputnum[0])+' at index '+str(numlist.index(inputnum[0]))+' : ',end='')
        inputnum.remove(inputnum[0])
        print(numlist,end=' ')
        if len(inputnum)!=0:
            print(inputnum)
    return insertNum(numlist,inputnum,i)

def findMax(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],findMax(L[1:]))
    
def findSpot(L,item,i):
    if L[i] < item:
        return findSpot(L,item,i+1)
    else:
        return i


inputnum = [int(e) for e in input('Enter Input : ').split(' ')]

numlist = []
numlist.append(inputnum[0])
inputnum.remove(inputnum[0])
print('\nsorted\n'+str(insertNum(numlist,inputnum,0)))

