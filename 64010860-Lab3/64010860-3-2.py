string = input("Enter expresion : ")
#print(string)

stack = []
open = ['(','{','[']
close = [')','}',']']

for x in string:
    if x in open:
        stack.append(x)
    elif x in close:
        position = close.index(x)
        if len(stack) > 0 and open[position] == stack[len(stack)-1]:
            stack.pop()
            #print(stack)
        elif  len(stack) > 0 and open[position] != stack[len(stack)-1]:
            print(string,'Unmatch open-close')
            exit()
        else:
            print(string,'close paren excess')
            exit()
if len(stack) == 0:
    print(string,'MATCH')
elif len(stack) > 0:
    leftover = ''
    for y in stack:
        leftover += y
    print(string,'open paren excess  ',str(len(stack)),':',leftover)


        



