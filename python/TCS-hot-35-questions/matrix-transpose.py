# Given an R×C matrix, print its transpose (rows become columns, columns become rows).
# Sample input
# 2 3
# 1 2 3
# 4 5 6
# Sample output
# 1 4
# 2 5
# 3 6
r,c = map(int,input().split())

matrix = []
for _ in range(r):
        row = list(map(int,input().split()))
        matrix.append(row)
for j in range(c):
    for i in range(r):
        print(matrix[i][j],end = ' ')
    print()
    
    
# to rotate 90 degree
# for row in matrix:
#     row.reverse()
# print(matrix)