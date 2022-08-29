print('*** Fun with countdown ***')
numbers = [int(e) for e in input("Enter List : ").split()]

count=0
for x in numbers:
    if (x==1):
        count+=1

res =[] 
# 4 4 5 4 3 2 1 8 3 2 1

for i in range(count):
    templist = []
    temp = max(numbers)
    while(1):
        if (temp in templist and temp-1 in numbers):
            temp = temp-1

        if (temp-1 in numbers and temp!=1):
            templist.append(temp)
            numbers.remove(temp)
            temp = temp-1
                
        elif temp-1 not in numbers:
            numbers.remove(max(numbers))
            temp = max(numbers)
        if temp == 1:
            templist.append(temp)
            break

    while(templist[0]!=1 and templist[0]!=2 and templist[0]!=3 and templist[0]!=5 and templist[0]!=10):
        templist.remove(templist[0])


    res.append(templist)
    
    
if [1] in res:
    sorted_res = sorted(res,key=len)
    print('['+str(count)+', '+str(sorted_res)+']')
else:
    print('['+str(count)+', '+str(res)+']')



