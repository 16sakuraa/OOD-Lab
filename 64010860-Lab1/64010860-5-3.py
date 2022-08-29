print('*** Fun with countdown ***')
numbers = [int(e) for e in input("Enter List : ").split()]

count=0
res =[]
templist = []
# print(len(numbers))
for i in range(len(numbers)-1):
  #  print(numbers[i])
  #  print(numbers[i+1])
    if numbers[i]-1==numbers[i+1] and numbers[i]!=1:
        templist.append(numbers[i])
    elif numbers[i]==1:
        templist.append(numbers[i])
        res.append(templist)
        templist = []
        count+=1
    if numbers[i+1]==1 and i==len(numbers)-2:
            templist.append(numbers[i+1])
            res.append(templist)
            count+=1
  #  print('i ->'+str(i))
    


print('['+str(count)+', '+str(res)+']')