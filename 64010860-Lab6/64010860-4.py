
best = 1000000000

def diff(a,b):
    if a>b:
        c = a-b
        return int(c)
    elif b>a:
        c = b-a
        return int(c)

def perket(index,s,b):
    global sour
    global bit
    global n
    global best


    if index==n:
        if b>0 and diff(s,b) < int(best):
            best = diff(s,b)
        #print(best)
        return best

    else:
        perket(index+1,s,b)
        perket(index+1,s*sour[index],b+bit[index])




inputString = [e for e in input('Enter Input : ').split(',')]

sour = []
bit = []

for x in inputString:
    a,b = x.split()
    sour.append(int(a))
    bit.append(int(b))


n = len(inputString)
perket(0,1,0)
print(best)



