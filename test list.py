list = [int(e) for e in input("Enter List : ").split()]

print(list)
list.remove(int(input("Enter number to remove : ")))
print(list)
print(max(list))