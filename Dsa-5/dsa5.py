rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

matrix = []
# creation of matrix
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input("Enter the value:"))
        row.append(value)
    matrix.append(row)

print("Matrix")

# # traversal of matrix 
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()

# # visiting primary diagonal
# for i in range(rows):
#     print(matrix[i][i],end=" ")
# # visiting secondary diagonal
# for i in range(rows):
#     print(matrix[i][columns-1-i],end=" ")

# # visiting all elements in row wise manner
# for i in range(rows):
#     for j in range(columns):
#         print(matrix[i][j],end=" ")
# # visiting all elements in column wise manner
# for j in range(columns):
#     for i in range(rows):
#         print(matrix[i][j],end=" ")
# # calculate the sum of rows  and columns
# for i in range(rows):
#     sum=0
#     sumcol=0
#     for j in range(columns):
#         sum=sum+matrix[i][j]
#         sumcol=sumcol+matrix[j][i]
#     print("sum of rows: ",sum)
#     print("sum of columns: ",sumcol)
#sum of primary diagonal
sum=0
for i in range(rows):
    sum=sum+matrix[i][i]
print("sum of primary diagonal: ",sum)