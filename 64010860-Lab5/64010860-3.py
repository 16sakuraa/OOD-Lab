class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next
    # def __str__(self):
    #     if self.head is None:
    #         print('This linked list is empty')
    #         return
        
    #     itr = self.head
    #     liststr = ''

    #     while itr:
    #         #print(itr)
    #         if itr.next is None:
    #             liststr += str(itr.data)
    #         else:
    #             liststr += str(itr.data) + ' <- '
    #         itr = itr.next
            
    #     print(liststr)

    #def traverse(self):

def createList(L=[]):
    newnode = node(L[0])
    head = newnode

    for i in range(0,len(L)-1):
        tempnode = node(L[i+1])
        newnode.next = tempnode
        #print(i)
        newnode = tempnode


    return head

def printList(H):
    itr = H
    y=''
    while itr:
        y += str(itr.data)
        itr = itr.next
    
    print(y)

# def mergeOrderesList(p,q):
#     ### Code Here ###

#################### FIX comand ####################   
# input only a number save in L1,L2

L1,L2 = [e for e in input('Enter Input : ').split(',')]

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
# m = mergeOrderesList(LL1,LL2)
# print('Merge Result : ',end='')
# printList(m)