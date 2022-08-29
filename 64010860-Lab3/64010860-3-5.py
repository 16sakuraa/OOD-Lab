from inspect import stack


treeString = [e for e in input("Enter Input : ").split(',')]
#print(treeString)

stackAction = []
stackHeight = []

count = 0
max = 0
previousMax = []
for i in range(len(treeString)):
    
    if treeString[i][0] == 'B':
        stackAction.append('B')
        stackHeight.append(int('-1'))

        for j in range(len(stackHeight)-1):

            if stackHeight[j+1] < stackHeight[j] and stackHeight[j+1]>0 and stackHeight[j]>0:
                count+=1
                if (j>max):
                    max=j
            elif stackHeight[j+1]>stackHeight[j] and stackHeight[j+1]>0 and stackHeight[j]>0:
                if stackHeight[j+1] > max:
                    count=0
                    max=stackHeight[j+1]
                elif stackHeight[j+1]<max:
                    if len(previousMax)==0:
                        previousMax.append(stackHeight[j+1])
                    for k in previousMax:
                        if stackHeight[j+1]>k:
                            previousMax.pop()
                        if previousMax.index(k) == len(previousMax)-1:
                            previousMax.append(stackHeight[j+1])
                    count=len(previousMax)

            if stackHeight[j+1] == -1:
                if stackHeight[j]>max:
                    max=stackHeight[j]
                    count=1
                elif stackHeight[j]<max:
                    

            #if j+1 == len(treeString) and stackHeight[j+1] > 0:
            #    if stackHeight[j+1]>max:
            #        max=stackHeight[j+1]
            #        count=1
            #    elif stackHeight[j+1]>stackHeight[j]

        print(count)

    elif treeString[i][0] == 'A':
        a,h = treeString[i].split()
        stackAction.append(a)
        stackHeight.append(int(h))

print(stackAction)
print(stackHeight)