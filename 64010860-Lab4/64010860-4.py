inputString = [e for e in input("Enter Input : ").split(',')]

my = []
your = []
activity = ['Eat','Game','Learn','Movie']
location = ['Res.','ClassR.','SuperM.','Home']


for x in inputString:
    a,b = x.split()
    c,d = a.split(':')
    my.append(a)
    your.append(b)

print('My   Queue = ',end ="")
for y in range(len(my)):
    print(my[y],end = "")
    if y < len(my)-1:
        print(',',end=" ")

print('\nYour Queue = ',end ="")
for z in range(len(your)):
    print(your[z],end = "")
    if z < len(your)-1:
        print(',',end=" ")

totalscore=0
myRes = ''
yourRes = ''
for i in range(len(inputString)):
    a1,l1 = my[i].split(':')
    a2,l2 = your[i].split(':')
    if (a1==a2 and l1==l2):
        totalscore+=4
    elif (a1!=a2 and l1==l2):
        totalscore+=2
    elif (a1==a2 and l1!=l2):
        totalscore+=1
    else:
        totalscore-=5
    if i == len(inputString)-1:
        myRes+= activity[int(a1)]+':'+location[int(l1)]
        yourRes+= activity[int(a2)]+':'+location[int(l2)]
    else:
        myRes+= activity[int(a1)]+':'+location[int(l1)]+', '
        yourRes+= activity[int(a2)]+':'+location[int(l2)]+', '
    
print('\nMy   Activity:Location = '+myRes)
print('Your Activity:Location = '+yourRes)


if totalscore >=7:
    print("Yes! You're my love! : Score is "+str(totalscore)+".")
elif totalscore <7 and totalscore>0:
    print("Umm.. It's complicated relationship! : Score is "+str(totalscore)+".")
else:
    print("No! We're just friends. : Score is "+str(totalscore)+".")