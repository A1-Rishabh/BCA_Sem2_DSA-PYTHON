rows=3
columns=3
a = []
b = []
sum=[]
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter the value at [{i}{j}]:"))
        row.append(value)
    a.append(row)

for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter the value at [{i}{j}]:"))
        row.append(value)
    b.append(row)
print(a)
print(b)

for i in range (rows):
    row=[]
    for j in range(columns):
        row.append(a[i][j]+ b[i][j])
    sum.append(row)
print("Sum=",sum)