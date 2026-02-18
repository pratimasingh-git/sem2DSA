
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

#row_wise_transversal = []

for r in range(rows):
    for c in range(columns):
        print(matrix[r][c], end=' ')
    print()

#cloumn wise transversal

for c in range(columns):
    for r in range(rows):
        print(matrix[r][c],end='')
    print()