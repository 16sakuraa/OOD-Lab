power,comp = input('Enter Input : ').split('/')
powerNum = [int(e) for e in power.split()]
compNum = [e for e in comp.split(',')]

total=0
for i in powerNum:
    total+=i
print(total)

for i in compNum:
    
    a,b = [int(e) for e in i.split()]
    totalA=powerNum[a]
    totalB=powerNum[b]
    
    for i in range(1,2):
        if 2*a+i <= len(powerNum)-1:
            totalA+=powerNum[2*a+i]
        if 2*b+i <= len(powerNum)-1:
            totalB+=powerNum[2*b+i]
   
    if totalA>totalB:
        print(str(a)+'>'+str(b))
    elif totalB>totalA:
        print(str(a)+'<'+str(b))
    else:
        print(str(a)+'='+str(b))