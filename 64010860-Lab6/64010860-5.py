def asteroid_collision(asts,index):

    if index < len(asts)-1:
        if asts[index]>0: # current asteroid go right

            if abs(asts[index])>abs(asts[index+1]) and asts[index+1]<0:
                del asts[index+1]
                return asteroid_collision(asts,index)

            elif abs(asts[index])<abs(asts[index+1]) and asts[index+1]<0:
                del asts[index]
                return asteroid_collision(asts,index-1)
            
            elif abs(asts[index])==abs(asts[index+1]) and asts[index+1]<0:
                del asts[index]
                del asts[index]
                if index>0:
                    return asteroid_collision(asts,index-1) # last edit : add -1
                else:
                    return asteroid_collision(asts,index)

        elif asts[index]<0 and index>0: # current asteroid go left

            if abs(asts[index])>abs(asts[index-1]) and asts[index-1]>0:
                del asts[index-1]
                return asteroid_collision(asts,index-1)

            elif abs(asts[index])<abs(asts[index-1]) and asts[index-1]>0:
                del asts[index]
                return asteroid_collision(asts,index-1)

            elif abs(asts[index])==abs(asts[index-1]) and asts[index-1]>0:
                del asts[index]
                del asts[index-1]
                return asteroid_collision(asts,index-2) # last edit : add -1

                # 5, 3, 3, -3, -3 index = 2
                # 5, 3, -3 index=2
                # 5 index = 0

                # -5, 5, 3, 3, -3, -3
                # 5, -5, 3, 3, -3, -3

        return asteroid_collision(asts,index+1)
        
    elif index == len(asts)-1:

        if asts[index]<0:
            if asts[index-1]>0 and abs(asts[index-1])>abs(asts[index]):
                del asts[index]

            elif asts[index-1]>0 and abs(asts[index-1])<abs(asts[index]):
                del asts[index-1]

            elif asts[index-1]>0 and abs(asts[index-1])==abs(asts[index]):
                del asts[index]
                del asts[index-1]

        return asts
    
    elif index > len(asts)-1:
        return asts
        

x = input("Enter Input : ").split(",")
x = list(map(int,x))
print(asteroid_collision(x,0))