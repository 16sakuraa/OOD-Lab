def findMin(numlist):
    min=numlist[0]
    for i in numlist:
        if i<min:
            min = i
    return min
    

l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "Quick Sort"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    lcopy = l.copy()
    res = []
    median,count = 0,0
    listCopy = []
    while(len(l)>0):
        item = lcopy[count]
        listCopy.append(item)
        count+=1
        res.append(findMin(l))
        l.remove(findMin(l))
        if len(res)%2==0:
            a = res[int((len(res)/2)-1)]
            b = res[int((len(res)/2))]
            median = (a+b)/2
        elif len(res)%2!=0:
            median = float(res[int(len(res)/2)])
        print('list = ',end='')
        #print(listCopy,end='')
        print(res,end='')
        print(' : median = '+str(median))
        
    