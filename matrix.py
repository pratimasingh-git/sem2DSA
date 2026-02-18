rows = int(input("Enter rows: "))
columns = int(input("Enter columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        value =int(input(f"Enter value for position: "))
        row.append(value)
    matrix.append(row)

print(matrix)


#wap to print the upper triangle  of a matrix

for r in range(rows - 1):
    for c in range(r+1, columns):
        print(matrix[r][c], end="")
    print()
    
for r in range(1, rows):
    for c in range(r):
        print(matrix[r][c], end="")
    print()