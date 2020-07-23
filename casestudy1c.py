#getting numbers between 1000 and 3000 that have an even number in them

items = []
for i in range(1000, 3001):
    x = str(i)
    if (int(x[0])%2==0) and (int(x[1])%2==0) and (int(x[2])%2==0):
        items.append(x)
print(items)