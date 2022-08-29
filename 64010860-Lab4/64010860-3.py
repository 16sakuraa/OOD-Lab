code,hint= input('Enter code,hint : ').split(',')
dif = ord(hint)-ord(code[0])
queue = []
for x in code:
    char = ord(x)
    char+=dif
    queue.append(chr(char))
    print(queue)

