people,time= input("Enter people and time : ").split()

mainQ = []
firstQ = []
secondQ = []

timer1 = 0
timer2 = 0

for i in people:
    mainQ.append(i)

for x in range(1,int(time)+1):
    if len(firstQ) < 5 and len(mainQ) > 0 :
        firstQ.append(mainQ[0])
        mainQ.pop(0)
    
    elif len(firstQ) == 5 and len(secondQ) < 5 and len(mainQ) > 0 :
        secondQ.append(mainQ[0])
        mainQ.pop(0)

    print(x,end =" ")
    print(mainQ,end =" ")
    print(firstQ,end= " ")
    print(secondQ)
    
    if len(firstQ)>0:
        timer1+=1
        if timer1%3==0:
            firstQ.pop(0)

    if len(secondQ)>0:
        timer2+=1
        if timer2%2==0:
            secondQ.pop(0)
        

    
