print('*** TorKham HanSaa ***')
listinput = []
listinput = [str(e) for e in input("Enter Input : ").split(',')]

stack = []
i=0
while i < len(listinput):
    if listinput[i][0] == 'R':
        stack.clear()
        print('game restarted')
        del listinput[:i+1]
        i=0
    elif listinput[i][0] =='X':
        exit()
    else:
        char,word = listinput[i].split()
        if char == 'P':
            if len(stack)==0:
                stack.append(word)
                print("'"+str(word)+"' -> "+str(stack))
                i+=1
            elif word[1].lower() == stack[i-1][len(stack[i-1])-1].lower() and word[0].lower() == stack[i-1][len(stack[i-1])-2].lower():
                stack.append(word)
                print("'"+str(word)+"' -> "+str(stack))
                i+=1
            else:
                print("'"+str(word)+"' -> game over")
                break
        elif char == 'p':
            print("'"+str(listinput[i]+"' is Invalid Input !!!"))
            break
        
  

        