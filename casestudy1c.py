items = []
for i in range(1000, 3001):
    x = str(i)
    if (int(x[0])%2==0) and (int(x[1])%2==0) and (int(x[2])%2==0):
        items.append(x)
print(items)