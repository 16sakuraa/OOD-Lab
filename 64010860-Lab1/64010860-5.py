print('*** Fun with countdown ***')
numbers = [int(e) for e in input("Enter List : ").split()]
#numbers.sort()

#print(numbers)
count=0
for x in numbers:
    if (x==1):
        count+=1
#print(count + '\n')

res =[] 

# 4 4 5 4 3 2 1 8 3 2 1


for i in range(count):
    templist = []
    
    #temp=1
    temp=max(numbers)
    
    #templist.append(temp)
    numbers.remove(max(numbers))
    while( temp-1 not in numbers and temp!=1):
      #  numbers.remove(max(numbers))
        temp=max(numbers)
    
    templist.append(temp)
    
    for j in numbers:
        if j==temp-1:
            templist.append(j)
            temp=j
            numbers.remove(j)
    res.append(templist)

print('['+str(count)+', '+str(res)+']')





