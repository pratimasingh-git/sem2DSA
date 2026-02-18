# Rotate the matrix by 90 degree in anti-clockwise
#STEP1: transpose of orignal matrix
#STEP2: reverse the order of each row of transposed matrix

matrix=[[1,2,3],[4,5,6],[7,8,9]]

rows= len(matrix)
column=len(matrix[0])

tRows= column
tCloumn= rows

transpose=[]

for r in range(tRows):
    rowArr=[]
    for c in range(tCloumn):
        rowArr.append(0)
    transpose.append(rowArr)

print(transpose)

# 1. transpose of matrix

for r in range(rows):
    for c in range(column):
        transpose[c][r]= matrix[r][c]

# 2. reverse the order of each row of transposed matrix

transpose.reverse()

print(transpose)