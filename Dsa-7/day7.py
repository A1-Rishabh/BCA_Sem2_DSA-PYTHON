rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        value = int(input(f"Enter the value for position ({i},{j}): "))
        row.append(value)
    matrix.append(row)

print("Matrix:")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
# Upper triangular matrix 
print("Upper triangular elements (excluding diagonal):")
for r in range(rows-1):
    for c in range(r+1,columns):
        print(matrix[r][c],end=" ")
    print()
# Lower triangular matrix
print("Lower triangular elements (excluding diagonal):")
for r in range(1,rows):
    for c in range(r):
        print(matrix[r][c],end=" ")
    print() 


# Transpose of a matrix
transpose = []

for c in range(columns):
    row = []
    for r in range(rows):
        row.append(matrix[r][c])
    transpose.append(row)

print("Transpose of the matrix:")
for i in range(columns):
    for j in range(rows):
        print(transpose[i][j], end=" ")
    print()