normal,mirror=input('Enter Input (Normal, Mirror) : ').split()

i=0
mirrorEx=0
mirrorRes = []
item = []
for x in mirror[::-1]:
    mirrorRes.append(x)
    if i>=2 and mirrorRes[i-1]==x and mirrorRes[i-2]==x:
        mirrorEx+=1
        mirrorRes.pop()
        mirrorRes.pop()
        mirrorRes.pop()
        item.append(x)
        i-=3
    i+=1

normalRes = []
normalEx = 0
fail = 0
j = 0
for y in normal:
    normalRes.append(y)
    if j>=2 and normalRes[j-1]==y and normalRes[j-2]==y and len(item)>0:
        normalRes.pop()
        normalRes.append(item[0])
        item.pop(0)
        normalRes.append(y)
        j+=1
    elif j>=2 and normalRes[j-1]==y and normalRes[j-2]==y and len(item)==0:
        normalEx+=1
        normalRes.pop()
        normalRes.pop()
        normalRes.pop()
        j-=3

    if j>=2 and normalRes[j-1]==y and normalRes[j-2]==y:
        fail+=1
        normalRes.pop()
        normalRes.pop()
        normalRes.pop()
        j-=3

    j+=1

print('NORMAL :')
print(len(normalRes))
if (len(normalRes)>0):
    normalRes.reverse()
    leftover = ''
    for z in normalRes:
        leftover+=z
    print(leftover)
else:
    print('Empty')
print(str(normalEx)+' Explosive(s) ! ! ! (NORMAL)')
if(fail>0):
    print('Failed Interrupted '+str(fail)+' Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(len(mirrorRes))
if (len(mirrorRes)>0):
    leftover = ''
    mirrorRes.reverse()
    for a in mirrorRes:
        leftover+=a
    print(leftover)
else:
    print('ytpmE')
print('(RORRIM) ! ! ! (s)evisolpxE '+str(mirrorEx))
