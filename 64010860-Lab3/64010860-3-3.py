gem = input("Enter Input : ").split()
stack = []
i=0
combo=0
maxcombo=0
resetcombo=0
for x in gem:
    stack.append(x)
    #pos = gem.index
    
    if (i >= 2 and stack[i-1]==x and stack[i-2]==x):
        #print(stack[i-1])
        #print(stack[i-2])
        
        stack.pop()
        stack.pop()
        stack.pop()
        i-=3
        combo+=1
        resetcombo=0
        if (combo>maxcombo):
            maxcombo=combo
    else:
        resetcombo+=1
        if (resetcombo>2):
            combo=0
    i+=1

print(len(stack))
if (len(stack)>0):
    stack.reverse()
    leftover = ''
    for y in stack:
        leftover+=y
    print(leftover)
else:
    print('Empty')



if(maxcombo>=2):
    print('Combo : '+str(maxcombo)+' ! ! !')
