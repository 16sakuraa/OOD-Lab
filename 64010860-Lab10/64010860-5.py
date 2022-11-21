def FindMinWeight(item,box):
    minWeight = 10000000
    if box == 1:
        return sum(item)
    
    for i in range(len(item)):
        if len(item[i:]) < box - 1:
            break

        boxI = sum(item[:i])
        theRest = FindMinWeight(item[i:],box - 1)
        minWeight = min(max(boxI,theRest),minWeight)
    return minWeight




allItem , numBox = input("Enter Input : ").split('/')
item = [int(e) for e in allItem.split()]
minWeight = FindMinWeight(item,int(numBox))
print('Minimum weigth for '+str(numBox)+' box(es) = '+str(minWeight))
# Minimum weigth for 3 box(es) = 8
