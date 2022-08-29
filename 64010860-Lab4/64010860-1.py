inputString = [e for e in input('Enter Input : ').split(',')]

queue = []

for x in range(len(inputString)):

    if inputString[x][0] == 'E':
        action,value = inputString[x].split()
        queue.append(value)
        print(len(queue))
    
    elif inputString[x][0] == 'D':
        if (len(queue)>0):
            print(str(queue[0])+' '+str(queue.index(queue[0])))
            queue.pop(0)
        else:
            print('-1')

if len(queue)==0:
    print('Empty')

while (len(queue)>0):
    print(str(queue[0]), end=" ")
    queue.pop(0)


    