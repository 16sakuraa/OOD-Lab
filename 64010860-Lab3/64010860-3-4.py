class Stack :

    def __init__(self,list = None) :
        self.size = 0
        self.list = []
        self.items = self.list

    def isEmpty(self) :
        if len(self.list) > 0:
            return 0
        else:
            return 1 

    def push(self,data) :
        self.list.append(data)

    def pop(self) :
        self.list.remove(self.list[len(self.list)-1])

    def getSize(self) :
        return len(self.mylist)

    def peek(self) :
        return self.list[len(self.list)-1]

def isOperand(ch):
        return ch.isalpha()

def infix2postfix(exp) :

    operatorValue = [0,0,1,1,2,2,3]
    operator =      ['(',')','+','-','*','/','^']
    s = Stack()
    operatorStack = Stack()

    for x in exp:

        if isOperand(x):
            s.push(x)

        elif x == '(':
            operatorStack.push(x)
        elif x == ')':
            while((not operatorStack.isEmpty()) and operatorStack.peek() != '('):
                    a = operatorStack.peek()
                    s.push(str(a))
                    operatorStack.pop()

        else:
            while(not operatorStack.isEmpty()):
                y = operatorValue[operator.index(operatorStack.peek())]
                if operatorValue[(operator.index(x))] <= y:
                    b = operatorStack.peek()
                    s.push(str(b))
                    operatorStack.pop()
                elif y==0:
                    break
                else:
                    break
            
            operatorStack.push(x)

    while not operatorStack.isEmpty():
            c = operatorStack.peek()
            s.push(str(c))
            operatorStack.pop()
            
    res = ''
    for i in s.items:
        if i!='(' and i!=')':
            res += str(i)
    
    return str(res)

print(" ***Infix to Postfix***")

token = input("Enter Infix expression : ")

print("PostFix : ")

print(infix2postfix(token))