

class Stack:

    def __init__(self):
        self.size = 0
        self.mylist = []
        self.items = self.mylist

    def push(self,item):
        self.mylist.append(item)

    def pop(self):
        self.mylist.remove(self.mylist[len(self.mylist)-1])
    
    def isEmpty(self):
        if len(self.mylist) > 0:
            return 0
        else:
            return 1 

    def getSize(self):
        return len(self.mylist)


inp = input('Enter Input : ').split()

S = Stack()

i=0
combo=0
maxcombo=0
resetcombo=0

for x in inp:
    S.push(x)
    #print(x)
    if i >= 2 and S.items[i-1]==x and S.items[i-2]==x:
        combo+=1
        S.pop()
        S.pop()
        S.pop()
        i-=3
        if combo>maxcombo:
            maxcombo=combo
    i+=1

str1 =''

for y in reversed(S.items):
    str1+=y
print(S.getSize())
if S.isEmpty():
    print("Empty")
else:
    print(str1) 


if combo>=2:
    print('Combo : '+str(maxcombo)+' ! ! !')

