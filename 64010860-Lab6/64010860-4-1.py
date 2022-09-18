ingre = int(input())
x = []
y = []
diff = []
for i in range(ingre):
    xData,yData = [int(num) for num in input().split()]
    for j in range(len(x)):
        x.append(x[j]*xData)
        y.append(y[j]+yData)
    x.append(xData)
    y.append(yData)
for i in range(len(x)):
    diff.append(abs(x[i]-y[i]))
print(min(diff))