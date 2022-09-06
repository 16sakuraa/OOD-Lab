class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur,s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            #print('test '+str(cur.value))
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newnode = Node(value=item)
        last = self.head
        newnode.next = None

        if self.head is None:
            #self.head.previous = None
            self.head = newnode
            self.tail = newnode
            return
        
        while (last.next is not None):
            last = last.next
        
        last.next = newnode
        newnode.previous = last
        self.tail = newnode
            

    def addHead(self, item):
        
        newnode = Node(value=item)
        newnode.next = self.head
        newnode.previous = None

        if self.head is not None:
            self.head.previous = newnode
        
        if self.head is None:
            self.tail = newnode

        self.head = newnode

    def insert(self, pos, item):
        if pos==0:
            self.addHead(item)
            return
        elif pos<0:
            pos = self.size()+pos
            if pos<0:
                self.addHead(item)
                return
        elif pos==self.size() or self.isEmpty() or pos>=self.size():
            self.append(item)
            return

        count=0

        newnode = Node(value=item)

        itr = self.head
        while itr:
            if count == pos-1:
                itr.next.previous = newnode
                newnode.next = itr.next
                newnode.previous = itr
                itr.next = newnode

                break

            itr = itr.next
            count +=1
    
    def removeAt(self,index):
        if index==0:
            self.head = self.head.next
        elif index==self.size():
            self.pop()


        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count+=1



    def search(self, item):
        itr = self.head
        while itr:
            if itr.value == item:
                print('Found')
                return 
            itr = itr.next
        print('Not Found')
        return



    def index(self, item):
        itr = self.head
        count = 0
        while itr:
            if itr.value == item:
                return count
            itr = itr.next
            count+=1
        return -1

    def size(self):
        size = 0
        itr = self.head
        while itr:
            itr = itr.next
            size+=1
        #print(size)
        return size

    def pop(self, pos):
        if pos<0 or self.size()<pos:
            #print('Out of Range')
            return

        count=0
        itr = self.head
        if pos==self.size():
            while itr.next.next is not None:
                itr=itr.next
            itr.next = None
            return
        while itr:
            if pos==0:
                self.head = self.head.next
                #print('Success')
                return
            elif count == pos-1:
                itr.next = itr.next.next
                #print('Success')
                return
            itr = itr.next
            count+=1
    
    def print(self):
        if self.head is None:
            print('This linked list is empty')
            return
        
        itr = self.head
        liststr = ''

        while itr:
            #print(itr)
            if itr.next is None:
                liststr += str(itr.value)
            else:
                liststr += str(itr.value) + ' '
            itr = itr.next
            
        print(liststr)

L = LinkedList()

inputString = [e for e in input('Enter Input : ').split(',')]

cursorPos = 0
for x in inputString:
    if x[0] == 'I':
        a,b = x.split()
        L.insert(cursorPos,b)
        cursorPos+=1
    elif x[0] == 'L':
        if cursorPos>0:
            cursorPos-=1
    elif x[0] == 'R':
        if cursorPos<L.size():
            cursorPos+=1
    elif x[0] == 'B':
        if cursorPos>0:
            L.pop(cursorPos-1)
            cursorPos-=1
    elif x[0] == 'D':
        if cursorPos==0:
            L.pop(0)
        elif cursorPos<L.size():
            L.pop(cursorPos+1)

L.insert(cursorPos,'|')
L.print()