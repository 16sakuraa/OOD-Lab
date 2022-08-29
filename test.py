def mod_position(arr, s):
    charlist = []
    for x in range(len(arr)+1):
        if x%int(s)==0 and x!=0:
            charlist.append(arr[x-1])

    return charlist


print('*** Mod Position ***')
text,num = input("Enter Input : ").split(',')


output = mod_position(text,num)

print(output)
        

