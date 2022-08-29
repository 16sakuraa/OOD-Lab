
treeString = [e for e in input("Enter Input : ").split(',')]

stackAction = []
stackHeight = []

count = []
for i in range(len(treeString)):
    
    if treeString[i][0] == 'B':
        for j in stackHeight:
            if len(count) > 0:
                if (all(x < j for x in count)):
                    count.clear()
                    count.append(j)
                elif (all(x > j for x in count)):
                    count.append(j)
                else:
                    for k in count:
                        if (j > k):
                            count.pop()
                    count.append(j)
            else:
                count.append(j)
        res = [*set(count)]
        res.sort(reverse=True)
        print(len(res))
        count.clear()

    elif treeString[i][0] == 'A':
        a,h = treeString[i].split()
        stackAction.append(a)
        stackHeight.append(int(h))
    
    elif treeString[i][0] == 'S':
        for i in range(len(stackHeight)):
            if stackHeight[i]%2==0:
                stackHeight[i]-=1
            else:
                stackHeight[i]+=2
