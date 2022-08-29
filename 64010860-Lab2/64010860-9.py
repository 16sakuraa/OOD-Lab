#from tkinter import Y


numbers = [int(e) for e in input("Enter Your List : ").split()]
setlist = []
if len(numbers) < 3:
    print('Array Input Length Must More Than 2')
else:

    for x in range(0,len(numbers)-2):
        for y in range(x+1,len(numbers)-1):
            for z in range(y+1,len(numbers)):
                if numbers[x]+numbers[y]+numbers[z] == 5:
                    temp = []
                    temp.append(numbers[x])
                    temp.append(numbers[y])
                    temp.append(int(numbers[z]))
                    temp.sort()
                    if (len(setlist) > 0):
                        if temp not in setlist:
                            setlist.append(temp)
                    else:
                        setlist.append(temp)
    print(setlist)


                            





#-3 2 4 6 8 10
#5 -5 5 -5 5 -5 5 5 -5 -5 -5 -5 5
#-25 -10 -7 -3 2 4 8 10