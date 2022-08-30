
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

    def insertFirst(self,data):
        node = Node(data,self.head)
        self.head = node

    def insertLast(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data,None)

    def removeAt(self,index):
        if index==0:
            self.head = self.head.next
        
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1

    def insertValue(self,index,data):
        count=0
        if index==0:
            self.insertFirst(data)
            return
        
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count +=1

        
    def print(self):
        if self.head is None:
            print('This linked list is empty')
            return
        
        itr = self.head
        liststr = ''

        while itr:
            #print(itr)
            if itr.next is None:
                liststr += str(itr.data)
            else:
                liststr += str(itr.data) + ' <- '
            itr = itr.next
            
        print(liststr)
    
    def findZero(self):
        current = self.head
        while current.data != '0':
            self.insertLast(current.data)
            self.removeAt(0)
            current = current.next
          
            
        
        
            

print(' *** Locomotive ***')
inputstr = [e for e in input('Enter Input : ').split()]

ll1 = Linkedlist()
print('Before : ',end='')
for x in range(len(inputstr)):
    ll1.insertLast(inputstr[x])

ll1.print()
ll1.findZero()
print('After : ',end='')
ll1.print()

    


