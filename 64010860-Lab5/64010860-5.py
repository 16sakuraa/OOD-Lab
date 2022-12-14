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
          #  self.head.previous = None
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
    
    def replace(self,pos,item):
        count=0
        newnode = Node(value=item)
        itr = self.head
        while itr:
            if count == pos-1:
                itr.value = newnode.value
                break
            itr = itr.next
            count +=1


    def search(self, item):
        itr = self.head
        while itr:
            if itr.value == item:
                return 'Found'
            itr = itr.next
        return 'Not Found'



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
        if pos<0 or self.size()<=pos:
            return 'Out of Range'
        
        count=0
        itr = self.head
        while itr:
            if pos==0:
                self.head = self.head.next
                return 'Success'
            elif count == pos-1:
                itr.next = itr.next.next
                return 'Success'
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
                liststr += str(itr.value) + ' <- '
            itr = itr.next
            
        print(liststr)
    
    def findmax(self):
        maxNum = self.head.value
        itr = self.head
        while itr:
            if itr.value > maxNum:
                maxNum = itr.value
            itr = itr.next
        
        print(maxNum)
        return maxNum
    
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

    def radixsort(self):
        box = []
        for i in range(10):
            box.append(LinkedList(0))
        print("------------------------------------------------------------")
        stop = False
        counter = 0
        for i in range(self.max_length+1):
            print("Round : " + str(i+1))
            while not self.isEmpty():
                temp = self.removeAt(0)[::-1]
                try:
                    box[int(temp[i])].addHead(temp[::-1])   
                    print(temp[i],end=' from ')
                    print(temp[::-1])
                except:
                    box[0].addHead(temp[::-1])
            if box[0].size() == self.max:
                stop = True
            for j in range(10):
                box[j].sort()
                print(str(j) + ' : ' + box[j].print())
                while not box[j].isEmpty():
                    temp = box[j].addHead()
                    self.append(temp)
            print("------------------------------------------------------------")
            counter += 1
            if stop:
                break
        self.max_length = counter



# def countingSort(arr, exp1):
 
#     n = arr.size()
#     # output = []
#     # count = []

#     # for i in range(n):
#     #     output.append(0)
    
#     # for j in range(10):
#     #     count.append(0)

#     output = [0] * (n)
#     count = [0] * (10)

#     itr = arr.head
#     while itr:
#         index = int(itr.value)//exp1
#         count[index%10] +=1
#         itr = itr.next
    
#     for k in range(1,10):
#         count[k] += count[k-1]

#     itr = arr.head
#     i = n - 1
#     while i>=0:
#         index = int(itr.value)//exp1
#         output[count[index%10]-1] = int(itr.value)
#         count[index%10]-=1
#         i-=1
#         itr = itr.next


#     LLoutput = LinkedList()
#     for element in output:
#         LLoutput.append(int(element))
    
#     arr = LLoutput
#     arr.print()
#     return arr
        

# def radixsort(arr):

#     maxNum = arr.findmax()

#     divide = 1
#     while maxNum / divide >= 1:
#         countingSort(arr, divide)
#         divide *= 10
    


    
L =LinkedList()
inputNum = [e for e in input('Enter Input : ').split()]
for i in inputNum:
    L.append(int(i))

#L.findmax()
L.radixsort()


