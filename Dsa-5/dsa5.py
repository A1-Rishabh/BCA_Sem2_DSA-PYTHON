# rows = int(input("Enter rows: "))
# columns = int(input("Enter columns: "))

# matrix = []
# # creation of matrix
# for i in range(rows):
#     row = []
#     for j in range(columns):
#         value = int(input("Enter the value:"))
#         row.append(value)
#     matrix.append(row)

# print("Matrix")

# # traversal of matrix
# for i in range(rows):
#     for j in range(columns):
#         print(matrix[i][j],end=" ")
#     print()


row=int(input("enter a number in row"))
colomn=int(input("enter a number in colomn"))
matrix =[]
for i in range(row):
    row=[]
    for _ in range(colomn):
        value = int(input("enter a value position"))
        row.append(value)
    matrix.append(row)

print(matrix)

for i in range(row):
    for j in range(colomn):
        print(matrix[i][j],end=" ")
    print()