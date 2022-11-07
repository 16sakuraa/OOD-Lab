def findMin(numlist):
    min=numlist[0]
    for i in numlist:
        if i<min:
            min = i
    return min

def sortingAndMedian(numlist):
    sortList = []
    while(len(numlist)>0):
        min = findMin(numlist)
        sortList.append(min)
        numlist.remove(min)

    median = 0
    if len(sortList)%2==0:
        a = sortList[int((len(sortList)/2)-1)]
        b = sortList[int((len(sortList)/2))]
        median = (a+b)/2
    elif len(sortList)==1:
        median = float(sortList[0])
    elif len(sortList)%2!=0:
        median = float(sortList[int(len(sortList)/2)])
    
    return median
    

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Quick Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    res = []
    while(len(l)>0):
        res.append(l[0])
        l.remove(l[0])
        print('list = ',end='')
        print(res,end='')
        resCopy = res.copy()
        median = sortingAndMedian(resCopy)
        print(' : median = '+str(median))

        
        