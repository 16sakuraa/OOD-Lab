class node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

def createList(List=[]):
    L = [e for e in List.split()]
    newnode = node(int(L[0]))
    head = newnode
    for i in range(0,len(L)-1):
        tempnode = node(int(L[i+1]))
        newnode.next = tempnode
        newnode = tempnode
    return head

def printList(H):
    itr = H
    y=''
    while itr:
        y += str(itr.data)+' '
        itr = itr.next
    print(y)

def mergeOrderesList(p,q):
    dummy = node(0)
    tail = dummy

    while True:
        if p is None:
            tail.next = q
            break
        if q is None:
            tail.next = p
            break

        if p.data <= q.data:
            tail.next = p
            p = p.next
        else:
            tail.next = q
            q = q.next

        tail = tail.next
    
    return dummy.next

#################### FIX comand ####################   
# input only a number save in L1,L2

L1,L2 = [e for e in input('Enter Input : ').split(',')]

LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)