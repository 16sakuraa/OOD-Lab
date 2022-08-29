

class Stack:

    #mylist = list()

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

   # def items(self):
    #    print(self.mylist)




print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.getSize(),"Data in stack : ",s.items)

while not s.isEmpty():
    s.pop()

print(s.getSize(),"Data in stack : ",s.items)